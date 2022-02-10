terraform {
  backend "azurerm" {
  }
}

data "azurerm_client_config" "current" {}


locals {
  cohort = format("ce%02d", var.cohort)

  default_tags = tomap({
    "env"     = var.environment
    "creator" = var.user
    "pod"     = var.pod
    "region"  = var.region_code
    "cohort"  = local.cohort
    "Purpose" = var.application
    "usage"   = "ansible"
    }
  )
}


module "add_ansible_user" {
  source              = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-ubuntu_first_boot?ref=ce02_terraform-kubrick-ubuntu_first_boot_20220104.3"
  user                = var.ansible_username
  ssh_public_key_file = var.ansible_public_key_file
}


module "windows_vm" {
  source              = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-azure_ubuntu_vm_potato_team_city"
  count               = 1
  resource_group_name = azurerm_resource_group.target.name
  subnet_id           = data.azurerm_subnet.network.id
  vmid                = count.index
  public_key_filename = abspath(var.public_key_file)
  custom_data         = module.add_ansible_user.base64encode
  environment         = var.environment
  user                = var.user
  cohort              = var.cohort
  application         = var.application
  admin_name          = var.admin_name
  prefix              = var.environment
  size                = var.size
  pod                 = var.pod
  string_length       = var.string_length
  analytics_group     = var.external_rg
  analytics_workspace = var.analytics_workspace
  depends_on = [
    module.add_ansible_user,
    azurerm_resource_group.target
  ]
}