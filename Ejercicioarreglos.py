# Ejercicio práctico: Imagina que tenemos la siguiente matriz de ventas, donde cada fila es un vendedor y cada columna es un producto vendido:
ventas = [
    [20, 35, 50],  # Vendedor 1
    [15, 25, 60],  # Vendedor 2
    [40, 45, 30]   # Vendedor 3
]

# Objetivo: Calcular el total de ventas de cada vendedor y el total de ventas de cada producto.
# Total ventas por vendedor (suma de cada fila)
for i in range(len(ventas)):
    total_vendedor = sum(ventas[i])
    print(f"Total ventas Vendedor {i+1}: ${total_vendedor}")

# Total ventas por producto (suma de cada columna)
for j in range(len(ventas[0])):
    total_producto = sum(ventas[i][j] for i in range(len(ventas)))
    print(f"Total ventas Producto {j+1}: ${total_producto}")
