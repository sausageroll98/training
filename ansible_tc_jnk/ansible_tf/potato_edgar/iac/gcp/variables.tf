variable "user" {
  type = string
}

variable "team" {
  type = string
}

variable "environment" {

  type = string
}

variable "cohort" {

  type = number
}

variable "region_code" {
  type = string
}

variable "application" {

  type = string
}

variable "public_key_file" {
  type = string
}

variable "ansible_public_key_file" {
  type = string
}

variable "random_int" {
  type    = number
  default = 3
}


variable "external_vnet" {
  type = string
}

variable "external_rg" {
  type = string
}

variable "external_subnet_name" {
  type = string
}

variable "project" {
  type = string
}

variable "admin_name" {
  type = string
}

variable "region" {
  description = "GCP deployment region"
  type        = string
}

variable "ansible_username" {
  description = "Ansible username for config"
  type        = string
  default     = "ansible"
}