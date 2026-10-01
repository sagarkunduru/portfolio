variable "aws_region" {
  description = "AWS region for the lab."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Prefix used for lab resources."
  type        = string
  default     = "sagar-platform-lab"
}

variable "vpc_cidr" {
  description = "CIDR range for the platform VPC."
  type        = string
  default     = "10.20.0.0/16"
}
