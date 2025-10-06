"""(2 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados"""

from datetime import datetime


def decorador_suma(funcion):
    def interna(**kwargs):

        ahora = datetime.now()

        print(f"El decorador está siendo ejecutado a las {ahora.hour}h con {ahora.minute}min y {ahora.second}s.")
        print(f"La suma total de los valores es: {sum(kwargs.values())}")
        funcion(**kwargs)

    return interna


@decorador_suma
def mostrar_mayor(**kwargs):

    print(f"El número mayor es: {max(kwargs.values())}")


print("---- Ejemplo 1 ----")

mostrar_mayor(value_1=10, value_2=20, value_3=5, value_4=8, value_5=12, value_6=9)


print("\n---- Ejemplo 2 ----")

mostrar_mayor(a=3, b=15, c=7, d=1, e=9, f=11, value_7=10, value_8=22, value_9=45)

print("\n---- Ejemplo 3 ----")

mostrar_mayor(n1=100, n2=50, n3=75, n4=120, n5=90)
