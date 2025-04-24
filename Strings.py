# Las strings pueden manejarse de forma indexada donde un indice indica un caracter por ejemplo:
palabra = "algoritmos"
print (palabra [0:4])
#Retorna "algo", toma las primeras 4 letras.
print (palabra [0:-6])
#Retorna "algo", toma primeras 4 letras.
print (palabra [-8:-6]*2)
#Retorna "gogo".

#Operaciones 

mensaje1 = "hola"
mensaje2 = "Julian"

mensaje_completo = mensaje1 + " " + mensaje2
print (mensaje_completo)

mensaje_completo = mensaje1 * 2 + " " + mensaje2
print (mensaje_completo)


