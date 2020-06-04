# Problema contraseña
# ----- Zona de Variables Globales ------#
clave = "posta"

# ----- Zona de Lógica ------#

# Acá le decis, repetime esto desde 0 hasta 3 aumentando de a 1
for i in range(0,3):

    print("intento: ", i)

    # --- Cada vez que entre vas a pedirle la clave
    guachin = input("Mete la clave Guachin: ")

    # --- Verificas si la clave esta bien
    if clave == guachin:  # Con str.lower escribe todo en minusculas
        print("COINCIDE VIEJI: Acceso al correccional")
        break
    else:
        print("NO COINCIDE: Corre Guachin")
