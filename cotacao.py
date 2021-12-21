from datetime import datetime
import requests
import PySimpleGUI as  sg

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacoes = requisicao.json()

cotacao_USD = cotacoes['USDBRL']['bid']
cotacao_EUR = cotacoes['EURBRL']['bid']
cotacao_BTC = cotacoes['BTCBRL']['bid']

class TelaCotacao:
   
    def __init__(self):

        sg.theme('DarkGrey3')
        
        layout = [
            [sg.Text('USD:', size=(10,0)), sg.Text('', key='dolar')],
            [sg.Text('EUR:', size=(10,0)), sg.Text('', key='euro')],
            [sg.Text('BTC:', size=(10,0)), sg.Text('', key='bitcoin')],
            [sg.Text('DATA:' , size=(10,0)), sg.Text('', key='data')], 
            [sg.Button('Visualizar', size=(30,0))],
            [sg.Button('Salvar Cotação', size=(30,0))]       
        ]

        self.janela = sg.Window('COTAÇÃO DO DIA', layout)

    def Iniciar(self):
       
        while True:
            events, values = self.janela.Read()
            if events == sg.WINDOW_CLOSED:
                break
            
            data = datetime.now()
            dataformat = (data.strftime('%d-%m-%Y %H:%M'))

            self.janela['dolar'].update('R$ '+ cotacao_USD)
            self.janela['euro'].update('R$ '+ cotacao_EUR)
            self.janela['bitcoin'].update('R$ '+ cotacao_BTC)
            self.janela['data'].update(dataformat)

            if events == 'Salvar Cotação':
                with open('cotacao.txt', 'a') as arquivo:
                    arquivo.write(f'DATA: {dataformat} - USD {cotacao_USD} - EUR {cotacao_EUR} - BITCOIN {cotacao_BTC}\n')

tela = TelaCotacao()
tela.Iniciar()
