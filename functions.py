from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def create_webdriver():
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    return driver


def upload_s3():
    pass


def treat_string():
    pass


def list_s3():
    pass
