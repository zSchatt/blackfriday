from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import config
import boto3
import os

access_key = config.access_key_s3
access_secret = config.secret_key
bucket_name = config.bucket_name

def create_webdriver():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox()#options=option)
    return driver


def upload_s3(marca, caminho):
    
    # conectando ao serviço do S3
    client_s3 = boto3.client(
        service_name = 's3',
        region_name = 'us-east-1',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret)
    
    # fazendo upload para o S3
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


def download_s3(amazon):
    
    # conectando ao serviço do S3
    client_s3 = boto3.client(
        service_name = 's3',
        region_name = 'us-east-1',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret)

    # fazendo download do S3
    jsons_amazon = r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon'
    client_s3.download_file(
        bucket_name,
        amazon, 
        jsons_amazon)