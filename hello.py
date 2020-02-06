#!/usr/bin/env python
import re
inicio = ''
final = ''

# Abro el archivo de Log.
file = open('/home/agustin/proyectos/pc/python.txt')
stringCompleto = file.read()
file.close()

# Reemplazo los saltos de línea porque son problemáticos para las regEx.
stringCompleto = stringCompleto.replace('\n', ',')
# print(stringCompleto)

# Armo las regExs
invariante = re.compile(r'(T1,(?:T\d(?:\d)?,)*?T4,)?')

# lista = invariante.findall(stringCompleto)

# uso un ¿iterator? en vez de findall para obtener todos los objetos de match y poder
# usar las propiedades start, end y group
for m in invariante.finditer(stringCompleto):
    if m.group(0) != '':
        print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
        inicio = m.start()
        final = m.end()
        break  # sacar para ver todos los matches

# Saco un invariante, aca vamos a tener problema con las de dos cifras.
nuevoString = stringCompleto[:inicio] + stringCompleto[inicio + 3:final - 3] + stringCompleto[final:]
print(stringCompleto)
print(nuevoString)

# La última transición que borré está en final.

# una vez que match, borrar las transiciones especificadas, no la fruta del medio.
# después para el segmento de invariante siguiente, hay que buscar a partir de donde estaba la
# ultima transición que borre.
