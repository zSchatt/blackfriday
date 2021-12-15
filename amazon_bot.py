from selenium.webdriver.common.by import By
from time import sleep
import config
import functions
import json
import re
import os

def scrappy_celulares(driver, url):
    
    """
    funcao de chamadas de produtos
    """

    def apple(driver, url):
        
        def pesquisa_itens(elements):
            for index, i in enumerate(elements):

                #pegar elements dnv
                sleep(1.5)
                elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
                sleep(1.5)
                    
                if not '$' in elements[index].text:
                    
                    pass

                elif '$' in elements[index].text:
                    
                    sleep(1.5)
                    elements[index].click()

                    try:
                        
                        # pegar infos celular
                        sleep(1)
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        nome = driver.find_element(By.ID, 'title').text
                        tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                        ram = re.findall('(?:RAM |RAM instalada )(\d+\sGB|\d+)', tabela)

                        # regex pra pegar as infos na tabela
                        celular = re.findall(r'(iphone)(?:\s)(\d+?\D|\S+)(?:\s)?(mini|plus|pro|pro max|\w+|)', nome, re.I)

                    except IndexError:
                        
                        # pegar infos celular
                        sleep(1)
                        nome = driver.find_element(By.ID, 'title').text
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        ram = []

                        # regex pra pegar as infos na tabela
                        celular = re.findall(r'(iphone)(?:\s)(\d+?\D|\S+)(?:\s)?(mini|plus|pro|pro max|\w+|)', nome, re.I)

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
                        elif '6' in celular[0][1]:
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
                        elif '6S' in celular[0][2].upper():
                            processador = '1.8 GHz Dual Core'
                            if ram == []:
                                ram = '2 GB'
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
                    
                    if not os.path.exists(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_apple.json'):
                        
                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_apple.json', 'w') as f:
                            json.dump(arquivo, f, indent=4, separators=(',',': '))
                    
                    else:

                        lista_apple = {
                            "NOME": nome,
                            "PRECO": preco,
                            "RAM": ram,
                            "PROCESSADOR": processador
                        }

                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_apple.json', "r+") as f:
                            dados = json.load(f)
                            dados['Apple'].append(lista_apple)
                            f.seek(0)
                            json.dump(dados, f, indent=4, separators=(',',': '))

                    # comando para voltar a página
                    driver.back()
    
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        sleep(1)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[3].click()
        sleep(1)

        
        # clicks para definir order by
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)

        # click para especifcar APENAS celulares
        sleep(1)
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[9].click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
        
        # function enumerate do for para indexar
        pesquisa_itens(elements)

        # for para trocar as paginas do site
        for i in range(0, 9):
            sleep(1.5)
            num = driver.find_element(By.CSS_SELECTOR, 'li.a-last')
            num.click()
            sleep(1.5)
            elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
            pesquisa_itens(elements)
        
        # function para baixar do s3
        functions.download_s3('amazon_apple.json')





    # APPLE PRONTO.






    def motorola(driver, url):
        
        def pesquisa_itens(elements):
            for index, i in enumerate(elements):
                
                # pegar elements dnv
                sleep(1.5)
                elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
                sleep(1.5)

                if not '$' in elements[index].text:
                    
                    pass

                elif '$' in elements[index].text:
                    
                    sleep(2)
                    elements[index].click()

                    try:
                        
                        # pegar infos celular
                        sleep(1)
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        nome = driver.find_element(By.ID, 'title').text
                        tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                        ram = re.findall('(?:RAM |RAM instalada )(\d+\sGB|\d+)', tabela)

                    except IndexError:
                        
                        # pegar infos celular
                        sleep(1)
                        nome = driver.find_element(By.ID, 'title').text
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        ram == []
                    
                    if ram == []:
                        ram = "NAO IDENTIFICADO"
                    else:
                        ram = ram[0]

                    lista_motorola = []
                    arquivo = {
                        "Motorola":
                        [
                            {
                            "NOME" : nome,
                            "PRECO" : preco,
                            "RAM" : ram
                            }
                        ]
                    }
                    
                    if not os.path.exists(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_motorola.json'):
                        
                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_motorola.json', 'w') as f:
                            json.dump(arquivo, f, indent=4, separators=(',',': '))
                    
                    else:

                        lista_motorola = {
                            "NOME": nome,
                            "PRECO": preco,
                            "RAM": ram,
                        }

                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_motorola.json', "r+") as f:
                            dados = json.load(f)
                            dados['Motorola'].append(lista_motorola)
                            f.seek(0)
                            json.dump(dados, f, indent=4, separators=(',',': '))
                    
                    # comando para voltar a página
                    driver.back()

        uri = 's?bbn=16243890011&rh=n%3A16209062011%2Cn%3A!16209063011%2Cn%3A16243803011%2Cn%3A16243890011%2Cp_89%3Amotorola&ref=megamenu_ce_teste_1_2_1_5'
        driver.get(url+'/'+uri)
        sleep(1)

        # clicks para definir order by
        sleep(1)
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)

        # click para especifcar APENAS celulares
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[9].click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
        
        # function enumerate do for para indexar
        pesquisa_itens(elements)

        # for para trocar as paginas do site
        for i in range(0, 3):
            sleep(1)
            num = driver.find_element(By.CSS_SELECTOR, 'li.a-last')
            num.click()
            sleep(1)
            elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
            sleep(1)
            pesquisa_itens(elements)

        # function para baixar do s3
        functions.download_s3('amazon_motorola.json')





    # MOTOROLA PRONTO






    def samsung(driver, url):
        
        def pesquisa_itens(elements):
            for index, i in enumerate(elements):

                # pegar elements dnv
                elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
                
                if 'MICRO SDHC' in elements[index].text.upper():
                   
                    pass
                
                elif 'EVO' in elements[index].text.upper():
                    
                    pass

                elif 'TAB' in elements[index].text.upper():

                    pass

                elif 'TABLET' in elements[index].text.upper():

                    pass

                elif 'CHROMEBOOK' in elements[index].text.upper():

                    pass

                elif 'NOTEBOOK' in elements[index].text.upper():

                    pass

                elif '$' in elements[index].text:
                    
                    sleep(2)
                    elements[index].click()

                    try:
                        
                        # pegar infos celular
                        sleep(1)
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        nome = driver.find_element(By.ID, 'title').text
                        tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                        ram = re.findall('(?:RAM |RAM instalada )(\d+\sGB|\d+)', tabela)

                    except IndexError:
                        
                        # pegar infos celular
                        sleep(1)
                        nome = driver.find_element(By.ID, 'title').text
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        ram == []
                    
                    if ram == []:
                        ram = "NAO IDENTIFICADO"
                    else:
                        ram = ram[0]

                    lista_samsung = []
                    arquivo = {
                        "Samsung":
                        [
                            {
                            "NOME" : nome,
                            "PRECO" : preco,
                            "RAM" : ram,
                            }
                        ]
                    }
                    
                    if not os.path.exists(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_samsung.json'):
                        
                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_samsung.json', 'w') as f:
                            json.dump(arquivo, f, indent=4, separators=(',',': '))
                    
                    else:

                        lista_samsung = {
                            "NOME": nome,
                            "PRECO": preco,
                            "RAM": ram,
                        }

                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_samsung.json', "r+") as f:
                            dados = json.load(f)
                            dados['Samsung'].append(lista_samsung)
                            f.seek(0)
                            json.dump(dados, f, indent=4, separators=(',',': '))
                    
                    # comando para voltar a página
                    driver.back()
        
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        driver.find_elements(By.CSS_SELECTOR, 'div.bxc-grid__image.bxc-grid__image--light')[3].click()

        # clicks para definir order by
        sleep(1)
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        sleep(1)

        # click para especifcar APENAS celulares
        driver.find_elements(By.CSS_SELECTOR, 'span.a-size-base.a-color-base')[9].click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')

        pesquisa_itens(elements)

        # for para trocar as paginas do site
        for i in range(0, 10):
            sleep(1)
            num = driver.find_element(By.CSS_SELECTOR, 'li.a-last')
            num.click()
            sleep(1)
            elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
            pesquisa_itens(elements)

        # function para baixar do s3
        functions.download_s3('amazon_samsung.json')        





    # SAMSUNG PRONTO






    def xiaomi(driver, url):
        
        def pesquisa_itens(elements):
            for index, i in enumerate(elements):    
                
                # pegar elements dnv
                elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
                
                if 'CABEÇA' in elements[index].text.upper():
                    

                    pass

                elif 'CARREGADOR' in elements[index].text.upper():
                
                    pass
                
                elif 'PELÍCULA' in elements[index].text.upper():
                
                    pass
                
                elif 'TEMPERATURA' in elements[index].text.upper():
                
                    pass
                
                elif 'KETTLE' in elements[index].text.upper():
                
                    pass
                
                elif 'PURIFICADOR' in elements[index].text.upper():

                    pass

                elif '$' in elements[index].text:
                    
                    sleep(1)
                    elements[index].click()
                    
                    try:
                        
                        # pegar infos celular
                        sleep(1)
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        nome = driver.find_element(By.ID, 'title').text
                        tabela = driver.find_elements(By.CSS_SELECTOR, 'div.a-expander-content.a-expander-section-content.a-section-expander-inner')[20].text
                        ram = re.findall('(?:RAM |RAM instalada )(\d+\sGB|\d+)', tabela)

                    except IndexError:
                        
                        # pegar infos celular
                        sleep(1)
                        nome = driver.find_element(By.ID, 'title').text
                        preco = driver.find_element(By.CSS_SELECTOR, 'span.a-price.a-text-price.a-size-medium.apexPriceToPay').text
                        ram == []
                    
                    if ram == []:
                        ram = "NAO IDENTIFICADO"
                    else:
                        ram = ram[0]

                    lista_xiaomi = []
                    arquivo = {
                        "Xiaomi":
                        [
                            {
                            "NOME" : nome,
                            "PRECO" : preco,
                            "RAM" : ram,
                            }
                        ]
                    }
                    
                    if not os.path.exists(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_xiaomi.json'):
                        
                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_xiaomi.json', 'w') as f:
                            json.dump(arquivo, f, indent=4, separators=(',',': '))
                    
                    else:

                        lista_xiaomi = {
                            "NOME": nome,
                            "PRECO": preco,
                            "RAM": ram,
                        }

                        with open(r'C:\Users\User\Desktop\novo projeto\blackfriday\amazon\amazon_xiaomi.json', "r+") as f:
                            dados = json.load(f)
                            dados['Xiaomi'].append(lista_xiaomi)
                            f.seek(0)
                            json.dump(dados, f, indent=4, separators=(',',': '))
                    
                    # comando para voltar a página
                    driver.back()
                
        uri = 'Celulares-Comunicacao/b/?ie=UTF8&node=16243803011&ref_=sv_megamenu_ce_teste_3'
        driver.get(url+'/'+uri)
        sleep(1)
        driver.find_elements(By.CSS_SELECTOR, 'div.a-section.octopus-pc-category-card-v2-category')[0].click()
        sleep(1)
        driver.find_elements(By.CSS_SELECTOR, 'div.a-checkbox.a-checkbox-fancy.aok-float-left.apb-browse-refinements-checkbox')[36].click()
        sleep(1)
        
        # clicks para definir order by
        sleep(1)
        driver.find_element(By.ID, 'a-autoid-0-announce').click()
        driver.find_element(By.ID, 's-result-sort-select_1').click()
        elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')

        
        # function para pegar os produtos
        pesquisa_itens(elements)
        
        # for para trocar as paginas do site
        for i in range(0, 18):
            sleep(1)
            num = driver.find_element(By.CSS_SELECTOR, 'li.a-last')
            num.click()
            sleep(1)
            elements = driver.find_elements(By.CSS_SELECTOR, 'div.a-section.a-spacing-medium')
            pesquisa_itens(elements)

        # function para baixar do s3
        functions.download_s3('amazon_xiaomi.json')





    # XIAOMI PRONTO






    match config.marcas:
        case 'todas': apple(driver, url), motorola(driver, url), samsung(driver, url), xiaomi(driver, url)
        case 'apple': apple(driver, url)
        case 'motorola': motorola(driver, url)
        case 'samsung': samsung(driver, url)
        case 'xiaomi': xiaomi(driver, url)