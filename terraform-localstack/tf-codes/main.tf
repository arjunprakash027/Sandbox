module "simpS3" {
  source = "./modules/simpS3"
  # # Pass variables as needed
  bucket_name = "value1"
  # var2 = "value2"
}

module "simpEC2" {
  source = "./modules/simpEC2"
}

output "test_output" {
  value = "Hello, Terraform!"
}