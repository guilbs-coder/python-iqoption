from iqoptionapi.stable_api import IQ_Option

def getBalance(api):
    return api.get_balance()