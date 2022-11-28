import sys

def sumcuad(num):
    resultado = 0
    for i in range(1,num+1):
        cal = i ** 2
        resultado += cal
    
    return resultado

try:
    input = int(sys.argv[1])
    if input < 0:
        print("Este valor es negativo")
    else:
        print(sumcuad(input))
except:
    print("Este valor no es un número")
