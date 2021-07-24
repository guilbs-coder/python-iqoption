from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, json
import sys
import eel
from getBalance import getBalance

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
        saldo = getBalance(ap1)
        list_API = API, saldo
        return list_API
    else:
        return "Erro ao conectar"
        sys.exit()

eel.start('index.html', size=(1100, 600))
