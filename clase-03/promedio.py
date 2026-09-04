precios = []
total = 0

while True:
    entrada = input("Precio (o 'fin' para terminar): ")

    if entrada.lower() == "fin":
        break

    precio = float(entrada)
    precios.append(precio)
    total = total + precio

if len(precios) == 0:
    print("No se cargaron precios.")
else:
    cantidad = len(precios)
    promedio = total / cantidad

    mas_caro = precios[0]
    mas_barato = precios[0]

    for precio in precios:
        if precio > mas_caro:
            mas_caro = precio

        if precio < mas_barato:
            mas_barato = precio

    print("Cantidad de precios:", cantidad)
    print("Total:", total)
    print("Promedio:", promedio)
    print("Precio más caro:", mas_caro)
    print("Precio más barato:", mas_barato)

    print("\nComprobación con funciones de Python:")
    print("Total con sum():", sum(precios))
    print("Más caro con max():", max(precios))
    print("Más barato con min():", min(precios))
