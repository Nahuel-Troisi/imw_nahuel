# Diccionario que asocia cada número con su letra correspondiente
letras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E"}

# Leemos el número del DNI desde la línea de comandos
numero_dni = input("Ingrese el número del DNI: ")

# Calculamos la letra del DNI
letra = letras[int(numero_dni) % 23]

# Concatenamos el número con la letra y mostramos el resultado
print(numero_dni + letra)
