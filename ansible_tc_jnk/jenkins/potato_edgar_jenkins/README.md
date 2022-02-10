## Azure Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 2.60.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | 2.1.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.1.0 |
| <a name="requirement_template"></a> [template](#requirement\_template) | 2.2.0 |
| <a name="requirement_tls"></a> [tls](#requirement\_tls) | 3.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 2.60.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_add_ansible_user"></a> [add\_ansible\_user](#module\_add\_ansible\_user) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-ubuntu_first_boot | ce02_terraform-kubrick-ubuntu_first_boot_20220104.3|
| <a name="module_linux_vm"></a> [linux\_vm](#module\_linux\_vm) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-azure_ubuntu_vm | ce02_terraform-kubrick-azure_ubuntu_vm_20220104.1 |

## Resources

| Name | Type |
|------|------|
| [azurerm_resource_group.target](https://registry.terraform.io/providers/hashicorp/azurerm/2.60.0/docs/resources/resource_group) | resource |
| [azurerm_client_config.current](https://registry.terraform.io/providers/hashicorp/azurerm/2.60.0/docs/data-sources/client_config) | data source |
| [azurerm_subnet.network](https://registry.terraform.io/providers/hashicorp/azurerm/2.60.0/docs/data-sources/subnet) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_admin_name"></a> [admin\_name](#input\_admin\_name) | Default linux admin name | `string` | n/a | yes |
| <a name="input_ansible_public_key_file"></a> [ansible\_public\_key\_file](#input\_ansible\_public\_key\_file) | Location of the Ansible public key file | `string` | n/a | yes |
| <a name="input_ansible_username"></a> [ansible\_username](#input\_ansible\_username) | Ansible username for config | `string` | `"ansible"` | no |
| <a name="input_application"></a> [application](#input\_application) | Target application | `string` | n/a | yes |
| <a name="input_cohort"></a> [cohort](#input\_cohort) | cohort ID | `number` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | Target Environment | `string` | n/a | yes |
| <a name="input_external_rg"></a> [external\_rg](#input\_external\_rg) | External VNet resource group | `string` | n/a | yes |
| <a name="input_external_subnet_name"></a> [external\_subnet\_name](#input\_external\_subnet\_name) | External Subnet name | `string` | n/a | yes |
| <a name="input_external_vnet"></a> [external\_vnet](#input\_external\_vnet) | External VNet connection | `string` | n/a | yes |
| <a name="input_instance"></a> [instance](#input\_instance) | Instance count for the VMs | `number` | n/a | yes |
| <a name="input_location"></a> [location](#input\_location) | Azure deployment region location | `string` | n/a | yes |
| <a name="input_project"></a> [project](#input\_project) | Project identifier | `string` | n/a | yes |
| <a name="input_public_key_file"></a> [public\_key\_file](#input\_public\_key\_file) | Location of the VM public key file | `string` | n/a | yes |
| <a name="input_random_int"></a> [random\_int](#input\_random\_int) | Length of random integer | `number` | `3` | no |
| <a name="input_region_code"></a> [region\_code](#input\_region\_code) | Three letter region code | `string` | n/a | yes |
| <a name="input_size"></a> [size](#input\_size) | Standard VM size to be used | `string` | `"Standard_B1s"` | no |
| <a name="input_team"></a> [team](#input\_team) | Operation team name | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | Expected user | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_public_ip_address"></a> [public\_ip\_address](#output\_public\_ip\_address) | azure VM public ip addresses |
| <a name="output_resource_group"></a> [resource\_group](#output\_resource\_group) | target resource group |

## AWS Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | 3.70.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | 2.1.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.1.0 |
| <a name="requirement_template"></a> [template](#requirement\_template) | 2.2.0 |
| <a name="requirement_tls"></a> [tls](#requirement\_tls) | 3.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 3.70.0 |
| <a name="provider_local"></a> [local](#provider\_local) | 2.1.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_add_ansible_user"></a> [add\_ansible\_user](#module\_add\_ansible\_user) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-ubuntu_first_boot | ce02_terraform-kubrick-ubuntu_first_boot_20220104.3|
| <a name="module_linux_vm"></a> [linux\_vm](#module\_linux\_vm) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-aws_ubuntu_vm | ce02_terraform-kubrick-aws_ubuntu_vm_20220104.1 |

## Resources

| Name | Type |
|------|------|
| [aws_key_pair.deploy](https://registry.terraform.io/providers/hashicorp/aws/3.70.0/docs/resources/key_pair) | resource |
| [local_file.public_key_file](https://registry.terraform.io/providers/hashicorp/local/2.1.0/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_admin_name"></a> [admin\_name](#input\_admin\_name) | n/a | `string` | n/a | yes |
| <a name="input_ansible_public_key_file"></a> [ansible\_public\_key\_file](#input\_ansible\_public\_key\_file) | n/a | `string` | n/a | yes |
| <a name="input_application"></a> [application](#input\_application) | n/a | `string` | n/a | yes |
| <a name="input_cohort"></a> [cohort](#input\_cohort) | n/a | `number` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | n/a | `string` | n/a | yes |
| <a name="input_external_rg"></a> [external\_rg](#input\_external\_rg) | n/a | `string` | n/a | yes |
| <a name="input_external_subnet_name"></a> [external\_subnet\_name](#input\_external\_subnet\_name) | n/a | `string` | n/a | yes |
| <a name="input_external_vnet"></a> [external\_vnet](#input\_external\_vnet) | n/a | `string` | n/a | yes |
| <a name="input_project"></a> [project](#input\_project) | n/a | `string` | n/a | yes |
| <a name="input_public_key_file"></a> [public\_key\_file](#input\_public\_key\_file) | n/a | `string` | n/a | yes |
| <a name="input_random_int"></a> [random\_int](#input\_random\_int) | n/a | `number` | `3` | no |
| <a name="input_region"></a> [region](#input\_region) | n/a | `string` | `"eu-west-1"` | no |
| <a name="input_region_code"></a> [region\_code](#input\_region\_code) | n/a | `string` | n/a | yes |
| <a name="input_team"></a> [team](#input\_team) | n/a | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | n/a | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_public_ip_address"></a> [public\_ip\_address](#output\_public\_ip\_address) | n/a |

## GCP Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 4.5.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | 2.1.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.1.0 |
| <a name="requirement_template"></a> [template](#requirement\_template) | 2.2.0 |
| <a name="requirement_tls"></a> [tls](#requirement\_tls) | 3.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_local"></a> [local](#provider\_local) | 2.1.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_add_ansible_user"></a> [add\_ansible\_user](#module\_add\_ansible\_user) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-ubuntu_first_boot | ce02_terraform-kubrick-ubuntu_first_boot_20220104.3|
| <a name="module_linux_vm"></a> [linux\_vm](#module\_linux\_vm) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-gcp_ubuntu_vm | ce02_terraform-kubrick-gcp_ubuntu_vm_20220104.1 |

## Resources

| Name | Type |
|------|------|
| [local_file.public_key_file](https://registry.terraform.io/providers/hashicorp/local/2.1.0/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_admin_name"></a> [admin\_name](#input\_admin\_name) | n/a | `string` | n/a | yes |
| <a name="input_ansible_public_key_file"></a> [ansible\_public\_key\_file](#input\_ansible\_public\_key\_file) | n/a | `string` | n/a | yes |
| <a name="input_application"></a> [application](#input\_application) | n/a | `string` | n/a | yes |
| <a name="input_cohort"></a> [cohort](#input\_cohort) | n/a | `number` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | n/a | `string` | n/a | yes |
| <a name="input_external_rg"></a> [external\_rg](#input\_external\_rg) | n/a | `string` | n/a | yes |
| <a name="input_external_subnet_name"></a> [external\_subnet\_name](#input\_external\_subnet\_name) | n/a | `string` | n/a | yes |
| <a name="input_external_vnet"></a> [external\_vnet](#input\_external\_vnet) | n/a | `string` | n/a | yes |
| <a name="input_project"></a> [project](#input\_project) | n/a | `string` | n/a | yes |
| <a name="input_public_key_file"></a> [public\_key\_file](#input\_public\_key\_file) | n/a | `string` | n/a | yes |
| <a name="input_random_int"></a> [random\_int](#input\_random\_int) | n/a | `number` | `3` | no |
| <a name="input_region"></a> [region](#input\_region) | GCP deployment region | `string` | n/a | yes |
| <a name="input_region_code"></a> [region\_code](#input\_region\_code) | n/a | `string` | n/a | yes |
| <a name="input_team"></a> [team](#input\_team) | n/a | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | n/a | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_public_ip_address"></a> [public\_ip\_address](#output\_public\_ip\_address) | n/a |
