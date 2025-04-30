#Ejercicio 4: Mostrar los números del 1 al 5.

for i in range(1, 6):
    print(i)


#Ejercicio 5: Pedir números hasta que el usuario ingrese un 0. Mostrar la suma de todos los números ingresados.

suma = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número (0 para terminar): "))
    

print("Suma total:", suma)
