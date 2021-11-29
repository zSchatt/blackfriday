from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def filtro_itens():
    i = 1
    while i != 51:
        sleep(1)
        itens = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
        if not 'PATROCINADOS' in itens[i].text.upper():
            if 'APPLE' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'ASUS' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'LG' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'MOTOROLA' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'XIAOMI' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'SMARTPHONE' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            elif 'SAMSUNG' in itens[i].text.upper():
                if '$' in itens[i].text.upper():
                    print('=-==-==-==-==-==-==-==-==-==-==-=')
                    print(itens[i].text)
                    i += 1
                else:
                    i += 1
            else:
                i += 1
        else: i += 1

def troca_pagina(contagem):
    troca_pag = driver.find_elements(By.CSS_SELECTOR, 'li.a-normal')
    troca_pag[contagem].click()
    


option = Options()
option.headless = True
driver = webdriver.Firefox()

url_amazon = 'https://www.amazon.com.br/'
driver.get(url_amazon)
sleep(1)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Celulares' + Keys.ENTER)
sleep(1.5)
driver.find_element(By.CLASS_NAME, 'a-button-inner').click()
driver.find_element(By.ID, 's-result-sort-select_2').click()

for i in range(1, 4):
    filtro_itens()
    troca_pagina(i)

cont = 1
while cont != 2:
    i = 3
    filtro_itens()
    troca_pagina(i)
    cont += 1
