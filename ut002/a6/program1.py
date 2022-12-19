import sys

def count_words(sentence):
    # Creamos un diccionario vacío para almacenar las palabras y sus frecuencias
    summary = {}

    # Dividimos la frase en palabras
    words = sentence.split()

    # Contamos las frecuencias de cada palabra
    for word in words:
        if word in summary:
            summary[word] += 1
        else:
            summary[word] = 1

    return summary

# Leemos la frase del usuario
sentence = input("Ingrese una frase: ")

# Llamamos a la función count_words y almacenamos el resultado en una variable
result = count_words(sentence)

# Mostramos el resultado de forma "organizada"
for word, count in result.items():
    print(f"{word}: {count}")

