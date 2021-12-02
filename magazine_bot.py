from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import re
import config


def scrappy_celulares(driver, url):
    """
    funcao de chamadas de produtos
    """
    def apple(driver, url):
        uri = ''
        driver.get(url+'/'+uri)


    def motorola(driver, url):
        uri = ''
        driver.get(url+'/'+uri)
    
    
    def samsung(driver, url):
        uri = ''
        driver.get(url+'/'+uri)


    def xiaomi(driver, url):
        uri = ''
        driver.get(url+'/'+uri)


    def lg(driver, url):
        uri = ''
        driver.get(url+'/'+uri)


    match config.marcas:
        case 'todas': apple(driver, url), motorola(driver, url), samsung(driver, url), xiaomi(driver, url), lg(driver, url)
        case 'apple': apple(driver, url)
        case 'motorola': motorola(driver, url)
        case 'samsung': samsung(driver, url)
        case 'xiaomi': xiaomi(driver, url)
        case 'lg': lg(driver, url)