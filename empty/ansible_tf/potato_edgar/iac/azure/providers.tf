terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.1.0"
    }

    tls = {
      source  = "hashicorp/tls"
      version = "3.1.0"
    }

    template = {
      source  = "hashicorp/template"
      version = "2.2.0"
    }

    azurerm = {
      source  = "hashicorp/azurerm"
      version = "2.60.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.1.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}