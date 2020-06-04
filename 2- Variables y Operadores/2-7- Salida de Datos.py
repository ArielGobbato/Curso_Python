# SALIDA DE DATOS POR CONSOLA

nombre = "Ariel"
edad = 35

print("Hola", nombre, "tienes" , edad , "años") # MEZCLA ENTRE VARIABLE TEXTO Y VARIABLE DEFINIDA

print(("hola {} tienes {} años").format(nombre,edad)) # PRIMEROS VARIABLE TEXTO Y ENTRE {} LAS VARIABLES DEFINIDAS QUE DESPUES DEFINO CON FORMAT

print (f"Hola {nombre} tienes {edad} años")  # dentro del print pongo f"" y dentro de las comillas llamo a las variables entre {} mientras escribo