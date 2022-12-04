import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

# Generamos una secuencia aleatoria de bases de ADN
sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

# Contamos el número de cada tipo de base de ADN en la secuencia
adenine_count = sequence.count("A")
guanine_count = sequence.count("G")
cytosine_count = sequence.count("C")
thymine_count = sequence.count("T")

# Mostramos el resultado por pantalla
print("Adenine: ", adenine_count)
print("Guanine: ", guanine_count)
print("Cytosine: ", cytosine_count)
print("Thymine: ", thymine_count)
