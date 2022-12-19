import sys

def menu(phone_book):
  # Mostramos el menú con las opciones disponibles
  print("1. Mostrar lista de contactos")
  print("2. Añadir contacto")
  print("3. Borrar contacto")
  print("4. Salir")
  
  # Pedimos al usuario que elija una opción
  choice = int(input("Elija una opción: "))
  
  # Dependiendo de la opción elegida, llamamos a la función correspondiente
  if choice == 1:
    # Mostramos la lista de contactos
    show_contacts(phone_book)
  elif choice == 2:
    # Pedimos al usuario que introduzca el nombre y el teléfono del nuevo contacto
    name = input("Introduzca el nombre del nuevo contacto: ")
    phone = input("Introduzca el teléfono del nuevo contacto: ")
    
    # Añadimos el contacto a la agenda
    add_contact(phone_book, name, phone)
  elif choice == 3:
    # Pedimos al usuario que introduzca el nombre del contacto a borrar
    name = input("Introduzca el nombre del contacto a borrar: ")
    
    # Borramos el contacto de la agenda
    remove_contact(phone_book, name)
  else:
    # Salimos del programa
    return

def show_contacts(phone_book):
  # Recorremos el diccionario y mostramos los nombres y teléfonos de cada contacto
  for name, phone in phone_book.items():
    print(f"{name}: {phone}")

def add_contact(phone_book, name, phone):
  # Si el nombre ya existe, mostramos un error
  if name in phone_book:
    print("Error: ya existe un contacto con ese nombre")
  # Si el nombre no existe, añadimos el contacto a la agenda
  else:
    phone_book[name] = phone

def remove_contact(phone_book, name):
  # Si el nombre no existe, mostramos un error
  if name not in phone_book:
    print("Error: no existe un contacto con ese nombre")
  # Si el nombre existe, borramos el contacto de la agenda
  else:
    del phone_book[name]

phone_book = {
  "Alicia": "645617432",
  "Manuel": "691854321",
  "Pepe": "676298911",
  "Zeben": "699812345"
}

menu(phone_book)
