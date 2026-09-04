medida_base = float(input("Medida base en centímetros: "))

for multiplicador in range(1, 11):
    resultado = medida_base * multiplicador

    if resultado > 100:
        print(medida_base, "x", multiplicador, "=", resultado, "cm - Supera los 100 cm")
    else:
        print(medida_base, "x", multiplicador, "=", resultado, "cm")
