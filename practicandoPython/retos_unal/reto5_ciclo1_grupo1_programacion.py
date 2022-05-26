# Desarrollar una librería llamada “figuritas” 
# con cuatro funciones

#----------------------------------------------------------------------------------------------------------

#1.(vale 1) La función "tipodefigurita":

from unittest import result
import numpy as np

def tipodefigurita(figuras):
    count = np.unique(figuras)
    return(count)
    
#tipodefigurita(['accion','magia','batalla','batalla','batalla','accion','batalla','batalla','batalla'])

#---------------------------------------------------------------------------------------------------------

# 2. (Vale 1) La función "mefaltandeltipodefigurita "  

def mefaltandeltipodefigurita(numFig,tipoFig,figura):
    result = []
    for i in range(len(tipoFig)):
        if i in numFig:
            if tipoFig[i] == figura:
                result.append(i)
    return(result)
        
# mefaltandeltipodefigurita([3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'batalla')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#3. (Vale 1) La función "notengo"

def notengo(list1,list2):
    newList = []
    for i in list1:
        if i not in list2:
            newList.append(i)
    return(newList)

# notengo([3,5,7,10,15,16],[4,10,5,8])

#-----------------------------------------------------------------------------------------------------------------------

# 4. (Vale 1) La función "puedocambiar"

def puedocambiar(susFiguras,misFiguras):
    fig = []
    for i in susFiguras:
        if i in misFiguras:
            fig.append(i)
    cuenta = len(fig)
    return(cuenta)

# puedocambiar([3,5,7,10,15,16],[4,10,5,8])