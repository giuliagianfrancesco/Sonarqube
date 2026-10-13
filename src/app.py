import os

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
