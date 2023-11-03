import pyautogui as pg
import pandas as pd
import os
import psutil
from navigation import Desktop, Screen

class Fakturama:
    def open(path):
        for  process in psutil.process_iter(['name']):
            if process.info['name'] == 'Fakturama.exe':
                Desktop.max("Fakturama")
                return print('programa já aberto')
        os.startfile(path)
        Screen.try_locate_image(r'assets\images\btn_new_product.png', tries=120)
        Desktop.max("Fakturama")

class FNew:
    #Botões

    def products_spreadsheet(archive):
        
        data_frame = pd.read_excel(archive)
        print(data_frame.head())

        
        for i, r in data_frame.iterrows():
            # salvando dados
            item_number = str(r["Item Number"])
            name = str(r["Name"])
            category = str(r["Category"])
            gtin = str(r["GTIN"])
            description = str(r["Description"])
            notice = str(r["Notice"])


            # Identifica botão de novo produto
            btn_new_product = Screen.try_locate_image(r'assets\images\btn_new_product.png')
            print(btn_new_product)
            pg.click(btn_new_product, interval=1)

            # Identifica nova aba
            tab_new_product = Screen.try_locate_image(r'assets\images\tab_new_product.png')
            print(tab_new_product)
            pg.click(tab_new_product, interval=1)

            #preenche campos
            pg.press('tab', 2, interval=0.5)
            pg.write(item_number)

            pg.press('tab', 1, interval=0.5)
            pg.write(name)

            pg.press('tab', 1, interval=0.5)
            pg.write(category)

            pg.press('tab', 1, interval=0.5)
            pg.write(gtin)

            pg.press('tab', 2, interval=0.5)
            pg.write(description)

            # salvando e fechando aba
            pg.hotkey('ctrl','s', interval=0.5)
            pg.hotkey('ctrl','w', interval=0.5)
