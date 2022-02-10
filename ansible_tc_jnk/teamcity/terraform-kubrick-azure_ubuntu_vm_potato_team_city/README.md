## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | n/a |
| <a name="provider_local"></a> [local](#provider\_local) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [azurerm_dev_test_global_vm_shutdown_schedule.shutdown](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/dev_test_global_vm_shutdown_schedule) | resource |
| [azurerm_linux_virtual_machine.linux_vm](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine) | resource |
| [azurerm_network_interface.linux_vm](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface) | resource |
| [azurerm_public_ip.linux_vm](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/public_ip) | resource |
| [azurerm_resource_group.deploy](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/resource_group) | data source |
| [local_file.pub](https://registry.terraform.io/providers/hashicorp/local/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_admin_name"></a> [admin\_name](#input\_admin\_name) | default VM Admin user | `string` | n/a | yes |
| <a name="input_application"></a> [application](#input\_application) | Target Application | `string` | n/a | yes |
| <a name="input_cohort"></a> [cohort](#input\_cohort) | Cohort ID | `number` | n/a | yes |
| <a name="input_custom_data"></a> [custom\_data](#input\_custom\_data) | custom VM setup commands | `string` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | Target environment | `string` | n/a | yes |
| <a name="input_prefix"></a> [prefix](#input\_prefix) | VM Prefixing | `string` | n/a | yes |
| <a name="input_public_key_filename"></a> [public\_key\_filename](#input\_public\_key\_filename) | filename for SSH public key | `string` | n/a | yes |
| <a name="input_resource_group_name"></a> [resource\_group\_name](#input\_resource\_group\_name) | Target Azure Resource Group | `string` | n/a | yes |
| <a name="input_size"></a> [size](#input\_size) | VM Size | `string` | `"Standard_A1_v2"` | no |
| <a name="input_subnet_id"></a> [subnet\_id](#input\_subnet\_id) | Subnet ID for the VM | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | End User | `string` | n/a | yes |
| <a name="input_vmid"></a> [vmid](#input\_vmid) | Unique identifier for the VM | `number` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ip_address"></a> [ip\_address](#output\_ip\_address) | Public IP Address |
