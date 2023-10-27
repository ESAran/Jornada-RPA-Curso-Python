from navigation import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def IniciaChallenge(driver):
    botao_start = driver.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')
    botao_start.click()

def ExecutaChallenge(driver, data_frame):
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