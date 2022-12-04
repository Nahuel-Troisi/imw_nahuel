import sys

# Obtenemos la lista de argumentos
n = sys.argv[1:]
max = len(n)
res = 0

# Calculamos la suma total
for i in n:
    res += float(i)

# Mostramos la media en pantalla
media  = res / max
print(media)
