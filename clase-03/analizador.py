titulo = input("Título de la obra: ")
palabras = titulo.split()
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
cantidad_vocales = 0

for letra in titulo:
    if letra in vocales:
        cantidad_vocales = cantidad_vocales + 1

palabras_invertidas = palabras[::-1]
titulo_invertido = " ".join(palabras_invertidas)

print("Cantidad de caracteres:", len(titulo))
print("Cantidad de palabras:", len(palabras))
print("Cantidad de vocales:", cantidad_vocales)
print("Título en mayúsculas:", titulo.upper())
print("Palabras invertidas:", titulo_invertido)
