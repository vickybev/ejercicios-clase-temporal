# Se piden las dimensiones de la pieza y se convierten a números decimales.
ancho_cm = float(input("Ancho de la pieza (cm): "))
alto_cm = float(input("Alto de la pieza (cm): "))

# Se calcula la superficie en cm² y se convierte a m².
superficie_cm2 = ancho_cm * alto_cm
superficie_m2 = superficie_cm2 / 10_000

# La imprenta cobra $450 por cada metro cuadrado.
precio_base = superficie_m2 * 450

# Se calcula el precio final según el tamaño de la pieza.
if superficie_m2 > 2:
    precio_final = precio_base * 1.15
    detalle = "se aplicó un recargo del 15% por manipulación"
elif superficie_m2 < 0.5:
    precio_final = 300
    detalle = "se aplicó el cargo mínimo de $300"
else:
    precio_final = precio_base
    detalle = "no se aplicaron recargos ni cargo mínimo"

# Se presenta el presupuesto completo con los valores formateados.
print("\n========================================")
print("PRESUPUESTO DE IMPRESIÓN")
print("========================================")
print(f"Dimensiones: {ancho_cm:.2f} x {alto_cm:.2f} cm")
print(f"Superficie: {superficie_m2:.3f} m²")
print(f"Precio base: ${precio_base:.2f}")
print(f"Detalle: {detalle}")
print(f"PRECIO FINAL: ${precio_final:.2f}")
print("========================================")
