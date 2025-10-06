"""(2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante."""

from datetime import datetime


def conteo(funcion):
    def interna(*args):
        if len(args) <= 1:
            print("Debes ingresar más de un parámetro para continuar.")
        else:
            funcion(*args)
            print("La función fue ejecutada exitosamente.")
    return interna


@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    ahora = datetime.now()
    hora = ahora.hour
    minuto = ahora.minute
    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos.")
    print(f"Su promedio es {promedio:.2f}")  # .2f = muestra solo 2 decimales

    print("---- Ejemplo correcto ----")
    registrar_alumno("Kass", 24, 14, 17, 14, 16)


print("\n---- Ejemplo con error ----")
registrar_alumno("Kass")
