# Ejercicio: Imagina que tienes una lista de estudiantes con sus notas, y quieres calcular el promedio de notas de cada uno y almacenar la información en un archivo.

# 1. Crear una lista de estudiantes con sus notas.
# 2. Calcular el promedio de cada estudiante.
# 3. Almacenar los resultados en un archivo.
import pickle

# Crear una lista de registros (estudiantes con sus notas)
estudiantes = [
    {"nombre": "Laura", "notas": [8, 7, 9, 6]},
    {"nombre": "Carlos", "notas": [9, 10, 8, 9]},
    {"nombre": "Sofia", "notas": [7, 7, 6, 8]},
]

# Calcular el promedio de cada estudiante
for estudiante in estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    estudiante["promedio"] = promedio

# Mostrar los resultados
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.2f}")

# Guardar los resultados en un archivo
with open("estudiantes.pkl", "wb") as file:
    pickle.dump(estudiantes, file)


#  ¿De dónde sale estudiante si solo definimos estudiantes?

# estudiantes es la lista completa de todos los estudiantes. Es una lista de diccionarios.

# estudiante es una sola variable que se crea dentro del for para recorrer uno por uno los elementos de estudiantes.

# Mirá este pedacito:
# for estudiante in estudiantes:
# Lo que significa es:

# "Para cada elemento que hay en la lista estudiantes, guardalo momentáneamente en la variable estudiante, y trabajá con él."

# Entonces Python automáticamente va tomando:

# El primer estudiante → lo guarda en estudiante,

# Después el segundo → otra vez en estudiante,

# Y así sucesivamente.