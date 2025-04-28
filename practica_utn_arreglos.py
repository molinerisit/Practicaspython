# ========================================
# 🧠 PRÁCTICA CON ARREGLOS (LISTAS) - UTN
# Algoritmos y Estructuras de Datos
# Autor: Julián Molineris
# ========================================

# -----------------------------
# 🔹 1. ARREGLOS UNIDIMENSIONALES
# -----------------------------

# Cargar arreglo
def cargar(v, tam):
    for i in range(tam):
        v[i] = int(input(f"Ingrese valor en posición {i}: "))

# Mostrar arreglo
def mostrar(v, tam):
    for i in range(tam):
        print(f"Posición {i}: {v[i]}")

# Búsqueda secuencial
def buscar(v, tam, elem):
    for i in range(tam):
        if v[i] == elem:
            return i
    return -1

# Ordenamiento burbuja (de menor a mayor)
def ordenar(v, tam):
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

# Búsqueda dicotómica (requiere arreglo ordenado)
def buscar_dicotomico(v, elem):
    inf = 0
    sup = len(v) - 1
    while inf <= sup:
        medio = (inf + sup) // 2
        if v[medio] == elem:
            return medio
        elif elem > v[medio]:
            inf = medio + 1
        else:
            sup = medio - 1
    return -1

# Merge (intercalar dos arreglos ordenados)
def intercalar(v1, v2):
    v3 = []
    i = j = 0
    while i < len(v1) and j < len(v2):
        if v1[i] < v2[j]:
            v3.append(v1[i])
            i += 1
        else:
            v3.append(v2[j])
            j += 1
    while i < len(v1):
        v3.append(v1[i])
        i += 1
    while j < len(v2):
        v3.append(v2[j])
        j += 1
    return v3

# -----------------------------
# 🔹 2. MATRICES BIDIMENSIONALES
# -----------------------------

# Cargar matriz
def cargar_matriz(m, fil, col):
    for i in range(fil):
        for j in range(col):
            m[i][j] = int(input(f"Ingrese valor en [{i},{j}]: "))

# Mostrar matriz
def mostrar_matriz(m, fil, col):
    for i in range(fil):
        for j in range(col):
            print(f"{m[i][j]:4}", end=" ")
        print()

# Ordenar matriz por una columna (de mayor a menor)
def ordenar_matriz_por_columna(m, fil, col, colu):
    for i in range(fil - 1):
        for j in range(i + 1, fil):
            if m[i][colu] < m[j][colu]:
                for k in range(col):
                    m[i][k], m[j][k] = m[j][k], m[i][k]

# Búsqueda secuencial en matriz
def buscar_en_matriz(m, fil, col, elem):
    for i in range(fil):
        for j in range(col):
            if m[i][j] == elem:
                return (i, j)
    return (-1, -1)

# Búsqueda dicotómica en matriz ordenada por la primera columna
def buscar_dico_matriz(m, elem):
    inf = 0
    sup = len(m) - 1
    while inf <= sup:
        medio = (inf + sup) // 2
        if m[medio][0] == elem:
            return medio
        elif elem > m[medio][0]:
            inf = medio + 1
        else:
            sup = medio - 1
    return -1

# -----------------------------
# 🔹 PROGRAMA PRINCIPAL
# -----------------------------
def main():
    print("=== ARREGLOS UNIDIMENSIONALES ===")
    tam = 5
    V = [0] * tam
    cargar(V, tam)
    print("Arreglo cargado:")
    mostrar(V, tam)

    print("\nOrdenando arreglo...")
    ordenar(V, tam)
    mostrar(V, tam)

    x = int(input("\nElemento a buscar (secuencial): "))
    pos = buscar(V, tam, x)
    print(f"Resultado búsqueda secuencial: {pos}")

    print("\nBuscando con búsqueda dicotómica...")
    pos = buscar_dicotomico(V, x)
    print(f"Resultado búsqueda dicotómica: {pos}")

    print("\nEjemplo de merge:")
    V1 = [1, 3, 5]
    V2 = [2, 4, 6, 8]
    V3 = intercalar(V1, V2)
    print("Resultado del merge:", V3)

    print("\n=== MATRICES BIDIMENSIONALES ===")
    FIL, COL = 3, 4
    M = [[0] * COL for _ in range(FIL)]
    cargar_matriz(M, FIL, COL)
    print("Matriz cargada:")
    mostrar_matriz(M, FIL, COL)

    print("\nOrdenando por columna 0 (de mayor a menor)...")
    ordenar_matriz_por_columna(M, FIL, COL, 0)
    mostrar_matriz(M, FIL, COL)

    n = int(input("\nBuscar elemento en matriz: "))
    fila, columna = buscar_en_matriz(M, FIL, COL, n)
    print(f"Resultado búsqueda: fila={fila}, columna={columna}")

    print("\nBúsqueda dicotómica en matriz por columna 0:")
    pos = buscar_dico_matriz(M, n)
    print(f"Resultado búsqueda dicotómica en matriz: fila={pos}")

# Ejecutar
if __name__ == "__main__":
    main()


# 🧪 EJERCICIO 1: Cargar y mostrar un arreglo
# 📌 Pedir al usuario que cargue 5 números enteros en un arreglo y luego mostrar los valores ingresados.

def cargar(V, tam):
    for i in range(tam):
        V[i] = int(input(f"Ingrese el número en la posición {i}: "))

def mostrar(V, tam):
    print("Contenido del arreglo:")
    for i in range(tam):
        print(f"Posición {i}: {V[i]}")

# Programa principal
Tam = 5
V = Tam * [0]
cargar(V, Tam)
mostrar(V, Tam)

# 🧪 EJERCICIO 2: Búsqueda secuencial
# 📌 Dado un arreglo de 10 números enteros, buscar si un valor ingresado por el usuario existe en el arreglo. Indicar su posición o que no fue encontrado.

def buscar(X, e):
    i = 0
    while i < len(X) and X[i] != e:
        i += 1
    return i if i < len(X) else -1

# Programa
V = [4, 8, 15, 16, 23, 42, 10, 3, 7, 12]
nro = int(input("Ingrese número a buscar: "))
pos = buscar(V, nro)

if pos != -1:
    print(f"El número está en la posición {pos}")
else:
    print("El número no fue encontrado")

# 🧪 EJERCICIO 3: Intercalación (MERGE)
# 📌 Dados dos arreglos ordenados, unirlos en uno solo también ordenado.


def intercalar(V1, V2, V3, n, m):
    i = j = k = 0
    while i < n and j < m:
        if V1[i] < V2[j]:
            V3[k] = V1[i]
            i += 1
        else:
            V3[k] = V2[j]
            j += 1
        k += 1
    while i < n:
        V3[k] = V1[i]
        i += 1
        k += 1
    while j < m:
        V3[k] = V2[j]
        j += 1
        k += 1

# Programa
V1 = [2, 4, 6]
V2 = [1, 3, 5, 7]
V3 = [0] * (len(V1) + len(V2))

intercalar(V1, V2, V3, len(V1), len(V2))
print("Arreglo intercalado:", V3)