# Leer el número k y la cadena
k = int(input("Ingresa el número k: "))
cadena = input("Ingresa la cadena: ")

# Verificar si k es un número positivo
if k <= 0:
  print("Error: k debe ser un número positivo")
  exit()

# Dividir la cadena en palabras
palabras = cadena.split()

# Contar cuántas palabras tienen longitud k
contador = 0
for palabra in palabras:
  if len(palabra) == k:
    contador += 1

# Imprimir el resultado
print(f"Hay {contador} palabras con longitud k")

