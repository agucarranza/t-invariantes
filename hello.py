#!/usr/bin/env python
import re

# Abro el archivo de Log.
# file = open('/home/agustin/escritorio/prueba.txt')
file = open('/home/agustin/proyectos/pc/python.txt')
stringCompleto = file.read()
file.close()

nuevo = ''

# Reemplazo los saltos de línea porque son problemáticos para las regEx.
stringCompleto = stringCompleto.replace('\n', ',')

# Armo las regExs
primerGrupo = re.compile(r'''(?:

(?: (T1,) (?= (?:T\d(?:\d)?,)*? (T4,) (?:T\d(?:\d)?,)*? )? )  |
(?: (T2,) (?= (?:T\d(?:\d)?,)*? (T5,) (?:T\d(?:\d)?,)*? )? )  |
(?: (T3,) (?= (?:T\d(?:\d)?,)*? (T6,) (?:T\d(?:\d)?,)*? )? )

)''', re.VERBOSE)

segundoGrupo = re.compile(r'''(?:

(?: (T7,) (?= (?:T\d(?:\d)?,)*? (T8,) (?:T\d(?:\d)?,)*? )? )  |
(?: (T9,) (?= (?:T\d(?:\d)?,)*? (T10,) (?:T\d(?:\d)?,)*? (T11,) (?:T\d(?:\d)?,)*? (T12,) (?:T\d(?:\d)?,)*? )? )

)''', re.VERBOSE)

for i in range(1):
    print('ciclo: ' + str(i))

    matches = primerGrupo.search(stringCompleto)

    print('Inicio: ' + stringCompleto)

    if matches:
        for groupNum in range(0, len(matches.groups())):
            groupNum = groupNum + 1
            if matches.group(groupNum) is not None:
                print('Grupo: ' + str(groupNum) + ' ' + 'Sale: ' + matches.group(groupNum))
                nuevo = re.split(matches.group(groupNum), stringCompleto, 1)
                stringCompleto = re.sub(matches.group(groupNum), r"", stringCompleto, 1)
                print(stringCompleto)
                print('Nuevo: ' + nuevo[1])

    print('********************************************************************')
    print(stringCompleto)
    print('********************************************************************')

    stringCompleto = nuevo[1]

    matches = segundoGrupo.search(stringCompleto)

    print('Inicio: ' + stringCompleto)

    if matches:
        for groupNum in range(0, len(matches.groups())):
            groupNum = groupNum + 1
            if matches.group(groupNum) is not None:
                print('Grupo: ' + str(groupNum) + ' ' + 'Sale: ' + matches.group(groupNum))
                nuevo = re.split(matches.group(groupNum), stringCompleto, 1)
                stringCompleto = re.sub(matches.group(groupNum), r"", stringCompleto, 1)
                print(stringCompleto)
                print('Nuevo: ' + nuevo[1])

    print('********************************************************************')
    print(stringCompleto)
    print('********************************************************************')

# una vez que match, borrar las transiciones especificadas, no la fruta del medio.
# después para el segmento de primerGrupo siguiente, hay que buscar a partir de donde estaba la
# ultima transición que borre.
