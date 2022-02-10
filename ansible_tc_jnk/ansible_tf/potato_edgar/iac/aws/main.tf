terraform {
  backend "s3" {
  }
}


locals {
  cohort = format("ce%02d", var.cohort)
  default_tags = tomap({
    "env"     = var.environment
    "user"    = var.user
    "region"  = var.region
    "cohort"  = local.cohort
    "Purpose" = var.application
    "usage"   = "ansible"
    }
  )

  key_name = format("key%s%s%s%03d", var.user, local.cohort, var.environment, var.vmid)
}

data "local_file" "public_key_file" {
  filename = var.public_key_file
}

resource "aws_key_pair" "deploy" {
  key_name   = local.key_name
  public_key = data.local_file.public_key_file.content
}


module "add_ansible_user" {
  source              = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-ubuntu_first_boot?ref=ce02_terraform-kubrick-ubuntu_first_boot_20220104.3"
  user                = var.ansible_username
  ssh_public_key_file = var.ansible_public_key_file
}


module "linux_vm" {
  source           = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/terraform-kubrick-aws_ubuntu_vm_potato"
  count            = 1
  vmid             = count.index
  key_name         = aws_key_pair.deploy.key_name
  admin_name       = var.admin_name
  user_data_base64 = module.add_ansible_user.base64encode
  environment      = var.environment
  user             = var.ansible_username
  cohort           = var.cohort
  application      = var.application
  prefix           = var.environment
  region           = var.region
  depends_on = [
    module.add_ansible_user
  ]
}