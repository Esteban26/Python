
def contarArpa():
    nota = input('letras: ') 
    nota = nota.upper()
    nota = nota.split(",")
    cont1 = 1
    cont=[]
    element=[]
    for i in range(0,len(nota),1):
        try:
            if nota[i]== nota[i + 1]: 
                cont1 +=1
            else:
                element.append(nota[i])
                cont.append(str(cont1)) 
                cont1 = 1
        except:
            element.append(nota[-1])
            cont.append(str(1))  
    
    letra=" ".join(element)
    cuenta=" ".join(cont)

    print(letra)
    print(cuenta)


contarArpa()
    # print(letra,end=' ') 
    # print(cuenta,end=' ')
