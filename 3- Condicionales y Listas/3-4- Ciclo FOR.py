# BUCLES, LOOP O CICLO FOR (por)
# número Determinado de ciclos mientras se cumpla una condición

#  variable iteradora "I" o como se llame

for i in [5,2,"Papu",7,"polainas "]:
    # el  iterador i recorre los elementos de la lista entre []
    print(i*2)
    # el print puede modificarse con una funcion

for p in [5, 2, "Papu", 7, "polainas "]:
    # el  iterador i recorre los elementos de la lista entre []
    print(f"Elemento: {p}")
    #con el f"...":{} muestro la lista con una palabra, por ej elemento:



diccionario = {"papu":35 , "josefa": 21 , "albertitere":67}
# los diccionarios tienen el par (clave,valor)
for k in diccionario:
    print(f"{k} ->{diccionario[k]}")
    # se muestra clave (los que está entre "") y valor (los números) por separado al ejecutar el programa

for clave,valor in diccionario.items():
    print(f"{clave} ->{valor}")
    #otra manera de expresar lo anterior


gilada="chupiripitame"
for l in gilada:
    print(F"{l}")
    #da el salto hacia abajo

gilada="chupiripitame"
for l in gilada:
    print(F"{l}",end=" $ ")
    #con el ,end no da el salto y le puedoo agregar cualquiera







