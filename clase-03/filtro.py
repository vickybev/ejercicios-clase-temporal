colores = [
    "rojo",
    "azul",
    "verde agua",
    "negro",
    "amarillo pastel",
    "gris",
    "violeta",
]

print("Colores con más de una palabra:")
for color in colores:
    if " " in color:
        print(color)

print("\nColores que empiezan con vocal:")
for color in colores:
    if color[0].lower() in "aeiouáéíóú":
        print(color)

colores_ordenados = sorted(colores)

print("\nLista ordenada alfabéticamente:")
print(colores_ordenados)

print("\nPrimeros tres colores de la lista ordenada:")
print(colores_ordenados[:3])

print("\nLista original sin modificar:")
print(colores)
