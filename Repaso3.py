#Ejercicio 6: Dada una lista de (vendedor, importe), mostrar cuánto vendió cada vendedor. 
ventas = [
    ("Ana", 100),
    ("Ana", 200),
    ("Bruno", 150),
    ("Bruno", 50),
    ("Carlos", 300)
]

i = 0
n = len(ventas)

while i < n:
    vendedor_actual = ventas[i][0]
    total_vendedor = 0

    while i < n and ventas[i][0] == vendedor_actual:
        total_vendedor += ventas[i][1]
        i += 1

    print(f"{vendedor_actual} vendió ${total_vendedor}")

#Ejercicio 7: Leer 5 números, almacenarlos en una lista, y mostrar el promedio.

numeros = []

for _ in range(5):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)


