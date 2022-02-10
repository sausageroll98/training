locals {
  local_users_group_name = format("ce%02d Project Users", var.cohort)
  instance               = format("%03d", var.vmid)
  vm_name                = format("vm%stc%s", var.user, local.instance)
  nic_name               = format("nic-%s", local.vm_name)
  public_ip_name         = format("pub-%s", local.vm_name)

  default_tags = tomap({
    "env"      = var.environment
    "pod"      = var.pod
    "creator"  = var.user
    "region"   = data.azurerm_resource_group.deploy.location
    "cohort"   = format("ce%02d", var.cohort)
    "Purpose"  = var.application,
    "usage"    = "windows",
    "platform" = "azure",
    "OS"       = "Windows"
    }
  )
}

data "azurerm_resource_group" "deploy" {
  name = var.resource_group_name
}

data "local_file" "pub" {
  filename = var.public_key_filename
}

resource "azurerm_network_interface" "windows_vm" {
  name                = local.nic_name
  location            = data.azurerm_resource_group.deploy.location
  resource_group_name = data.azurerm_resource_group.deploy.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_windows_virtual_machine" "windows_vm" {
  name                = local.vm_name
  resource_group_name = data.azurerm_resource_group.deploy.name
  location            = data.azurerm_resource_group.deploy.location
  size                = var.size
  admin_username      = var.admin_name
  admin_password      = azurerm_key_vault_secret.example.value
  network_interface_ids = [
    azurerm_network_interface.windows_vm.id,
  ]

  identity {
    type = "SystemAssigned"
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2016-Datacenter"
    version   = "latest"
  }
}

data "azuread_group" "ce02" {
  display_name = "ce02 Project Users"
}

resource "azurerm_role_assignment" "owner" {
  scope                = azurerm_windows_virtual_machine.windows_vm.id
  role_definition_name = "Virtual Machine Contributor"
  principal_id         = data.azuread_group.ce02.object_id
}

resource "azurerm_dev_test_global_vm_shutdown_schedule" "shutdown" {
  virtual_machine_id = azurerm_windows_virtual_machine.windows_vm.id
  location           = data.azurerm_resource_group.deploy.location
  enabled            = true

  daily_recurrence_time = "1745"
  timezone              = "GMT Standard Time"

  notification_settings {
    enabled = false
  }
}

# logging code

data "azurerm_resource_group" "analytics" {
  name = var.analytics_group
}

data "azurerm_log_analytics_workspace" "example" {
  name                = var.analytics_workspace
  resource_group_name = data.azurerm_resource_group.analytics.name
}

data "azurerm_monitor_diagnostic_categories" "vm" {
  resource_id = azurerm_windows_virtual_machine.windows_vm.id
}

resource "azurerm_monitor_diagnostic_setting" "vm" {
  name                       = local.vm_name
  target_resource_id         = azurerm_windows_virtual_machine.windows_vm.id
  log_analytics_workspace_id = data.azurerm_log_analytics_workspace.example.id

  dynamic "metric" {
    iterator = metric_category
    for_each = data.azurerm_monitor_diagnostic_categories.vm.metrics

    content {
      category = metric_category.value
      enabled  = true

      retention_policy {
        enabled = true
        days    = 7
      }
    }
  }
}

data "azurerm_client_config" "current" {}

data "azuread_group" "pod_potato" {
  display_name = "Pod Potato"
}

resource "azurerm_key_vault" "example" {
  name                        = format("kv%s%s%s%03d", var.user, var.application, var.environment, var.vmid)
  location                    = data.azurerm_resource_group.deploy.location
  resource_group_name         = data.azurerm_resource_group.deploy.name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  tags                        = local.default_tags

  sku_name = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azuread_group.pod_potato.object_id


    key_permissions = [
    ]

    secret_permissions = [
      "Get",
      "set",
      "List",
      "delete"
    ]

    storage_permissions = [
    ]
  }

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = "5423515a-d698-44b5-b48c-76937ff377ea"

    key_permissions = [
      "Get",
      "list",
      "delete"
    ]

    secret_permissions = [
      "Get",
      "list",
      "set",
      "delete"
    ]
  }
}
resource "random_string" "random1" {
  length  = var.string_length
  special = false
}

resource "azurerm_key_vault_secret" "example" {
  # for_each = {
  #   secret1 = format("s%s1", random_string.random1.result)
  # }
  name         = "secret1"
  value        = format("s%s1", random_string.random1.result)
  key_vault_id = azurerm_key_vault.example.id
}