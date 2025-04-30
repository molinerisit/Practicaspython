# Ejercicio 1: Pedir el nombre y la edad de una persona. Mostrar un mensaje que diga "Hola, [nombre], tenés [edad] años".

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad: "))
print(f"Hola, {nombre}, tenés {edad} años.")


#Ejercicio 2: Leer la edad de una persona y mostrar "Mayor de edad" si tiene 18 años o más.

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor.")


#Ejercicio 3: decir si la edad es par o impar.

if edad % 2 == 0:
    print("Es par")
else:
    print("Es impar")
