import boto3
import os
from functions import bucket_name, access_key, access_secret

# conectando ao serviço do S3
s3 = boto3.client(
    service_name = "s3",
    region_name = "us-east-1",
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret
)

# fazendo upload para o S3
jsons_amazon = r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon'

# fazendo download do S3
s3.download_file(
        bucket_name,
        'amazon_apple.json', 
        jsons_amazon)