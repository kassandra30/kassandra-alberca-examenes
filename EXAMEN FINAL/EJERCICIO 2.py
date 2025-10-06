"""Utilizar el concepto de módulo necesariamente.
Y escribir un programa para el
manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
Reglas:
- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)"""


import modulo_listas as ml

print("=== CASO 1 ===")
lista1 = ml.generar_lista(5)
if lista1:
    sinrep1 = ml.sin_repetidos(lista1)
    ml.ordenar_listas(sinrep1)
    ml.mayor_par(sinrep1)

print("\n=== CASO 2 ===")
lista2 = ml.generar_lista(7)
if lista2:
    sinrep2 = ml.sin_repetidos(lista2)
    ml.ordenar_listas(sinrep2)
    ml.mayor_par(sinrep2)
