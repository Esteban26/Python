#ramdom.choice() --> elige un numero al azar de una lista,tupla etc.
from operator import and_
import random
#--------------------------------------------------------------
armas = ["+", "Y", ".", "-", "|", "w", "M", "T", "*", "-"]
#--------------------------------------------------------------
equipov = []
equipof = []
armasElegidas = []
puntos = []
f = 'f'
v = 'v'
iqual = '='
#--------------------------------------------------------------
def elegirArma(equipo):
    while len(equipo) < 5:
        equipo.append(random.choice(armas))
    print(equipo)
#--------------------------------------------------------------
def letra(armasElegidas):
    while len(armasElegidas)<5:
        armasElegidas.append(random.choice(armas))
    print (armasElegidas)
#--------------------------------------------------------------
cont = 0
# elegirArma(equipof)
# elegirArma(equipov)
# letra(armasElegidas)



