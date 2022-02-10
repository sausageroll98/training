output "ip_address" {
  description = "Private IP Address"

  value = azurerm_linux_virtual_machine.linux_vm.*.private_ip_address[0]
}
