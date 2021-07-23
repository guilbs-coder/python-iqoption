from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time
import sys
        
def startScanVVZ(api, par):
    while True:
        minutes = float(((datetime.now()).strftime('%M.%S'))[1:])
        scan = True if (minutes >= 0.58 and minutes <= 1) or (minutes >= 5.58 and minutes <= 6) else False
        print('Hora de entrar?',scan,'/ Minutos:',minutes)
            
        if scan:
            velas = api.get_candles(par, 60, 4, time.time())
            velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
            velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
            velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'
            velas[3] = 'g' if velas[3]['open'] < velas[3]['close'] else 'r' if velas[3]['open'] > velas[3]['close'] else 'd'
            
            if velas[0] != velas[1] and velas[1] == velas[2] and velas[2] == velas[3]:
                print('The graphic got a HIT')
                print(velas[0], velas[1], velas[2], velas[3])
            else:
                print('It is no a HIT')
                print(velas[0], velas[1], velas[2], velas[3])