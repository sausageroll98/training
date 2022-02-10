output "ip_address" {
  description = "Private IP Address"

  value = azurerm_windows_virtual_machine.windows_vm.*.private_ip_address[0]
}