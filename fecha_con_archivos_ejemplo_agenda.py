import os
import pickle
import os.path

from datetime import datetime, timedelta
from datetime import date


class Agenda:
    def __init__(self):
        self.nombre = ""
        self.celu = ""
        self.fechaNac = date.today()


def ordenar():
	global afFechas, alFechas
	alFechas.seek (0, 0)
	auxi = pickle.load(alFechas)
	tamReg = alFechas.tell() 
	tamArch = os.path.getsize(afFechas)
	cantReg = int(tamArch / tamReg)  
	for i in range(0, cantReg-1):
		for j in range (i+1, cantReg):
			alFechas.seek (i*tamReg, 0)
			auxi = pickle.load(alFechas)
			alFechas.seek (j*tamReg, 0)
			auxj = pickle.load(alFechas)
			if (auxi.fechaNac > auxj.fechaNac):
				alFechas.seek (i*tamReg, 0)
				pickle.dump(auxj, alFechas)
				alFechas.seek (j*tamReg, 0)
				pickle.dump(auxi,alFechas)
				alFechas.flush()


def contactosOrdenados():
	global afFechas, alFechas
	os.system("cls")
	print("Lista de Contactos Ordenados por Fecha de Nacimiento")
	print("----------------------------------------------------\n")
	t = os.path.getsize(afFechas)
	if t==0:
		print ("No hay contactos registrados")
	else:
		ordenar()
		alFechas.seek(0, 0)
		while alFechas.tell()<t:
			contacto = pickle.load(alFechas)
			mostrarContacto(contacto)
	input()


def cumpleHoy():
	global afFechas, alFechas, contacto
	fechaHoy = date.today()    # Fecha del sistema en formato aaaa-mm-dd de tipo date
	ah = fechaHoy.year
	mh = fechaHoy.month
	dh = fechaHoy.day
	os.system("cls")
	print("Quien cumple Hoy", str(dh)+'/'+str(mh)+'/'+str(ah), "?")
	print("-----------------------------\n")
	t = os.path.getsize(afFechas)
	alFechas.seek(0, 0)
	while alFechas.tell()<t:
		contacto = pickle.load(alFechas)
		mn = contacto.fechaNac.month
		dn = contacto.fechaNac.day
		if mn==mh and dn==dh:  
			mostrarContacto(contacto)
	input()
	print("\n\nY mañana quien cumple?")
	print("----------------------\n")
	t = os.path.getsize(afFechas)
	alFechas.seek(0, 0)
	fechaHoy = fechaHoy + timedelta(days=1)   #  31/05/2022   01/06/2022
	mh = fechaHoy.month
	dh = fechaHoy.day
	while alFechas.tell()<t:
		contacto = pickle.load(alFechas)
		mn = contacto.fechaNac.month
		dn = contacto.fechaNac.day
		if mn==mh and dn==dh:  
			mostrarContacto(contacto)
	input()


def mostrarContacto(C):
	print("Nombre:", C.nombre.strip())
	print("Celular:", C.celu.strip())
	print("Fecha Nacimiento:", str(C.fechaNac.day) + '/' + str(C.fechaNac.month) + '/' + str(C.fechaNac.year))
	print()


def formatearContacto(C):
	C.nombre = C.nombre.ljust(30, ' ')   
	C.celu = C.celu.ljust(20, ' ') 
	#C.fechaNac no la formatemos porque es fija y de tipo date


def buscarContacto(N):
	global afFechas, alFechas, contacto
	t = os.path.getsize(afFechas)
	alFechas.seek(0, 0)
	encontrado = False
	while alFechas.tell()<t and not encontrado:
		pos = alFechas.tell()
		contacto = pickle.load(alFechas)
		if contacto.nombre.strip() == N:
			encontrado = True
	if encontrado:
		return pos
	else:
		return -1


def altaAgenda():
	global afFechas, alFechas
	contacto = Agenda() 
	os.system("cls")
	print("Nuevo Contacto\n--------------\n")
	t = os.path.getsize(afFechas)
	if t==0:
		print ("No hay contactos registrados")
	else:
		print ("Lista de Contactos")
		print ("------------------")
		alFechas.seek(0, 0)
		while alFechas.tell()<t:
			contacto = pickle.load(alFechas)
			mostrarContacto(contacto)
	nom = input("Ingrese el nombre del nuevo contacto <hasta 30 caracteres> [* para Volver]: ")
	while len(nom)<1 or len(nom)>30:
		nom = input("Incorrecto - Nombre del contacto <hasta 30 caracteres> [* para Volver]: ")
	while nom != "*":
		if buscarContacto(nom) == -1:
			contacto.nombre = nom
			
			contacto.celu = input("Celular <hasta 20 caracteres>: ")
			while len(contacto.celu)<1 or len(contacto.celu)>20:
				contacto.celu = input("Incorrecto - Celular <hasta 20 caracteres>: ")
			
			# Ingresa fecha en formato dd/mm/aaaa y la guradamos como date en formato aaaa-mm-dd
			ok = False
			while not ok:
				try:
					contacto.fechaNac = input("Ingrese fecha de nacimiento (dd/mm/aaaa): ")
					contacto.fechaNac = datetime.strptime(contacto.fechaNac, "%d/%m/%Y").date()
					ok = True
				except:
					print("Fecha inválida")
						
			formatearContacto(contacto)
			pickle.dump(contacto, alFechas)
			alFechas.flush()
			print("Nuevo contacto registrado\n")
		else:
			print("El contacto ya existe\n")
		os.system("pause")
		nom = input("Ingrese el nombre del nuevo contacto [* para Volver]: ")


def mostrarMenu():
	os.system("cls")
	print("AGENDA\n------\n")
	print("1 - Nuevo contacto")
	print("2 - Cumple Hoy")
	print("3 - Lista Contactos Ordenados por Fec. Nac.")
	print("0 - Salir \n\n")


### Programa Principal ###
afFechas = "c:\\ayed\\fechas.dat"  
if not os.path.exists(afFechas):   
	alFechas = open (afFechas, "w+b")   
else:
	alFechas = open (afFechas, "r+b")
opc = -1
while opc != 0:
	mostrarMenu()
	opc = int(input("Ingrese opción [0-3]: "))
	if opc == 1:
		altaAgenda()
	elif opc == 2:
		cumpleHoy()
	elif opc == 3:
		contactosOrdenados()
	else:
		print("\n\nGracias por visitarnos ...\n\n")
alFechas.close()
















