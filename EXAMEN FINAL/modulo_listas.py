
import random


def generar_lista(x):
    try:
        if type(x) != int:
            raise TypeError("X debe ser un número entero.")
        lista = [random.randint(1, 50) for _ in range(x)]
        print("Lista generada:", lista)


        indice = int(input(f"Ingrese un índice (0 a {len(lista)-1}): "))
        print("Elemento en el índice", indice, "es:", lista[indice])

        return lista
    except ValueError:
        print("Debe ingresar un número entero para el índice.")
    except IndexError:
        print("El índice no existe en la lista.")
    except TypeError as e:
        print(e)


def sin_repetidos(lista):
    lista_unica = list(set(lista))
    print("Lista sin repetidos:", lista_unica)
    return lista_unica


def ordenar_listas(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)
    print("De mayor a menor:", mayor_a_menor)
    print("De menor a mayor:", menor_a_mayor)
    return mayor_a_menor, menor_a_mayor


def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        print("El mayor número par es:", max(pares))
        return max(pares)
    else:
        print("No hay números pares en la lista.")
        return None
