'''
    INTERFACE GRÁFICA
    INSTALAR BIBLIOTECA
        + pip install PySimpleGUI

'''

import PySimpleGUI as sg
from challenge import challenge
from fake_data import fake_data

def tela_inicial():
    sg.change_look_and_feel('LightGray4')
                                                            

    tela_layout = [
        [sg.Text('____________________________________________________________')],
        [sg.Text('                                                            ')],
        [sg.Text('                         RPA CHALLENGE    |     BY ESAran   ')],
        [sg.Text('____________________________________________________________')],
        [sg.Text('                                                                  ')],
        [sg.Text('                   COLETAR DADOS DO FAKEDATA         '),sg.Button('executar', key= "select_fake")], 
        [sg.Text('                                                                  ')],
        [sg.Text('                       EXECUTAR CHALLENGE                   '), sg.Button('executar', key = "select_rpa")],
        [sg.Text('                                                            ')],
        [sg.Text('____________________________________________________________')],
        [sg.Text('     arquivo do FakeData será gravado como new_challenge.csv')],
        [sg.Text('                                                            ')],
        [sg.Button('Sair')]
    ]

    tela_inicio = sg.Window('RPA CHALLENGE - ESAran').layout(tela_layout)
    
    while True:
        event, values = tela_inicio.Read()
        if event in ('Sair', sg.WIN_CLOSED):
            break
        elif event == 'select_rpa':
            tela_challenge()
        elif event == 'select_fake':
            fake_data()
    tela_inicio.close()

def tela_challenge():
    sg.change_look_and_feel('LightGray4')
    tela_layout = [
        [sg.Text('Arquivo a ser utilizado: '),
         sg.Input(key='file')],
         [sg.Button('Ok')]
    ]
    tela = sg.Window('RPA Challenge - ESAran').layout(tela_layout)

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSED):
            break
        elif event == 'Ok':
            arquivo = './assets/' + values['file']
            if arquivo == './assets/':
                tela_alert()
            else:
                challenge(arquivo)
    tela.close()


def tela_alert():
    sg.change_look_and_feel('LightGray4')
    tela_layout = [
        [sg.Text('Por favor informe o nome do arquivo')],
        [sg.Button('Ok')]
    ]

    tela = sg.Window("RPA CHALLENGE - ESAran")

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSE) or (event == 'Ok'):
            break
    tela.close()

tela_inicial()