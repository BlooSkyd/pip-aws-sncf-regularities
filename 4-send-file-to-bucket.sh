#!/bin/bash
echo "Sending file to AWS S3 bucket, taking generally less than a minute..."
aws s3 cp trains_france_clean.parquet s3://data-source-sncfmc/