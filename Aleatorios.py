import random
x = random.random()
print(x)

# Numero aleatorio entero igual o mayor que 2 y menor a 10.


ejemplo = random.randrange(2,10)
print(ejemplo)


# Numero aleatorio mayor o igual que 20 y menor o igual que 100.


ejemplo = random.randint(2,10)
print(ejemplo)



secuencia = 2,3,4,5,6,7,8
secuencia1 = "hola","chau","gracias"

ejemplo1 = random.choice(secuencia)
ejemplo2 = random.choice(secuencia1)
print(ejemplo1, "", ejemplo2)

