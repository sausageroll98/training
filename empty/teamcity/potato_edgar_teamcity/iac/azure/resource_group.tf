locals {
  azurerm_resource_group_name = format("rg%s%s%s%s%02d", var.user, var.application, var.project, var.environment, var.instance)
}

resource "azurerm_resource_group" "target" {
  name     = local.azurerm_resource_group_name
  location = var.location
  tags     = local.default_tags
}