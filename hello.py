#!/usr/bin/env python
import re

# Abro el archivo de Log.
file = open('/home/agustin/proyectos/pc/python2.txt')
stringCompleto = file.read()
file.close()

# Reemplazo los saltos de línea porque son problemáticos para las regEx.
stringCompleto = stringCompleto.replace('\n', ',')

# Armo las regExs
invariante = re.compile(
    r'(?:(?:(?:(T1,)(?:T\d(?:\d)?,)*?(T4,)(?:T\d(?:\d)?,)*?)|(?:(T2,)(?:T\d(?:\d)?,)*?(T5,)(?:T\d(?:\d)?,)*?)|(?:(T3,'
    r')(?:T\d(?:\d)?,)*?(T6,)(?:T\d(?:\d)?,)*?))(?:(?:(T7,)(?:T\d(?:\d)?,)*?(T8,)(?:T\d(?:\d)?,)*?)|(?:(T9,'
    r')(?:T\d(?:\d)?,)*?(T10,)(?:T\d(?:\d)?,)*?(T11,)(?:T\d(?:\d)?,)*?(T12,)(?:T\d(?:\d)?,)*?))(?:(?:(T13,'
    r')(?:T\d(?:\d)?,)*?(T15,))|(?:(T14,)(?:T\d(?:\d)?,)*?(T16,))))', re.VERBOSE)

matches = invariante.search(stringCompleto)

print(stringCompleto)

if matches:
    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1
        if matches.group(groupNum) is not None:
            print('Grupo: ' + str(groupNum) + ' ' + 'Sale: ' + matches.group(groupNum))
            stringCompleto = re.sub(matches.group(groupNum), r"", stringCompleto, 1)
            print(stringCompleto)

print('********************************************************************')
print(stringCompleto)
print('********************************************************************')


# una vez que match, borrar las transiciones especificadas, no la fruta del medio.
# después para el segmento de invariante siguiente, hay que buscar a partir de donde estaba la
# ultima transición que borre.
