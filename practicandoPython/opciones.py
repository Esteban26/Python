opcion = int(input("""
1. digitar cedula
2. digitar nombre
3. digitar año de nacimiento
digite el numero de la opcion que quiera: """))

if opcion == 1:
    cedula = input("1.escribe tu cedula: ")
    print("tu cedula es: " + cedula)
elif opcion == 2:
    nombre = input("1.escribe tu nombre: ") 
    print ("Hola " + nombre)
elif opcion == 3:
    nacimiento = int(input("3.escribe tu año de nacimiento: "))
    edad = 2022 - nacimiento
    print(f'tu edad es {edad}')
else:
    print("Elige una opcion correcta :(")