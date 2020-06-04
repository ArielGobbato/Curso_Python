# LISTAS INSERTAR ELEMENTOS

colores = ["rojo" , "amarillo" , "verde" , "fuxia"]

colores.append("naranja")
# con .append puedo añadir al "final de la lista solamente"
print (colores)

colores = [] #lista vacia

colores.append("naranja")
colores.append("celeste")
# con .append puedo añadir al "final de la lista solamente"
print (colores)


colores = ["rojo" , "amarillo" , "verde" , "fuxia"]
colores.insert(2,"marron")
colores.insert(-1,"marron")
# con .insert se indica la posicion y el color a insertar
print (colores)

