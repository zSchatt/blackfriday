import os

lojas = 'amazon'
marcas = 'motorola'

access_key_s3 = os.getenv('ACESSO')
secret_key = os.getenv('SECRETO')
region = 'us-east-1'
bucket_name = 'amazon.bot'