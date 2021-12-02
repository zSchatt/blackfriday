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
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[2].click()
        sleep(1)
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)
        # click para especifcar APENAS celulares
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[9].click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.sg-col-inner')
        # function enumerate do for para indexar
        for index, i in enumerate(elements):    
            if index > 2:
                # if para pegar elements dnv
                if index > 3:
                    elements = driver.find_elements(By.CSS_SELECTOR, 'div.sg-col-inner')
                if '$' in elements[index].text:
                    sleep(1)
                    elements[index].click()

                    # pegar infos celular
                    sleep(1)
                    tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                    preco = driver.find_elements(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium')[0].text
                    # regex pra pegar as infos na tabela
                    print(tabela)
                    print(preco)
                    # comando para voltar a página
                    driver.back()

    def motorola(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[4].click()
        sleep(1)
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)
    
    def samsung(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[3].click()
        sleep(1)
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)

    def xiaomi(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.a-section.octopus-pc-category-card-v2-category')[0].click()
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[127].click()
        sleep(1)
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.sg-col-inner')
        # function enumerate do for para indexar
        for index, i in enumerate(elements):    
            if index > 2:
                # if para pegar elements dnv
                if index > 3:
                    elements = driver.find_elements(By.CSS_SELECTOR, 'div.sg-col-inner')
                if 'CARREGADOR' in elements[index].text.upper():
                    pass
                elif 'PELÍCULA' in elements[index].text.upper():
                    pass
                elif 'TEMPERATURA' in elements[index].text.upper():
                    pass
                elif 'KETTLE' in elements[index].text.upper():
                    pass
                elif '$' in elements[index].text:
                    sleep(1)
                    print(elements[index].text)

                    # pegar infos celular
                    sleep(1)
                    tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                    preco = driver.find_elements(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium')[0].text
                    # regex pra pegar as infos na tabela
                    print(tabela)
                    print(preco)
                    # comando para voltar a página
                    driver.back()


    def lg(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[5].click()
        sleep(1)
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)


    match config.marcas:
        case 'todas': apple(driver, url), motorola(driver, url), samsung(driver, url), xiaomi(driver, url), lg(driver, url)
        case 'apple': apple(driver, url)
        case 'motorola': motorola(driver, url)
        case 'samsung': samsung(driver, url)
        case 'xiaomi': xiaomi(driver, url)
        case 'lg': lg(driver, url)

