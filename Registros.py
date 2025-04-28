 #Un registro es una estructura de datos que puede almacenar diferentes tipos de datos (enteros, cadenas, flotantes, etc.) bajo un mismo nombre, pero en diferentes campos o componentes.
#Ejemplo de registro con diccionario:

persona = {
    "nombre": "Juana",
    "edad": 30,
    "ciudad": "Buenos Aires"
}

# Acceder a los campos del registro
print(persona["nombre"])  # Muestra "Juan"
print(persona["edad"])    # Muestra 30
print(persona["ciudad"])  # Muestra "Buenos Aires"


#Un arreglo de registros es una estructura de datos que almacena múltiples registros, formando una lista de registros.

personas = [
    {"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"},
    {"nombre": "Ana", "edad": 25, "ciudad": "Córdoba"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Rosario"}
]

# Acceder a los registros en el arreglo
print(personas[0]["nombre"])  # Muestra "Juan"
print(personas[1]["ciudad"])  # Muestra "Córdoba"

# Ejemplo de filtrado: Filtrar las personas que viven en Buenos Aires
buenos_aires = [persona for persona in personas if persona["ciudad"] == "Buenos Aires"]
print(buenos_aires)

# Ejemplo de modificación de un registro: Modificar la edad de Juan
personas[0]["edad"] = 31
print(personas[0]["edad"])  # Muestra 31

