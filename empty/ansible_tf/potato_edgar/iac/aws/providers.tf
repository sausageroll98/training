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

    aws = {
      source  = "hashicorp/aws"
      version = "3.70.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.1.0"
    }
  }
}


provider "aws" {
  region = var.region
}