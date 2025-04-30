# Guardar registros de estudiantes en un archivo: 1. Crear un archivo llamado estudiantes.txt. 2. Guardar los registros de los estudiantes en formato CSV (valores separados por comas).
# 3. Leer el archivo para mostrar los registros.


# 1. Crear un archivo y agregar registros de estudiantes
estudiantes = [
    {'nombre': 'Juan Pérez', 'edad': 20, 'nota_final': 8.5},
    {'nombre': 'Ana López', 'edad': 22, 'nota_final': 9.0},
    {'nombre': 'Carlos Martínez', 'edad': 21, 'nota_final': 7.5}
]

# Guardamos los registros en un archivo CSV
with open('estudiantes.txt', 'w') as file:
    # Escribir los encabezados
    file.write("nombre,edad,nota_final\n")
    for estudiante in estudiantes:
        # Escribir cada registro de estudiante
        file.write(f"{estudiante['nombre']},{estudiante['edad']},{estudiante['nota_final']}\n")

# 2. Leer el archivo y mostrar los registros
with open('estudiantes.txt', 'r') as file:
    # Leer las líneas del archivo
    lineas = file.readlines()
    
    # Mostrar los registros
    for linea in lineas[1:]:  # Omite la primera línea (encabezado)
        datos = linea.strip().split(',')
        nombre = datos[0]
        edad = int(datos[1])
        nota_final = float(datos[2])
        print(f"Nombre: {nombre}, Edad: {edad}, Nota final: {nota_final}")



# Ejemplo usando clases:

class Estudiante:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota final: {self.nota_final}"

# Crear instancias de la clase Estudiante
estudiantes = [
    Estudiante("Juan Pérez", 20, 8.5),
    Estudiante("Ana López", 22, 9.0),
    Estudiante("Carlos Martínez", 21, 7.5)
]

# Mostrar los estudiantes
for estudiante in estudiantes:
    print(estudiante)
