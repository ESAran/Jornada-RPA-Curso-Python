""" 
Pré instalação:

    Virtual Environment:
        - python install venv venv
        - definir o python interpreter como venv
        - rodar o script de activate do venv

    Instalar bibliotecas:
        - pip install selenium
        - pip install pandas as pd
"""

# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
 
 # definição de caminhos dos drivres e opções de serviços
chrome_options.binary_location = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chrome-win64/chrome.exe")
chrome_driver_path = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chromedriver-win64/chromedriver.exe")
#chrome_options.binary_location = ("chrome-win64\chrome.exe")
#chrome_driver_path = ("chromedriver-win64\chromedriver.exe")
service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
 
driver = webdriver.Chrome(options=chrome_options,service=service_options)
 
site = "http://rpachallenge.com/"

driver.get(site)

# exemplo de seletor Selenium para elementos web

# selector = driver.find_element(By.ID, "vivBer") # seletor por IP

# endereço
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]')
selector.send_keys("Rua Gralha Azul, 45")
# empresa
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]')
selector.send_keys("Sicredi Vale Litoral SC")
#cargo
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelRole"]')
selector.send_keys("Assistente de Processos")
# telefone
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelPhone"]')
selector.send_keys("47 996265490")
# email
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelEmail"]')
selector.send_keys("duarans03@gmail.com")
# primeiro nome
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]')
selector.send_keys("Eduardo")
# sobrenome
selector = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]')
selector.send_keys("Arán")

selector = driver.find_element(By.XPATH, '//input[@value="Submit"]')
selector.click()

selector = driver.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')
selector.click()

time.sleep(60)
