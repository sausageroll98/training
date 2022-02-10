output "resource_group" {
  description = "target resource group"
  value       = azurerm_resource_group.target.name
}
output "private_ip_address" {
  description = "azure VM private ip addresses"
  value       = module.linux_vm[*].ip_address
}
