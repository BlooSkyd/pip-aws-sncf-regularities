provider "aws" {
  region = "us-east-1"
}

# --- 1. S3 STORAGE ---
resource "aws_s3_bucket" "data_lake" {
  bucket = "data-source-sncfmc" 
  force_destroy = true # Permet de détruire le bucket même s'il contient des fichiers (utile pour le lab)
}

# --- 2. IAM ---
resource "aws_iam_role" "glue_service_role" {
  name = "AWSGlueServiceRole-TrainProject"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "glue_admin_attachment" {
  role       = aws_iam_role.glue_service_role.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# --- 3. DATA CATALOG ---
resource "aws_glue_catalog_database" "trains_db" {
  name = "trains_db"
}

# --- OUTPUTS ---
output "bucket_name" {
  value = aws_s3_bucket.data_lake.bucket
}