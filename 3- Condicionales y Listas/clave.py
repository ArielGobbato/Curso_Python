# Problema contraseña
#----- Zona de Variables Globales ------#
clave = "posta"

#----- Zona de Lógica ------#

# Acá le decis, repetime esto desde 0 hasta 3 aumentando en 1 
for i in range(0,3,1) : 

    print("Intento ", i+1)
    #--- Cada vez que entre vas a pedirle la clave
    guachin = input("Mete la clave Guachin: ").lower()

    #--- Verificas si la clave esta bien
    if clave == guachin :
        print("COINCIDE VIEJI: Acceso al correccional")
        break
    else:
        print("NO COINCIDE: Corre Guachin")
