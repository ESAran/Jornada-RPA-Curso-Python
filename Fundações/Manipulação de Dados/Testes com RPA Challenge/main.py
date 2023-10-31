from navigation import *
from challenge import *
import time
import pandas as pd

site_challenge = "https://rpachallenge.com"
driver = chromeBrowser(site_challenge)

data_frame = pd.read_excel("challenge.xlsx")

IniciaChallenge(driver)
ExecutaChallenge(driver, data_frame)

