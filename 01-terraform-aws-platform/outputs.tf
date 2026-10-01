output "vpc_id" {
  description = "Platform VPC ID."
  value       = aws_vpc.platform.id
}

output "private_application_subnets" {
  description = "Private application subnet IDs."
  value       = [aws_subnet.private_app_a.id, aws_subnet.private_app_b.id]
}
