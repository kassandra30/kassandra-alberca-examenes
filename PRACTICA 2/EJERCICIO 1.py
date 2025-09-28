"""Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

def procesar_notas(estudiantes):
    resultados = {}
    mejor = ("", 0)
    for n, notas in estudiantes.items():
        p = sum(notas)/len(notas)
        estado = "aprobado" if p>=11 else "desaprobado"
        resultados[n] = {"promedio": p, "estado": estado}
        if p > mejor[1]:
            mejor = (n, p)
    print("Mayor promedio:", mejor[0], mejor[1])
    return resultados

Estudiantes = {"Kass":[13,11,10], "Nicol":[9,8,10], "Leandro":[15,13,14]}
print(procesar_notas(Estudiantes))