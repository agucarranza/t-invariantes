#!/usr/bin/env python
import re

# Abro el archivo de Log
# file = open('ruta del archivo en windows')
file = open('/home/agustin/proyectos/pc/lala.txt')
tInvariantes = file.read()
file.close()
tInvariantes = tInvariantes.replace('\n', ',')
print(tInvariantes)

# Trozos de t-Invariantes
A1 = ("T1", "T4")
A2 = ("T2", "T5")
A3 = ("T3", "T6")
B1 = ("T7", "T8")
B2 = ("T9", "T10", "T11", "T12")
C1 = ("T13", "T15")
C2 = ("T14", "T17")

# Elegir el camino de entrada
regEx = re.compile(r'T\d')
mo = regEx.search(tInvariantes)
print(mo.group())

if mo.group() == 'T1':
    print('t2')
elif mo.group() == 'T2':
    print('t2')
elif mo.group() == 'T3':
    print('t3')
else:
    print('no cumple los t-Invariantes')


# while not tInvariantes == '':

# Falta el cartel

# Función buscar

def buscar():
    return False
