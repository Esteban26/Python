def run():
#calcular las etapas 

    pesoChavo = int(input("escribe el peso del Chavo: "))
    pesoQuico = (pesoChavo * 2) + 4
    pesoÑoño = int((pesoChavo + pesoQuico) / 5)

    print(pesoChavo, pesoQuico, pesoÑoño)

    if pesoÑoño <= 20:
        print("uno")
    elif pesoÑoño >= 21 and pesoÑoño <= 31:
        print("dos")
    elif pesoÑoño >= 31 and pesoÑoño < 80:
        print("tres")
    else:
        print("cuatro")

if __name__ == '__main__':
    run()

