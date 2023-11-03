'''
    bibliotecas
        - PyAutoGui
        - mypy
        - Pillow
        - pandas
        - openpyxl

            '''

from fakturama import Fakturama, FNew

fakturama_path = (r"C:\Program Files\Fakturama2\Fakturama.exe")
archive = (r"assets\fakturama.xlsx")


Fakturama.open(fakturama_path)
FNew.products_spreadsheet(archive)
