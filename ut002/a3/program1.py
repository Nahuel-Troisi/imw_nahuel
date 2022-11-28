import sys

def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return "No es un número primo"
    
    return "Si es un número primo"
    

try:
    input = int(sys.argv[1])
    if input < 0:
        print("Este valor es negativo")
    else:
        print(primo(input))
except:
    print("Este valor no es un número")