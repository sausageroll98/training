variable "user" {
  description = "Expected user"
  type        = string
}

variable "team" {
  description = "Operation team name"
  type        = string
}

variable "environment" {
  description = "Target Environment"
  type        = string
}

variable "instance" {
  description = "Instance count for the VMs"
  type        = number
}

variable "cohort" {
  description = "cohort ID"
  type        = number
}

variable "region_code" {
  description = "Three letter region code"
  type        = string
}

variable "application" {
  description = "Target application"
  type        = string
}

variable "public_key_file" {
  description = "Location of the VM public key file"
  type        = string
}

variable "ansible_public_key_file" {
  description = "Location of the Ansible public key file"
  type        = string
}

variable "random_int" {
  description = "Length of random integer"
  type        = number
  default     = 3
}



variable "external_vnet" {
  description = "External VNet connection"
  type        = string
}

variable "external_rg" {
  description = "External VNet resource group"
  type        = string
}

variable "external_subnet_name" {
  description = "External Subnet name"
  type        = string
}

variable "project" {
  description = "Project identifier"
  type        = string
}

variable "location" {
  description = "Azure deployment region location"
  type        = string
}

variable "admin_name" {
  description = "Default linux admin name"
  type        = string
}

variable "size" {
  description = "Standard VM size to be used"
  type        = string
  default     = "Standard_B1s"
}

variable "ansible_username" {
  description = "Ansible username for config"
  type        = string
  default     = "ansible"
}

variable "pod" {
  type        = string
  description = "Pod name"
  # default     = "Potato"
}

variable "analytics_workspace" {
  type        = string
  description = "The name of the analytics workspace"
  #default     = "lace02hub"
}