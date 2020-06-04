#Problema: AÑO BISIESTO

# DATOS DE ENTRADA
print("Ingrese el año:")
anio=int(input())

# PROCESAMIENTO DATOS
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("SI es Biciesto") # DATOS DE SALIDA
else:
    print("NO es Biciesto") # DATOS DE SALIDA