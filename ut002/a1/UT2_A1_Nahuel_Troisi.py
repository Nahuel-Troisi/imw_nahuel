# Nahuel Ivan Troisi
import sys
try:
    num = int(sys.argv[1])
    resto = 0

    if num == 0:
        print('No hay dinero')
    if num < 0:
        print(f'Debes: {num*-1}€')
    if num >= 50:
        result = num // 50
        resto = num % 50
        if result == 1:
            print(result, ' billete de 50€')
        else:
            print(result, ' billetes de 50€')
    if resto >= 20: 
        result = resto // 20
        resto = num % 20
        if result == 1:
            print(result,' billete de 20€')
        else:
            print(result,' billetes de 20€')
    elif num < 50 and num >= 20: 
        result = num // 20
        resto = num % 20
        if result == 1:
            print(result,' billete de 20€')
        else:
            print(result,' billetes de 20€')
    if resto >= 10:
        result = resto // 10
        resto = num % 10
        if result == 1:
            print(result,' billete de 10€')
        else:
            print(result,' billetes de 10€')
    elif num < 20 and num >= 10:
        result = num // 10
        resto = num % 10
        if result == 1:
            print(result,' billete de 10€')
        else:
            print(result,' billetes de 10€')
    if resto >= 2:
        result = resto // 2
        resto = num % 2
        if result == 1:
            print(result,' moneda de 2€')
        else:
            print(result,' monedas de 2€')        
    elif num < 10 and num >= 2:
        result = num // 2
        resto = num % 2
        if result == 1:
            print(result,' moneda de 2€')
        else:
            print(result,' monedas de 2€')  
    if resto >= 1:
        result = resto // 1
        resto = num % 1
        if result == 1:
            print(result,' moneda de 1€')
        else:
            print(result,' monedas de 1€')  
    elif num < 2 and num >= 1:
        result = num // 1
        resto = num % 1
        if result == 1:
            print(result,' moneda de 1€')
        else:
            print(result,' monedas de 1€')  

except:
    print('Eso no es número')















