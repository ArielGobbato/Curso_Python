# DICCIONARIO
#tiene la forma de ("clave" , "valor") separado por comas ,

diccionario = {} # diccionario vacio,
diccionario = {"azul":"blue" ,"rojo":"red" ,"amarillo":"yelow"}
print (diccionario["azul"]) #muestra solo el valor de la clave pedida

diccionario["amarillo"] = "yelow" #agrega un par (clave,valor) al final
print (diccionario)

diccionario["azul"] = "LAGARTIJA BLUE" #se cambia el valor de una clave
print (diccionario)

del(diccionario["amarillo"]) #se elimina una clave y por ende su valor
print (diccionario)


# se puede definir un diccionario con otro y mostrar lo que necesito
diccionario = {"Papu":{"edad":35,"altura":1.8} , "Mati":[31,1.5] , "Joaqo":[32,1.6]}
print (diccionario["Mati"])


#OTROS DICCIONARIOS
#clave tipo numero : valor tipo cadena (letra)
equipo={10:"Dybala" , 11:"Costa" , 7:"Ronaldo" , 14:"Mandzukic"}
print (equipo[10]) #muestra el valor de la clave seleccionada

print (equipo.get(6, "no existe un jugador con ese dorsal"))
#para que no aparezca error con .get aprarece un mensajito

print (9 in equipo)
# muestra si existe o no este valor (true or false)

print(equipo.keys()) #muestra solo las claves

print(equipo.values()) #muestra solo los valores

print(equipo.items()) #muestra los pares en orden

print(len(equipo)) #con .len muestra la cantidad de pares (clave, valor)

equipo.clear() #con .clear borro el contenido del equipo
print (equipo)






