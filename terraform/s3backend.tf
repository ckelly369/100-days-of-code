resource "aws_s3_bucket" "backend_bucket" {
  bucket = "ckelly-terraform-state"
  
  tags = {
    Name = "S3 bucket for state file"
  }
}

resource "aws_s3_bucket_acl" "backend_bucket_acl" {
  bucket = aws_s3_bucket.backend_bucket.id
  acl = "private"
}

resource "aws_s3_bucket_versioning" "backend_bucket_versioning" {
  bucket = aws_s3_bucket.backend_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "backend_bucket_encryption" {
  bucket = aws_s3_bucket.backend_bucket.id
  rule {
    apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "backend_bucket_block" {
  bucket = aws_s3_bucket.backend_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
