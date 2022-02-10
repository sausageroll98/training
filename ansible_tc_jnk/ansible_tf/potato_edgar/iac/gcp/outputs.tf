# output "ip" {
#   value = concat(
#     # tolist([module.team_magneton_linux_vm.public_ip]),
#     # module.team_char_linux_vm.*.linux_public_ip[0],
#     # tolist([module.team_ivysaur_linux_vm.public_ip]),
#     #   tolist([module.team_mew_linux_vm.linux_public_ip]),
#     #   tolist([module.team_persian_linux_vm.public_ip])
#   )
# }


output "public_ip_address" {
  value = module.linux_vm[*].ip_address
}