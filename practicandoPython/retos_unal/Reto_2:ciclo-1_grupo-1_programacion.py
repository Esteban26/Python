#ramdom.choice() --> elige un numero al azar de una lista,tupla etc.

import random

armas = ["+", "Y", ".", "-", "|", "w", "M", "T", "*", "-"]

equipov = []
equipof = []

def elegirarma(equipo):
    while len(equipo) < 6:
        equipov.append(random.choice(armas))
    print(equipov)
# elegirarma(equipov)

def letra():
    letra = random.choice(armas)
    return(letra)






