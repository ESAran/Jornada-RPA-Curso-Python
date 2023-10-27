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
import os
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
 

chrome_options.binary_location = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chrome-win64/chrome.exe")
chrome_driver_path = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chromedriver-win64/chromedriver.exe")

service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options,service=service_options)
 

site = "https://www.fakenamegenerator.com/gen-random-br-br.php"
driver.get(site)

header = ['First Name', 'Last Name', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number']

if os.path.exists('new_challenge.csv'):
    os.remove('new_challenge.csv')

with open('new_challenge.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file, delimiter=";") #usar delimitador
    writer.writerow(header)

print("\n-------------------------------------\n")
print(header)
print("\n-------------------------------------")
for i in range(10):
    # nome
    selector_name = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/h3")
    name = selector_name.text.split()
    first_name = name[0]
    print(first_name)
    last_name = name[-1]
    print(last_name)
    # company
    selector_company = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[17]/dd')
    company = selector_company.text
    print(company)
    # role
    selector_role = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/dl[18]/dd")
    role = selector_role.text
    print(role)
    # address
    selector_address = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div")
    address = selector_address.text.split('\n')
    address = str(address[0]) + ', ' + str(address[1])
    print (address)
    # email
    selector_email = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd')
    email = selector_email.text.split('\n')
    email = str(email[0])
    print (email)
    # phone
    selector_code = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[5]/dd')
    selector_number = driver.find_element(By.XPATH,'//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd')
    phone = "+" + str(selector_code.text) + " " + str(selector_number.text)
    print (phone)
    print("-------------------------------------\n")

    person = [first_name, last_name, company, role, address, email, phone]

    with open('new_challenge.csv', 'a', encoding='UTF8', newline='') as file: # a de append, adicionar e não sobreescrever 
        writer = csv.writer(file, delimiter=";")
        writer.writerow(person)


    selector_generate = driver.find_element(By.XPATH, '//*[@id="genbtn"]')
    selector_generate.click()
