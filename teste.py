import boto3
import os
from functions import bucket_name, access_key, access_secret

# conectando ao serviço do S3
client_s3 = boto3.client(
    service_name = 's3',
    region_name = 'us-east-1',
    aws_access_key_id=access_key,
    aws_secret_access_key=access_secret)

# fazendo upload para o S3
jsons_amazon = r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon'
marca = 'apple'
print(os.listdir(jsons_amazon))

caminho = os.path.join('amazon')
print(caminho)

for i in enumerate(os.listdir(jsons_amazon)):
    
    match marca:
        case 'apple': arquivo = 'amazon_apple.json'
        case 'motorola': arquivo = 'amazon_motorola.json'
        case 'xiaomi': arquivo = 'amazon_xiaomi.json'
        case 'samsung': arquivo = 'amazon_samsung.json'
    
    match caminho:
        case 'apple': caminho = os.path.join('amazon', 'amazon_apple.json')
        case 'motorola': caminho = os.path.join('amazon', 'amazon_motorola.json')
        case 'xiaomi': caminho = os.path.join('amazon', 'amazon_xiaomi.json')
        case 'samsung': caminho = os.path.join('amazon', 'amazon_samsung.json')

    client_s3.upload_file(
        caminho,
        bucket_name,
        arquivo)