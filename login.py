print("login mamalon")

#/*
# * EJERCICIO:
# * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
# *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
# *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
# *   que representen todos los tipos de estructuras de control que existan
# *   en tu lenguaje:
# *   Condicionales, iterativas, excepciones...
# * - Debes hacer print por consola del resultado de todos los ejemplos.

# ====== >> Operadores aritméticos << ======
# suma (+)
suma = 3 + 4
print(suma) # result: 7

# resta (-)
resta = 3 - 4
print(resta) # result: -1

# multiplicacion (*)
mult = 3 * 4
print(mult) # result: 12

# división (/)
division = 3 / 4
print(division) # result: 0.75

# división interna (//)
division_interna = 3 // 4
print(division_interna) # result: 0

# módulo (%)
modulo = 3 % 4
print(modulo) # result: 3

# exponenciación (**)
expo = 3 ** 4
print(expo) # result: 81

# ====== >> Operadores de comparación << ======
# igual (==)
comp1 = 3 == 4
print(comp1) # result: False

# diferente (!=)
comp2 = 3 != 4
print(comp2) # result: True

# más grande que (>)
comp3 = 3 > 4
print(comp3) # result: False

# mayor o igual (>=)
comp3 = 3 >= 4
print(comp3) # result: False

# menos que (<)
comp4 = 3 < 4
print(comp4) # result: True

# menos o igual (<=)
comp4 = 3 <= 4
print(comp4) # result: True

# ====== >> Operadores lógicos << ======
# and (and)
comp_log1 = 3 == 4 and "rojo" == "rojo"
print(comp_log1) # result: False

# or (or)
comp_log2 = 3 == 4 or "rojo" == "rojo"
print(comp_log2) # result: True

# not (not)
comp_log3 = not (3 == 4 or "rojo" == "rojo")
print(comp_log3) # result: False

# ====== >> Operadores de asignación << ======
# = 	x = 1
a, b, c, d, e, f = 10, 10, 10, 10, 10, 10
print(a) # result: 10
# +=	x = x + 1
b += 2
print(b) # result: 12
# -=	x = x - 1
c -= 3
print(c) # result: 7
# *=	x = x * 1
d *= 4
print(d) # result: 40
# /=	x = x / 1
e /= 5
print(e) # result: 2.0
# %=	x = x % 1
f %= 6
print(f) # result: 4
