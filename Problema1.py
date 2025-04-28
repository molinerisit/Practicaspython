# Ejercicio 1 - Alta y listado simple
# Enunciado: Crear un programa que permita:
# Cargar contactos (nombre, celular, fecha de nacimiento). Los debe guardar en un archivo.
# Listar todos los contactos almacenados.

import pickle
import os
from datetime import datetime, date

class Agenda:
    def __init__(self):
        self.nombre = ""
        self.celu = ""
        self.fechaNac = date.today()

def alta_contacto(archivo):
    contacto = Agenda()
    contacto.nombre = input("Nombre: ")
    contacto.celu = input("Celular: ")
    
    ok = False
    while not ok:
        try:
            fecha = input("Fecha nacimiento (dd/mm/aaaa): ")
            contacto.fechaNac = datetime.strptime(fecha, "%d/%m/%Y").date()
            ok = True
        except:
            print("Fecha inválida")
    
    pickle.dump(contacto, archivo)
    archivo.flush()
    print("Contacto guardado.\n")

def mostrar_contactos(archivo):
    archivo.seek(0)
    try:
        while True:
            contacto = pickle.load(archivo)
            print(f"Nombre: {contacto.nombre} - Celular: {contacto.celu} - Nacimiento: {contacto.fechaNac}")
    except EOFError:
        pass

# Programa principal
nombre_archivo = "agenda.dat"
if not os.path.exists(nombre_archivo):
    archivo = open(nombre_archivo, "w+b")
else:
    archivo = open(nombre_archivo, "r+b")

while True:
    print("\n1. Alta de contacto\n2. Mostrar contactos\n0. Salir")
    op = int(input("Opción: "))
    if op == 1:
        alta_contacto(archivo)
    elif op == 2:
        mostrar_contactos(archivo)
    elif op == 0:
        break

archivo.close()
