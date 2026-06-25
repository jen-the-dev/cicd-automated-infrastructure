terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type        = string
  default     = "ap-southeast-2"
  description = "AWS region for portfolio infrastructure"
}

resource "aws_ecr_repository" "app" {
  name                 = "portfolio-cicd-app"
  image_tag_mutability = "MUTABLE"
}

resource "aws_ecs_cluster" "portfolio" {
  name = "portfolio-cicd-cluster"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}
