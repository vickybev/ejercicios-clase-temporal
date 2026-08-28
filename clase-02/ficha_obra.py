# Se piden los datos de la obra y se convierten los valores numéricos.
titulo = input("Título: ")
autor = input("Autor: ")
anio = int(input("Año: "))
ancho = float(input("Ancho (cm): "))
alto = float(input("Alto (cm): "))

# Se calcula la superficie de la obra en centímetros cuadrados.
area = ancho * alto

# Se compara el ancho con el alto para determinar la orientación.
if ancho > alto:
    orientacion = "horizontal"
elif alto > ancho:
    orientacion = "vertical"
else:
    orientacion = "cuadrada"

# Se clasifica el tamaño según el área calculada.
if area < 1000:
    tamanio = "chica"
elif area <= 5000:
    tamanio = "mediana"
else:
    tamanio = "grande"

# Se muestran todos los datos juntos en una ficha formateada.
print("\n========================================")
print("FICHA TÉCNICA DE OBRA")
print("========================================")
print(f"Título: {titulo}")
print(f"Autor: {autor}")
print(f"Año: {anio}")
print(f"Dimensiones: {ancho:.1f} x {alto:.1f} cm")
print(f"Área: {area:.1f} cm²")
print(f"Orientación: {orientacion}")
print(f"Tamaño: {tamanio}")
print("========================================")
