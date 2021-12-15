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
    driver = webdriver.Firefox(options=option)
    return driver


def upload_s3():
    
    # conectando ao serviço do S3
    client_s3 = boto3.client(
        service_name = 's3',
        region_name = 'us-east-1',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret)
    
    # fazendo upload para o S3
    jsons_amazon = r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon'
    
    for json in enumerate(os.listdir(jsons_amazon)):
        client_s3.upload_file(
            jsons_amazon[json],
            bucket_name,
            json)


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