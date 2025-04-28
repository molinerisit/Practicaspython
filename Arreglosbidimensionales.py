#  Un arreglo bidimensional es como una tabla o una matriz. Está compuesto por filas y columnas, y es útil cuando necesitamos organizar datos en un formato tabular.

# Definir un arreglo bidimensional
ventas = [
    [20, 35, 50],  # Ventas del primer vendedor
    [15, 25, 60],  # Ventas del segundo vendedor
    [40, 45, 30]   # Ventas del tercer vendedor
]

# Acceder a un elemento en una posición específica (fila, columna)
print(ventas[0][1])  # Muestra 35 (ventas del primer vendedor, segunda venta)
print(ventas[2][2])  # Muestra 30 (ventas del tercer vendedor, tercera venta)



#Ejemplo de recorrido en matriz:

# Sumar las ventas de cada vendedor (fila por fila)
for i in range(len(ventas)):
    total_vendedor = sum(ventas[i])
    print(f"Total ventas vendedor {i+1}: ${total_vendedor}")

#Ejemplo de suma por columnas (total de ventas de cada producto):

# Sumar las ventas de cada producto (columna por columna)
for j in range(len(ventas[0])):
    total_producto = sum(ventas[i][j] for i in range(len(ventas)))
    print(f"Total ventas producto {j+1}: ${total_producto}")
