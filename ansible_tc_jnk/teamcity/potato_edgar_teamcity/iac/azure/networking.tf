
data "azurerm_subnet" "network" {
  name                 = var.external_subnet_name
  virtual_network_name = var.external_vnet
  resource_group_name  = var.external_rg
}
