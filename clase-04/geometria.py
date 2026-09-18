# Cada función calcula y retorna su resultado, sin imprimirlo.
def area_rectangulo(ancho, alto):
    return ancho * alto


def perimetro_rectangulo(ancho, alto):
    return 2 * (ancho + alto)


# Reutilizamos las dos funciones y agregamos la orientación.
def describir(ancho, alto):
    area = area_rectangulo(ancho, alto)
    perimetro = perimetro_rectangulo(ancho, alto)
    if ancho > alto:
        orientacion = "horizontal"
    elif alto > ancho:
        orientacion = "vertical"
    else:
        orientacion = "cuadrado"
    return f"Área: {area} - Perímetro: {perimetro} - Orientación: {orientacion}"


# Probamos las tres funciones con medidas de las tres orientaciones.
medidas = [[6, 3], [3, 6], [4, 4]]
for medida in medidas:
    ancho = medida[0]
    alto = medida[1]
    print("Medidas:", ancho, "x", alto)
    print("Área:", area_rectangulo(ancho, alto))
    print("Perímetro:", perimetro_rectangulo(ancho, alto))
    print(describir(ancho, alto))
