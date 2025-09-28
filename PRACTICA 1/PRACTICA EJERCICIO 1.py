#Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos) Reglas:
#Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar sus tipos de variables
# Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una conversión de datos
#Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
#tiene un bono del 5% en el mes diciembre”
#Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda.

nombre = "Kassandra Alberca"
salario = 1500.0
edad = "24"
compania = "Miskimayo"

edad_entero = int(edad)

if edad_entero > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_porcentaje = 0.10
else:
    print("Usted tiene un bono del 5% en el mes de diciembre")
    bono_porcentaje = 0.05

bono_final = (salario ** 2) + (salario * bono_porcentaje)

print(f"Bono final calculado: {bono_final}")