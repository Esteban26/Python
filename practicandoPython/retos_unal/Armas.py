def proceso(vArm, fArm, varArms):
    contv = 0
    contF = 0
    time = 0
    contArms = len(varArms)

    while time <= contArms:
        if varArms[time] in vArm:
            contv = contv + 1

        if varArms[time] in fArm:
            contF = contF + 1

        if contv == contF:
            print('≈', end='')
        else:
            if contv > contF:
                print('V', end='')
            else:
                if contF > contv:
                    print('F', end='')

        time = time + 1

        if time == contArms:
            break


def Menu():
    vArm = input("")
    fArm = input("")
    varArms = list(input())
    proceso(vArm, fArm, varArms)


Menu()
