from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, json
import sys
import eel

eel.init('_web')
ap1 = 0
@eel.expose
def loginIQ(email, senha):
    API = IQ_Option(email, senha)
    API.connect()

    API.change_balance("PRACTICE") # PRACTICE / REAL

    if API.check_connect():
        global ap1 
        ap1 = API
        saldo = API.get_balance()
        list_API = API, saldo
        return list_API
    else:
        return "Erro ao conectar"
        sys.exit()

@eel.expose        
def capturaSaldo():
    return ap1.get_balance()

@eel.expose 
def mhi2():
    while True:
        minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
        entrar = True if (minutos >= 4.58 and minutos <= 5) or minutos >= 9.58 else False
        print('Hora de entrar?',entrar,'/ Minutos:',minutos)


eel.start('index.html', size=(1100, 600))
