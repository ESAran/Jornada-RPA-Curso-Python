""" 
Pré instalação:

    Virtual Environment:
        - python install venv venv
        - definir o python interpreter como venv
        - rodar o script de activate do venv

    Instalar bibliotecas:
        - pip install selenium
        - pip install pandas as pd
        - pip install numpy as np
        - pip install openpyxl
"""

# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pandas as pd
import numpy as np

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
 

chrome_options.binary_location = ("C:/Users/eduardo_aran/Documents/Cruso Python/ExerciciosIntro/2modulo/chrome-win64/chrome.exe")
chrome_driver_path = ("C:/Users/eduardo_aran/Documents/Cruso Python/ExerciciosIntro/2modulo/chromedriver-win64/chromedriver.exe")

service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options,service=service_options)
 

site = "http://rpachallenge.com/"
driver.get(site)


# data_frame
arquivo = "challenge.xlsx"
data_frame = pd.read_excel(arquivo, sheet_name=0)

# iniciando rpa challenge
print("\n\ncomeçando RPA Challenge...")
print("-----------------------------------------------")
print(data_frame.head())


botao_start = driver.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')
botao_start.click()

for i, r in data_frame.iterrows():
    role = r["Role in Company"]
    email = r["Email"]
    first_name = r["First Name"]
    last_name = r["Last Name"]
    phone = r["Phone Number"]
    company = r["Company Name"]
    address = r["Address"]

    seletor_email = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelEmail']")
    seletor_email.clear
    seletor_email.send_keys(email)
 
    seletor_companyname = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelCompanyName']")
    seletor_companyname.clear
    seletor_companyname.send_keys(company)

    seletor_firstname = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelFirstName']")
    seletor_firstname
    seletor_firstname.send_keys(first_name)


    seletor_phone = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelPhone']")
    seletor_phone.clear
    seletor_phone.send_keys(phone)


    seletor_address = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelAddress']")
    seletor_address.clear
    seletor_address.send_keys(address)


    seletor_role = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelRole']")
    seletor_role.clear
    seletor_role.send_keys(role)

    seletor_lastname = driver.find_element(By.XPATH,"//input[@ng-reflect-name='labelLastName']")
    seletor_lastname.clear
    seletor_lastname.send_keys(last_name)
    
    seletor_submit = driver.find_element(By.XPATH,'//input[@value="Submit"]')
    seletor_submit.click()


resultado = driver.find_element(By.CLASS_NAME,"message2")
resultado = resultado.text
print("-----------------------------------------------")
print("\nRESULTADO:")
print(resultado)
print("-----------------------------------------------\n")
time.sleep(3)
