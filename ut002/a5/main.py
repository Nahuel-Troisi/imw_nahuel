import sys

# En la función num_vowels, se ha creado una cadena 
# vowels con las vocales en minúsculas y mayúsculas. 
# Luego, se recorre el texto y se cuenta el número de veces que aparece cada vocal.

def num_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for c in text:
        if c in vowels:
            count += 1
    return count

# En la función num_whitespaces, se ha utilizado el método count de las cadenas para contar 
# el número de espacios en blanco.

def num_whitespaces(text):
    return text.count(" ")

# En la función num_digits, se recorre el texto y se utiliza el método isdigit de las cadenas 
# para comprobar si cada carácter es un dígito. Si lo es, se incrementa el contador.

def num_digits(text):
    count = 0
    for c in text:
        if c.isdigit():
            count += 1
    return count

# En la función num_words, se ha utilizado el método split de las cadenas para dividir 
# el texto en palabras y luego se ha utilizado la función len para contar el número de palabras.

def num_words(text):
    return len(text.split())

# En la función reverse, se ha utilizado la indexación de Python para obtener una subcadena del texto 
# que va desde el final hasta el principio.

def reverse(text):
    return text[::-1]

#En la función length, se ha utilizado la función len para obtener la longitud del texto.

def length(text):
    return len(text)

# En la función halfs, se ha utilizado la división entera para calcular el índice del carácter 
# central del texto y luego se ha utilizado la indexación para obtener las dos mitades del texto.

def halfs(text):
    half = len(text) // 2
    return text[:half] + " | " + text[half:]

# En la función upper_vowels, se ha creado una nueva cadena vacía y se ha recorrido el texto 
# carácter a carácter. Si el carácter es una vocal, se añade a la nueva cadena en 
# mayúsculas, y si no lo es, se añade tal cual.

def upper_vowels(text):
    vowels = "aeiouAEIOU"
    new_text = ""
    for c in text:
        if c in vowels:
            new_text += c.upper()
        else:
            new_text += c
    return new_text

# En la función sorted_by_words, se ha utilizado el método split para dividir el texto en palabras y luego se ha utilizado 
# el método sort de las listas para ordenar las palabras alfabéticamente. Finalmente, se ha utilizado el método join de las 
# cadenas para unir las palabras en una cadena.

def sorted_by_words(text):
    words = text.split()
    words.sort()
    return " ".join(words)

# En la función length_of_words, se ha utilizado el método split para dividir el texto en palabras y luego se ha utilizado la 
# función len para calcular la longitud de cada palabra. Se ha guardado cada longitud en una lista y finalmente se ha utilizado 
# el método join de las cadenas para unir las longitudes en una cadena.

def length_of_words(text):
    lengths = []
    words = text.split()
    for w in words:
        lengths.append(str(len(w)))
    return " ".join(lengths)

if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
