"""Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:

• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.

• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos

o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido."""


class Persona:

    def __init__(self, nombre, edad, nacionalidad="peruana", saldo=0.0):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def actualizar_nombre(self, nombre):
        self.nombre = nombre

    def actualizar_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("Edad inválida. Debe ser mayor a 0.")

    def cumplir_anios(self):
        self.edad += 1

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre}: {self.saldo:.2f} soles")

    def transferir(self, destino, monto):
        if self.saldo < monto:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto
            destino.saldo += monto
            print(f"Transferencia de {monto:.2f}"
                  f" soles realizada de {self.nombre} "
                  f"a {destino.nombre}")


class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo,
                 nacionalidad="peruana", saldo=0.0):
        super().__init__(nombre, edad, nacionalidad, saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self, porcentaje=0.30):
        self.sueldo += self.sueldo * porcentaje
        print(f"Nuevo sueldo de {self.nombre}: {self.sueldo:.2f} soles")

    def prediccion(self, anio_objetivo, edad_param=None):
        anios_faltantes = anio_objetivo - 2025
        if edad_param is not None:
            if edad_param < self.edad:
                print("No es posible realizar la operación")
                return
            else:
                edad_futura = edad_param + anios_faltantes
        else:
            edad_futura = self.edad + anios_faltantes
        print(f"En el año {anio_objetivo} tendrá {edad_futura} años")


# PRUEBAS
emp1 = Empleado("Kass", 24, 1500, saldo=1000)
emp2 = Empleado("Leandro", 26, 2000, saldo=500)
print("\n--- Aumentos de sueldo ---")
emp1.aumento_sueldo()      # primer aumento
emp1.aumento_sueldo(0.20)  # segundo aumento
emp2.aumento_sueldo()      # aumento a María
print("\n--- Saldos antes de transferencia ---")
emp1.mostrar_saldo()
emp2.mostrar_saldo()
print("\n--- Transferencia exitosa ---")
emp1.transferir(emp2, 300)
print("\n--- Saldos después de transferencia ---")
emp1.mostrar_saldo()
emp2.mostrar_saldo()
print("\n--- Transferencia con saldo insuficiente ---")
emp2.transferir(emp1, 5000)
print("\n--- Predicciones de edad ---")
emp1.prediccion(2035)
emp2.prediccion(2030, edad_param=35)
emp2.prediccion(2030, edad_param=20)
