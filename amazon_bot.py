import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import re
import config
import json

def scrappy_celulares(driver, url):
   
    # função de chamadas de produtos
    
    def apple(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[2].click()
        sleep(1)
        
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        
        # click para especifcar APENAS celulares
        sleep(1)
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
                    preco = driver.find_elements(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium')[0].text
                    nome = driver.find_element(By.ID, 'title').text

                    # regex pra pegar as infos na tabela
                    celular = re.findall(r'(iphone)(?:\s)(\d+?\D|\S+)(?:\s)?(mini|plus|pro|pro max|)', nome, re.I)
                    
                    try:
                        tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                        ram = re.findall('(?:RAM |RAM instalada )(\d+\sGB|\d+)', tabela)
                    except:
                        ram = '0'

                    if 'IPHONE' in celular[0][0].upper():
                        if '5' in celular[0][1]:
                            if '5C' in celular[0][1].upper():
                                # iPhone 5C
                                processador = '1.3 GHz Dual Core'
                                if ram == []:
                                    ram = '1 GB'
                                else:
                                    ram = ram[0]
                            elif '5S' in celular[0][1].upper():
                                # iPhone 5S
                                processador = '1.3 GHz Dual Core'
                                if ram == []:
                                    ram = '1 GB'
                                else:
                                    ram = ram[0]
                            else:
                                # iPhone 5
                                processador = '1.3 GHz Dual Core'
                                if ram == []:
                                    ram = '1 GB'
                                else:
                                    ram = ram[0]
                        if '6' in celular[0][1]:
                            if '6S' in celular[0][1].upper():
                                if 'PLUS' in celular[0][2].upper():
                                    # iPhone 6S Plus
                                    processador = '2 GHz Dual Core'
                                    if ram == []:
                                        ram = '2 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone 6S
                                    processador = '1.8 GHz Dual Core'
                                    if ram == []:
                                        ram = '2 GB'
                                    else:
                                        ram = ram[0]
                            elif '6' in celular[0][1].upper():
                                if 'PLUS' in celular[0][2].upper():
                                    # iPhone 6 Plus
                                    processador = '1.4 GHz Dual Core'
                                    if ram == []:
                                        ram = '1 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone 6
                                    processador = '1.4 GHz Dual Core'
                                    if ram == []:
                                        ram = '1 GB'
                                    else:
                                        ram = ram[0]
                        elif '7' in celular[0][1]:
                            if 'PLUS' in celular[0][2].upper():
                                # iPhone 7 Plus
                                processador = '2.2 GHz Quad Core'
                                if ram == []:
                                    ram = '3 GB'
                                else:
                                    ram = ram[0]
                            else:
                                # iPhone 7
                                processador = '2.2 GHz Quad Core'
                                if ram == []:
                                    ram = '2 GB'
                                else:
                                    ram = ram[0]
                        elif '8' in celular[0][1]:
                            if 'PLUS' in celular[0][2].upper():
                                # iPhone 8 Plus
                                processador = '2x Monsoon + 4x Mistral'
                                if ram == []:
                                    ram = '3 GB'
                                else:
                                    ram = ram[0]
                            else:
                                # iPhone 8
                                processador = '2x Monsoon + 4x Mistral'
                                if ram == []:
                                    ram = '2 GB'
                                else:
                                    ram = ram[0]
                        elif 'X' in celular[0][1].upper():
                            if 'XS' in celular[0][1].upper():
                                if 'MAX' in celular[0][2].upper():
                                    # iPhone XS Max
                                    processador = '2x 2.5 GHz Vortex + 4x1.6 GHz Tempest'
                                    if ram == []:
                                        ram = '4 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone XS
                                    processador = '2x 2.5 GHz Vortex + 4x1.6 GHz Tempest'
                                    if ram == []:
                                        ram = '4 GB'
                                    else:
                                        ram = ram[0]
                            elif 'XR' in celular[0][1].upper():
                                # iPhone XR
                                processador = '2x 2.5 GHz Vortex + 4x1.6 GHz Tempest'
                                if ram == []:
                                    ram = '3 GB'
                                else:
                                    ram = ram[0]
                            else:
                                # iPhone X
                                processador = '2x Monsoon + 4x Mistral'
                                if ram == []:
                                    ram = '3 GB'
                                else:
                                    ram = ram[0]
                        elif '11' in celular[0][1]:
                            if 'PRO' in celular[0][2]:
                                if 'MAX' in celular[0][3]:
                                    # iPhone 11 Pro Max
                                    processador = '2x 2.65 GHz Lightning + 4x 1.8 GHz Thunder'
                                    if ram == []:
                                        ram = '4 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone 11 Pro
                                    processador = '2x 2.65 GHz Lightning + 4x 1.8 GHz Thunder'
                                    if ram == []:
                                        ram = '4 GB'
                                    else:
                                        ram = ram[0]
                            else:
                                # iPhone 11
                                processador = '2x 2.65 GHz Lightning + 4x 1.8 GHz Thunder'
                                if ram == []:
                                    ram = '4 GB'
                                else:
                                    ram = ram[0]
                        elif '12' in celular[0][1]:
                            if 'PRO' in celular[0][2].upper():
                                if 'MAX' in celular[0][3].upper():
                                    # iPhone 12 Pro Max
                                    processador = '2x 3.1 GHz Firestorm + 4x 1.8 GHz Icestorm'
                                    if ram == []:
                                        ram = '6 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone 12 Pro
                                    processador = '2x 3.1 GHz Firestorm + 4x 1.8 GHz Icestorm'
                                    if ram == []:
                                        ram = '6 GB'
                                    else:
                                        ram = ram[0]
                            elif 'MINI' in celular[0][2].upper():
                                # iPhone 12 Mini
                                processador = '2x 3.1 GHz Firestorm + 4x 1.8 GHz Icestorm'
                                if ram == []:
                                    ram = '4 GB'
                                else:
                                    ram = ram[0]
                            else:
                                # iPhone 12
                                processador = '2x 3.1 GHz Firestorm + 4x 1.8 GHz Icestorm'
                                if ram == []:
                                    ram = '4 GB'
                                else:
                                    ram = ram[0]
                        elif '13' in celular[0][1]:
                            if 'PRO' in celular[0][2]:
                                if 'MAX' in celular[0][3]:
                                    # iPhone 13 Pro Max
                                    processador = '2x 3.22 GHz Avalanche + 4x 1.82 GHz Blizzard'
                                    if ram == []:
                                        ram = '6 GB'
                                    else:
                                        ram = ram[0]
                                else:
                                    # iPhone 13 Pro
                                    processador = '2x 3.22 GHz Avalanche + 4x 1.82 GHz Blizzard'
                                    if ram == []:
                                        ram = '6 GB'
                                    else:
                                        ram = ram[0]
                            elif 'MINI' in celular[0][2]:
                                # iPhone 13 Mini
                                processador = '2x 3.22 GHz Avalanche + 4x 1.82 GHz Blizzard'
                                if ram == []:
                                    ram = '4 GB'
                                else:
                                    print(ram[0])
                            else:
                                # iPhone 13
                                processador = '2x 3.22 GHz Avalanche + 4x 1.82 GHz Blizzard'
                                if ram == []:
                                    ram = '4 GB'
                                else:
                                    ram = ram[0]
                        elif 'SE' in celular[0][1].upper():
                            # iPhone SE
                            processador = '2x 2.65 GHz Lightning + 4x 1.8 GHz Thunder'
                            if ram == []:
                                ram = '3 GB'
                            else:
                                ram = ram[0]

                    lista_apple = []
                    arquivo = {
                        "Apple":
                        [
                            {
                            "NOME" : nome,
                            "PRECO" : preco,
                            "RAM" : ram,
                            "PROCESSADOR" : processador
                            }
                        ]
                    }
                    
                    if not os.path.exists(r'C:\Users\JULIANO\Desktop\blackfriday\blackfriday\amazon\amazon_apple.json'):
                        
                        with open(r'C:\Users\JULIANO\Desktop\blackfriday\blackfriday\amazon\amazon_apple.json', 'w') as f:
                            json.dump(arquivo, f, indent=4, separators=(',',': '))
                    
                    else:

                        lista_apple = {
                            "NOME": nome,
                            "PRECO": preco,
                            "RAM": ram,
                            "PROCESSADOR": processador
                        }

                        with open(r'C:\Users\JULIANO\Desktop\blackfriday\blackfriday\amazon\amazon_apple.json', "r+") as f:
                            dados = json.load(f)
                            dados['Apple'].append(lista_apple)
                            f.seek(0)
                            json.dump(dados, f, indent=4, separators=(',',': '))


                    # comando para voltar a página
                    driver.back()


    def motorola(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[4].click()
        
        # clicks para definir order by
        sleep(1)
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)


    def samsung(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[3].click()
        
        # clicks para definir order by
        sleep(1)
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)


    def xiaomi(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.a-section.octopus-pc-category-card-v2-category')[0].click()
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[127].click()
        
        # clicks para definir order by
        sleep(1)
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
                    ...
                    print(tabela)
                    print(preco)
                    
                    # comando para voltar a página
                    driver.back()


    def lg(driver, url):
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[5].click()
        
        # clicks para definir order by
        sleep(1)
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

