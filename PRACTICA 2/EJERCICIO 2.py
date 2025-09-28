"""2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""

def normalizar_nombres(nombres):
    resultado = []
    vistos = []
    for n in nombres:
        for parte in n.split():
            p = parte.strip().title()
            if p not in vistos:
                resultado.append(p)
                vistos.append(p)
    return resultado

nombres = [" Kass ", "Nicol", "Leandro", "PAMELA", "Estrella", "Ana", "Gustavo calero"]
print(normalizar_nombres(nombres))