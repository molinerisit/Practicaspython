# ===============================
# 📘 PRÁCTICA ESTRUCTURAS UTN 2025
# Algoritmos y Estructuras de Datos
# Autor: Julián Molineris
# ===============================

# -----------------------------
# 🔹 1. ENTRADAS Y SALIDAS
# -----------------------------
print("🔹 Entrada y salida de datos")
producto = input("Ingrese nombre del producto: ")
precio = float(input("Ingrese precio del producto: "))
print(f"Producto ingresado: {producto} - Precio: ${precio}\n")

# -----------------------------
# 🔹 2. ESTRUCTURA SECUENCIAL
# -----------------------------
print("🔹 Estructura Secuencial (cálculo simple)")
cantidad = int(input("Ingrese cantidad: "))
total = cantidad * precio
print(f"Total a pagar por {cantidad} unidades de {producto}: ${total}\n")

# -----------------------------
# 🔹 3. ESTRUCTURA DECISORIA
# -----------------------------
print("🔹 Estructura de Decisión Simple / Doble / Múltiple")
if total > 10000:
    print("🔸 El total supera $10.000")
elif total > 5000:
    print("🔸 El total está entre $5.001 y $10.000")
else:
    print("🔸 El total es menor o igual a $5.000\n")

# -----------------------------
# 🔹 4. REPETICIÓN CON WHILE
# -----------------------------
print("🔹 Repetición con WHILE")
numero = int(input("Ingrese un número para cuenta regresiva: "))
while numero > 0:
    print(numero)
    numero -= 1
print("¡Despegue!\n")

# -----------------------------
# 🔹 5. REPETICIÓN CON FOR y RANGE
# -----------------------------
print("🔹 Repetición con FOR + RANGE")
for i in range(1, 6):
    print(f"Producto #{i}")
print("Fin del ciclo FOR\n")

# -----------------------------
# 🔹 6. FUNCIONES DEFINIDAS POR USUARIO
# -----------------------------
def calcular_descuento(tipo_cliente, cantidad, precio_unitario):
    neto = cantidad * precio_unitario
    if tipo_cliente == "L":
        if cantidad <= 24:
            descuento = 0.20
        else:
            descuento = 0.25
    elif tipo_cliente == "P":
        if cantidad < 6:
            descuento = 0.0
        elif 6 <= cantidad <= 18:
            descuento = 0.05
        else:
            descuento = 0.10
    else:
        descuento = 0.0  # tipo no válido
    bonificado = neto - (neto * descuento)
    return bonificado

# -----------------------------
# 🔹 7. FUNCIÓN PRINCIPAL main()
# -----------------------------
def main():
    print("🔹 Ejemplo completo con funciones y lógica completa\n")
    for i in range(1, 4):  # probamos con 3 clientes
        print(f"--- Cliente #{i} ---")
        cli = input("Ingrese tipo de cliente (L=libería / P=particular): ").upper()
        cant = int(input("Ingrese cantidad de libros: "))
        imp = float(input("Ingrese precio unitario: $"))
        resultado = calcular_descuento(cli, cant, imp)
        print(f"💰 Importe bonificado: ${resultado:.2f}\n")

# -----------------------------
# 🔹 EJECUCIÓN DEL PROGRAMA
# -----------------------------
if __name__ == "__main__":
    main()
