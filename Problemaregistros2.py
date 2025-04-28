#  Ejercicio práctico con Archivos: Vamos a crear un ejercicio donde gestionemos un archivo de registros de estudiantes con sus notas.
# Objetivo:
# Crear un archivo de texto llamado estudiantes.txt.
# Guardar en él el nombre y las notas de varios estudiantes.
# Luego, leer el archivo para mostrar los datos.


# 1. Crear el archivo de estudiantes y agregar información
with open('estudiantes.txt', 'w') as file:
    file.write("Juan,8,7,9,6\n")
    file.write("Ana,9,10,8,9\n")
    file.write("Carlos,7,7,6,8\n")

# 2. Leer el archivo y mostrar la información
with open('estudiantes.txt', 'r') as file:
    for linea in file:
        # Separar el nombre de las notas
        datos = linea.strip().split(",")
        nombre = datos[0]
        notas = list(map(int, datos[1:]))
        promedio = sum(notas) / len(notas)
        print(f"{nombre} - Promedio: {promedio:.2f}")
