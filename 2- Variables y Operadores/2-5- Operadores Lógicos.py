# Operadores lógicos BOOLEANOS
# BOOLEANOS
# and "Y" (multipliación lógica)
# or "O" (suma lógica)
# not (negador cambia los operadores anteriores)
# PRIORIDAD
# 1 NOT
# 2 AND
# 3 OR

a = 10
b= 12
c= 13
d = 10

resultado = ((a>b)or(a<c))and((a==c)or(a>=b))

print(resultado)

a = 10
b= 12
c= 13
d = 10

resultado = ((a>=b)or(a<c))or((a==c)or(a>=b))

print(resultado)