output "ip_address" {
  description = "Public IP Address"

  value = azurerm_linux_virtual_machine.linux_vm.*.public_ip_address[0]
}