# Se pide la medida y se convierte el texto ingresado a un número decimal.
centimetros = float(input("Medida en centímetros: "))

# Se calcula la misma medida en pulgadas y en milímetros.
pulgadas = centimetros / 2.54
milimetros = centimetros * 10

# Se muestran las conversiones redondeadas a dos decimales.
print("\n========================================")
print("CONVERSOR DE MEDIDAS")
print("========================================")
print(f"Centímetros: {centimetros:.2f} cm")
print(f"Pulgadas: {pulgadas:.2f} in")
print(f"Milímetros: {milimetros:.2f} mm")

# Se comprueba si la medida entra en un marco de hasta 30 centímetros.
if centimetros <= 30:
    print("Resultado: entra en un marco de 30 cm")
else:
    print("Resultado: no entra en un marco de 30 cm")

print("========================================")
