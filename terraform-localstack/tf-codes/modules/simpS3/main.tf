resource "aws_s3_bucket" "example" {
  bucket = var.bucket_name
}

output "bucket_arn" {
  value = aws_s3_bucket.example.arn
}
