# Ejercicio: Imagina que tenemos un conjunto de datos que contiene las ventas de diferentes vendedores en una tienda. 
# Cada registro tiene un vendedor, el producto vendido, y el monto de la venta. 
# Queremos calcular cuánto vendió cada vendedor y también mostrar el total general de ventas.

# ¿Qué necesitamos hacer?
# - Corte de control para identificar cuando cambia el vendedor.
# - Acumular el total de ventas de cada vendedor.
# - Al final, mostrar cuánto vendió cada vendedor y el total general de ventas.

ventas = [
    ("Ana", "Camiseta", 20),
    ("Ana", "Pantalón", 35),
    ("Bruno", "Zapatos", 50),
    ("Ana", "Gorra", 15),
    ("Bruno", "Camiseta", 25),
    ("Carlos", "Chaqueta", 60),
    ("Ana", "Camiseta", 20),
    ("Carlos", "Pantalón", 40),
]

# Primero ordenamos la lista para agrupar las ventas por vendedor
ventas.sort()

# Inicializamos el índice y el total general
i = 0
n = len(ventas)
total_general = 0

# Empezamos a recorrer las ventas
while i < n:
    vendedor_actual = ventas[i][0]  # Guardamos el vendedor actual
    total_vendedor = 0  # Inicializamos el total para este vendedor

    # Recorremos las ventas de ese vendedor
    while i < n and ventas[i][0] == vendedor_actual:
        total_vendedor += ventas[i][2]  # Acumulamos las ventas
        total_general += ventas[i][2]   # Acumulamos en el total general
        i += 1  # Avanzamos al siguiente registro

    # Mostramos el total de ventas por vendedor
    print(f"{vendedor_actual} vendió ${total_vendedor}")

# Mostramos el total general de ventas
print(f"Total general de ventas: ${total_general}")


# Explicación:

# Primero recorremos la lista de ventas.
# Por cada vendedor, acumulamos las ventas mientras no cambie el vendedor.
# Cuando cambia el vendedor, mostramos las ventas de ese vendedor y continuamos con el siguiente.
# Finalmente, mostramos el total general.
