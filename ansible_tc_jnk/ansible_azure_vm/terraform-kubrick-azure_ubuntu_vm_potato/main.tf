locals {
  local_users_group_name = format("ce%02d Project Users", var.cohort)
  instance               = format("%03d", var.vmid)
  vm_name                = format("vm%saz%s", var.user, local.instance)
  nic_name               = format("nic-%s", local.vm_name)
  public_ip_name         = format("pub-%s", local.vm_name)

  default_tags = tomap({
    "env"      = var.environment
    "pod"      = var.pod
    "creator"  = var.user
    "region"   = data.azurerm_resource_group.deploy.location
    "cohort"   = format("ce%02d", var.cohort)
    "Purpose"  = var.application,
    "usage"    = "ubuntu",
    "platform" = "azure",
    "OS"       = "Linux"
    }
  )
}

data "azurerm_resource_group" "deploy" {
  name = var.resource_group_name
}

data "local_file" "pub" {
  filename = var.public_key_filename
}

resource "azurerm_public_ip" "linux_vm" {
  name                = local.public_ip_name
  location            = data.azurerm_resource_group.deploy.location
  resource_group_name = data.azurerm_resource_group.deploy.name
  allocation_method   = "Static"
}

resource "azurerm_network_interface" "linux_vm" {
  name                = local.nic_name
  location            = data.azurerm_resource_group.deploy.location
  resource_group_name = data.azurerm_resource_group.deploy.name

  ip_configuration {
    name                          = "public"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.linux_vm.id
  }
}

resource "azurerm_linux_virtual_machine" "linux_vm" {
  name                = local.vm_name
  location            = data.azurerm_resource_group.deploy.location
  resource_group_name = data.azurerm_resource_group.deploy.name
  size                = var.size
  admin_username      = var.admin_name
  network_interface_ids = [
    azurerm_network_interface.linux_vm.id,
  ]

  admin_ssh_key {
    username   = var.admin_name
    public_key = (data.local_file.pub.content)
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-focal"
    sku       = "20_04-lts"
    version   = "latest"
  }

  custom_data = var.custom_data
}

resource "azurerm_dev_test_global_vm_shutdown_schedule" "shutdown" {
  virtual_machine_id = azurerm_linux_virtual_machine.linux_vm.id
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

data "azuread_group" "aad_users" {
  display_name = local.local_users_group_name
}

resource "azurerm_role_assignment" "data_owner" {
  scope                = azurerm_linux_virtual_machine.linux_vm.id
  role_definition_name = "Linux VM Data Owner"
  principal_id         = data.azuread_group.aad_users.object_id

  depends_on = [
    azurerm_linux_virtual_machine.linux_vm
  ]
}

data "azurerm_subscription" "current" {}

resource "azurerm_linux_virtual_machine" "management_host" {
  name = "management-vm"

  # ...

  identity = {
    type = "SystemAssigned"
  }
}

data "azurerm_monitor_diagnostic_categories" "vm" {
  resource_id = azurerm_linux_virtual_machine.linux_vm.id
}

resource "azurerm_monitor_diagnostic_setting" "vm" {
  name                       = local.vm_name
  target_resource_id         = azurerm_linux_virtual_machine.linux_vm.id
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