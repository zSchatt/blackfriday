import functions
import config
import amazon_bot
import magazine_bot
import casas_bahia_bot

def amazon(driver):
    """
    chamada do bot da amazon
    """
    url = r'https://www.amazon.com.br'
    amazon_bot.scrappy_celulares(driver, url)


def magazine(driver):
    """
    chamada do bot da magazineluiza
    """
    url = r'https://www.magazineluiza.com.br/'
    magazine_bot.scrappy_celulares(driver, url)


def casas_bahia(driver):
    """
    chamada do bot das casas bahia
    """
    url = r'https://www.casasbahia.com.br/'
    casas_bahia_bot.scrappy_celulares(driver, url)


driver = functions.create_webdriver()

match config.lojas:
    case 'todas': amazon(driver), magazine(driver), casas_bahia(driver)
    case 'amazon': amazon(driver)
    case 'magazineluiza': magazine(driver)
    case 'casasbahia': casas_bahia(driver)