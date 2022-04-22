# Pedir a un usuario un numero y determinar si es primo o no es primo

number = int(input("escribe un numero: "))
    
div = number % 2

if div == 0:
    print(f'{number} es un numero primo')
else:
    print(f'{number} no es un numero primo')
