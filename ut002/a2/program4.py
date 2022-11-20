import sys
import math

def diametro(r):
    return f'Diámetro: {int(2*r)}'

def circurferecia(r):
    return f'Perímetro: {2 * math.pi * r}'
    
def circulo(r):
    return f'Área: {math.pi * r**2}'
    

try:
    radio = float(sys.argv[1])

    opcion = 0

    while True:

        print("(1) Calcular el diámetro de la circunferencia:")
        print("(2) Calcular el perímetro de la circunferencia:")
        print("(3) Calcular el área del círculo:")
        print("(4) Salir")

        opcion = int(input("Elige la opcion: "))
        if opcion == 1:
            print(diametro(radio))
            continue
        elif opcion == 2:
            print(circurferecia(radio))
            continue
        elif opcion == 3:
            print(circulo(radio))
            continue
        elif opcion == 4:
            print('Saliendo...')
            break
        else:
            print("Error: Opción no válida")

except:
    print("Argumento no válido")

