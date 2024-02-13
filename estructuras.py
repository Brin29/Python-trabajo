# Listas
# Creación de listas mediante corchetes []
lista = [1, 2, 3, 'a', 'b', 'c']
# Creación de listas mediante la función list()
lista2 = list((1, 2, 3, 'a', 'b', 'c'))
# Acceso a los elementos de una lista
elemento = lista[0]
# Sublistas
sublista = lista[1:4:2]
# Operaciones que no modifican una lista
longitud = len(lista)
minimo = min(lista)
maximo = max(lista)
# Operaciones que modifican una lista
lista.append(4)
lista.extend([5, 6])
lista.insert(0, 0)
lista.remove('a')
dato = lista.pop(2)
lista.sort()
lista.reverse()

# Tuplas
# Creación de tuplas mediante paréntesis ()
tupla = (1, 2, 3, 'a', 'b', 'c')
# Creación de tuplas mediante la función tuple()
tupla2 = tuple([1, 2, 3, 'a', 'b', 'c'])
# Acceso a los elementos de una tupla
elemento_tupla = tupla[0]

# Diccionarios
# Creación de diccionarios mediante llaves {}
diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}
# Acceso a los elementos de un diccionario
valor = diccionario['clave1']
# Operaciones que no modifican un diccionario
longitud_diccionario = len(diccionario)
claves = diccionario.keys()
valores = diccionario.values()
items = diccionario.items()
# Operaciones que modifican un diccionario
diccionario['clave3'] = 'valor3'
diccionario.update({'clave4': 'valor4'})
valor_eliminado = diccionario.pop('clave1')
clave_valor_eliminado = diccionario.popitem()
del diccionario['clave2']
diccionario.clear()

# Revisar existencia de un elemento en un diccionario
existe_elemento = 'gino' in diccionario

# Copia de diccionarios
# Copia por referencia
diccionario_copia_referencia = diccionario
# Copia por valor
diccionario_copia_valor = dict(diccionario)
