resource "aws_instance" "example" {
  ami           = "ami-12345678" # A mock AMI ID, LocalStack doesn't use this
  instance_type = "t2.micro"

  tags = {
    Name = "LocalStack-EC2"
  }
}

output "instance_id" {
  description = "ID of EC2 instance"
  value = aws_instance.example.id
}


