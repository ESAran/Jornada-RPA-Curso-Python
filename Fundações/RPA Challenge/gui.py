'''
    INTERFACE GRÁFICA
    INSTALAR BIBLIOTECA
        + pip install PySimpleGUI

'''

import PySimpleGUI as sg
from challenge import challenge, resultado_challenge
from fake_data import fake_data

def tela_inicial():
    sg.change_look_and_feel('LightGray4')

    text1 =[
        [sg.Text('____________________________________________________________', background_color='seashell2')],
        [sg.Text('                                                            ', background_color='seashell2')],
        [sg.Text('RPA CHALLENGE    |    BY ESAran', font='Helvitca 14 italic bold', background_color='seashell2')],
        [sg.Text('____________________________________________________________', background_color='seashell2')]
    ]                                                    
    text2 = [
        [sg.Text('',)],
        [sg.Text('               COLETAR DADOS DO FAKEDATA       ', font='Helvitca 12',),sg.Button('executar', key= "select_fake")], 
        [sg.Text('                                                                  ',)],
        [sg.Text('               EXECUTAR CHALLENGE                        ', font='Helvitca 12'), sg.Button('executar', key = "select_rpa" )],
        [sg.Text('')],
    ]
    text3 = [
        [sg.Text('____________________________________________________________', background_color='seashell2')],
        [sg.Text('arquivo do FakeData será gravado como new_challenge.csv', font='Helvitca 8 italic', background_color='seashell2')],
        [sg.Button('Sair')]
    ]

    tela_layout = [
        [sg.Column(text1, size=(450, 120),element_justification='c', background_color='seashell2')],
        [sg.Column(text2, size=(450, 145))],
        [sg.Column(text3, size=(450, 88), background_color='seashell2')]
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
                tela.close()
                resultado = challenge(arquivo)
                tela_result(resultado)



def tela_alert():
    sg.change_look_and_feel('LightGray4')
    tela_layout_alert = [
        [sg.Text('Por favor informe o nome do arquivo')],
        [sg.Button('Ok')]
    ]

    tela = sg.Window("Aviso").layout(tela_layout_alert)

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSED) or (event == 'Ok'):
        
            break
    tela.close()

def tela_result(resultado):

    sg.change_look_and_feel('LightGray4')
    text = [
        [sg.Text('_____________________________________________________________')],
        [sg.Text('')],
        [sg.Text('CHALLENGE CONCLUÍDO COM SUCESSO', font='Helvitca 12')], 
        [sg.Text(resultado,  font='Helvitca 10 bold')],
        [sg.Text('____________________________________________________________')]]
    tela_layout_resultado = [
        [sg.Column(text, element_justification='c', size=(450, 140),)],
        [sg.Button('Ok')]
    ]

    tela = sg.Window("Resultado").layout(tela_layout_resultado)

    while True:
        event, values = tela.Read()
        if event in (None, sg.WIN_CLOSED) or (event == 'Ok'):
            break
    tela.close()


tela_inicial()
