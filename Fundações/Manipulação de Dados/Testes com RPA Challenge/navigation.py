from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def chromeBrowser(site):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    

    chrome_options.binary_location = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chrome-win64/chrome.exe")
    chrome_driver_path = ("C:/Users/eduardo_aran/OneDrive - Sicredi/Documents/Cruso Python/ExerciciosIntro/2modulo/chromedriver-win64/chromedriver.exe")

    service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(options=chrome_options,service=service_options)
    driver.get(site)

    return (driver)
