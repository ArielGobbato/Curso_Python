# BUCLES, LOOP O CICLO WHILE WHILE (mientras)
# número indeterminado de ciclos mientras se cumpla una condición

import math

numero = int(input("ingrese su numero"))

while numero<0:
    print("ERROR -> el numero debera ser positivo")
    numero = int(input("ingrese su numero"))

print (f"la raiz cuadrada es:{math.sqrt(numero):.2f}")

                                                # .2f indica la cantidad de decimales a mostrar despues de la coma

# OTRO EJEMPLO

i = 1
while i<=10:
    print (i)
    i += 1







