# La primera obra es la candidata; la reemplazamos si aparece otra más cara.
def obra_mas_cara(obras):
    if len(obras) == 0:
        return None
    mayor = obras[0]
    for obra in obras:
        if obra["precio"] > mayor["precio"]:
            mayor = obra
    return mayor


# Solo agregamos un autor si todavía no está en la lista.
def autores(obras):
    resultado = []
    for obra in obras:
        if obra["autor"] not in resultado:
            resultado.append(obra["autor"])
    return resultado


# Cada autor es una clave, y su valor cuenta cuántas obras tiene.
def obras_por_autor(obras):
    cantidades = {}
    for obra in obras:
        autor = obra["autor"]
        if autor not in cantidades:
            cantidades[autor] = 0
        cantidades[autor] += 1
    return cantidades


# Después del año indicado significa mayor estricto, sin incluir ese año.
def posteriores_a(obras, anio):
    resultado = []
    for obra in obras:
        if obra["anio"] > anio:
            resultado.append(obra)
    return resultado


obras = [
    {"titulo": "Sin título", "autor": "Pérez", "anio": 2020, "precio": 1500},
    {"titulo": "Serie azul", "autor": "Gómez", "anio": 2018, "precio": 3200},
    {"titulo": "Retrato", "autor": "Pérez", "anio": 2022, "precio": 900},
    {"titulo": "Paisaje", "autor": "Díaz", "anio": 2015, "precio": 4100},
    {"titulo": "Estudio", "autor": "Gómez", "anio": 2021, "precio": 2000},
]
print("Obra más cara:", obra_mas_cara(obras))
print("Autores:", autores(obras))
print("Cantidad por autor:", obras_por_autor(obras))
print("Posteriores a 2020:", posteriores_a(obras, 2020))
