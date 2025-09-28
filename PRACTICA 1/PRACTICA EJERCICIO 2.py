#Caso: Reporte de calificaciones:
#Se tiene un alumno con calificaciones en tres cursos:
#Matemáticas: 17, Ciencia: 14, Historia: 15
#Cada curso tiene un peso diferente en la nota final:
#Matemáticas: 40%, Ciencia: 30%, Historia: 30%
#Realizar lo que se pide a continuación:
#Calcula la nota final ponderada del alumno.
#Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
#Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
#"¿Aprobado?: True" o "¿Aprobado?: Sí"
#Genera una cadena resumen que diga:
#"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
#En caso no apruebe indicar lo contrario en los mensajes.

matematicas = 17
ciencia = 14
historia = 15

porciento_matematicas = 0.40
porciento_ciencia = 0.30
porciento_historia = 0.30

nota_final = (matematicas * porciento_matematicas +
              ciencia * porciento_ciencia +
              historia * porciento_historia)

nota_final = round(nota_final, 1)

print(f"La nota final es: {nota_final}")

aprobado = nota_final >= 13.0

print(f"¿Aprobado?: {aprobado}")

estado = "Aprobado" if aprobado else "Desaprobado"
print(f"¿Aprobado?: {'Sí' if aprobado else 'No'}")

resumen = f"El estudiante obtuvo una nota final de {nota_final} y su estado final es: {estado}"
print(resumen)