import sys

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Este valor es negativo")
    else:
        res=1
        for i in range(1,num+1):
            res *= i
            print(f'{i}! = {res}')
except:
    print('Este valor no es un número')