from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

option = Options()
option.headless = True
driver = webdriver.Firefox()

url_amazon = 'https://www.amazon.com.br/Eletronicos-e-Tecnologia/b/?ie=UTF8&node=16209062011&ref_=nav_cs_electronics_aa977060142142808a563d1c6c6b2474'
driver.get(url_amazon)
sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'li.a-spacing-micro.apb-browse-refinements-indent-2')[4].click()
#APPLE
driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__column.bxc-grid__column--3-of-12.bxc-grid__column--light')[0].click()
sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[8].click()
sleep(1)
driver.find_element(By.CLASS_NAME, 'a-button-inner').click()
driver.find_element(By.ID, 's-result-sort-select_2').click()
sleep(1)
celulares = driver.find_elements(By.CLASS_NAME, 'sg-col-inner')

for i in range(4, 28):
    sleep(1)
    cel = celulares[i].text
    if '$' in celulares[i].text:
        troca = re.sub('(iphone|Iphone|IPHONE)', 'iPhone', cel)
        pes = re.compile('((?:i|I)(?:Phone|phone|PHONE)(?:\s\d+|\d+\w+))')
        pre = re.compile('((R\$)( ?|\d+)(\d{1,3}|\d{1,3})(.\d{1,3})(\s\d{1,2}|,\d{1,2}))')
        pesquisa = pes.findall(troca)
        preco = pre.findall(troca)
        

    i += 1
    
driver.close()
sleep(5)
driver.get(url_amazon)
sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'li.a-spacing-micro.apb-browse-refinements-indent-2')[4].click()
#SAMSUNG
driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__column.bxc-grid__column--3-of-12.bxc-grid__column--light')[1].click()
sleep(1)
driver.close()
driver.get(url_amazon)
sleep(1)
driver.find_elements(By.CSS_SELECTOR, 'li.a-spacing-micro.apb-browse-refinements-indent-2')[4].click()
driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[7].click()
sleep(1)
driver.find_element(By.CLASS_NAME, 'a-button-inner').click()
driver.find_element(By.ID, 's-result-sort-select_2').click()
sleep(1)
celulares = driver.find_elements(By.CLASS_NAME, 'sg-col-inner')
