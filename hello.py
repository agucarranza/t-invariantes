#!/usr/bin/env python
import re

# Abro el archivo de Log.
file = open('/home/agustin/proyectos/pc/python.txt')
tInvariantes = file.read()
file.close()

# Reemplazo los saltos de línea porque son problemáticos para las regEx.
tInvariantes = tInvariantes.replace('\n', ',')

# Armo las regExs
unInvarianteCualquiera = re.compile(r'T2,|T5,|T7,|T8,|T13,|T15,')
otroInvarianteCualquiera = re.compile(r'T1,|T4,|T7,|T8,|T13,|T15,')

# Muestro los valores
print(list(dict.fromkeys(unInvarianteCualquiera.findall(tInvariantes))))    # sale ordenado.
print(list(dict.fromkeys(otroInvarianteCualquiera.findall(tInvariantes))))  # sale desordenado.

# Saco un invariante

# print(unInvarianteCualquiera.findall(tInvariantes))
print(unInvarianteCualquiera.sub('', tInvariantes))

