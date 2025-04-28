# Ejercicio 3 - Buscar un contacto
# Enunciado: Agregar opción para buscar un contacto por nombre y mostrar su información modificando el codigo del problema 2.


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

def cumple_mes_actual(archivo):
    archivo.seek(0)
    mes_actual = date.today().month
    print(f"Cumpleaños del mes {mes_actual}:")
    hay = False
    try:
        while True:
            contacto = pickle.load(archivo)
            if contacto.fechaNac.month == mes_actual:
                print(f"Nombre: {contacto.nombre} - Fecha: {contacto.fechaNac.day}/{contacto.fechaNac.month}")
                hay = True
    except EOFError:
        if not hay:
            print("No hay cumpleaños este mes.")

def buscar_contacto(archivo, nombre_buscar):
    archivo.seek(0)
    encontrado = False
    try:
        while True:
            contacto = pickle.load(archivo)
            if contacto.nombre.strip().lower() == nombre_buscar.strip().lower():
                print(f"Encontrado: {contacto.nombre} - Celular: {contacto.celu} - Nacimiento: {contacto.fechaNac}")
                encontrado = True
                break
    except EOFError:
        if not encontrado:
            print("Contacto no encontrado.")



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
    print("\n1. Alta de contacto\n2. Mostrar contactos\n3. Cumpleaños este mes\n4. Buscar contacto\n0. Salir")
    op = int(input("Opción: "))
    if op == 1:
        alta_contacto(archivo)
    elif op == 2:
        mostrar_contactos(archivo)
    elif op == 3:
        cumple_mes_actual(archivo)
    elif op == 4:
        nombre = input("Nombre a buscar: ")
        buscar_contacto(archivo, nombre)

    elif op == 0:
        break

archivo.close()
