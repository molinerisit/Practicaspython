from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()
print(ahora)  # Muestra algo como: 2025-04-26 12:34:56.789012

# Solo la fecha
print(ahora.date())

# Solo la hora
print(ahora.time())


#Crear fechas específicas

fecha = datetime(2025, 4, 26)  # Año, Mes, Día
print(fecha)


#Operaciones


from datetime import timedelta

# Sumar 5 días
nueva_fecha = ahora + timedelta(days=5)
print(nueva_fecha)

# Restar 3 días
otra_fecha = ahora - timedelta(days=3)
print(otra_fecha)

#Formateo de fechas

print(ahora.strftime("%d/%m/%Y"))  # 26/04/2025
print(ahora.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-04-26 12:34:56
