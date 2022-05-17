#---------------importamos el modulo Json----------------------------------------------

import json

#---creamos el diccionario de laminas con su precio y lo comvertimos a formato Json----

laminasTienda = {"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}
laminasTienda = json.dumps(laminasTienda)
laminasTienda = json.loads(laminasTienda)

#------creamos el input e inicializamos una variable tipo lista-------------------------

listUser = list(input(''))
suma = []


#-------funcion que comprueba que las laminas que quiero entan en el la tienda----------

def laminasQueEstanEnTienda():
    for k in listUser:
        if k in laminasTienda:
            print(k, end=' ')

#-------funcion que suma los precios de las laminas que quiero comprar------------------

def precioLaminasComprar():
    for i in listUser:
        if i in laminasTienda:
            suma.append(laminasTienda[i])
    print(sum(suma))

#---llamado de las funciones que me da las laminas que quiero y estan en la tienda con su precio total---

laminasQueEstanEnTienda()
precioLaminasComprar()
