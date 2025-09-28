#Caso: Calculadora de propinas Crea un programa que permita ingresar el total de una cuenta en un restaurante,
# el porcentaje de propina que desea dejar el cliente y el número de personas que
# dividirán la cuenta. El programa debe mostrar:
# El monto total con propina.
# El monto que debe pagar cada persona (con 2 decimales).
# Un mensaje será personalizado, indicará si el monto individual supera los 100
# soles, mostrando un mensaje de advertencia si es el caso.
# Entrada esperada (por input):
# Total de la cuenta: float
# Porcentaje de propina: float
# Número de personas: int
# Salida ejemplo (output):
# Monto total con propina: S/. 230.00
# Cada persona debe pagar: S/. 115.00
# ¡Advertencia! El monto por persona supera los S/. 100

Cuenta_total=input("Ingrese el total de la cuenta:")
Porcentaje_de_propina=input("Ingrese el porcentaje de propina: ")
Num_clientes=input("Ingrese el numero de personas:")
Propina_total=float(Cuenta_total) *float(Porcentaje_de_propina)/100
Total_Cuenta=float(Cuenta_total)+float(Porcentaje_de_propina)
Pago_por_persona=Total_Cuenta/int(Num_clientes)
print("La propina es de:",Propina_total)
print("El monto total a pagar por persona es de:",format(f"{Pago_por_persona:.2f}"))
if Pago_por_persona>100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
