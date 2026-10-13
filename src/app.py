import os
from requests_oauthlib.oauth2_session import OAuth2Session

scope = ['https://www.api.example.com/auth/example.data']

oauth = OAuth2Session(
    'example_client_id',
    redirect_uri='https://callback.example.com/uri',
    scope=scope)

token = oauth.fetch_token(
        'https://api.example.com/o/oauth2/token',
        client_secret='123_Password') # Noncomp
DB_PASSWORD = "admin123"

def esegui(comando):
    return eval(comando)

def leggi(file):
    try:
        f = open(file)
        return f.read()
    except:
        pass

def calcola(a, b, tipo):
    risultato = 0
    if tipo == 1:
        if a > 0:
            if b > 0:
                risultato = a + b
            else:
                risultato = a - b
        else:
            risultato = 0
    elif tipo == 1:
        risultato = a * b
    return a + b
def get_secret():
    secret = "47828a8dd77ee1eb9dde2d5e93cb221ce8c32b37"
    return secret
