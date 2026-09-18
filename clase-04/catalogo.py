# Etapa A: cada obra es un diccionario dentro de una lista.
def agregar_obra(catalogo):
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año (entero): "))
    precio = float(input("Precio (usá punto para decimales): "))
    obra = {"titulo": titulo, "autor": autor, "anio": anio, "precio": precio}
    catalogo.append(obra)


# Esta función muestra información; no devuelve una lista nueva.
def listar_obras(catalogo):
    if len(catalogo) == 0:
        print("El catálogo está vacío.")
    for i in range(len(catalogo)):
        obra = catalogo[i]
        print(f"{i + 1}. {obra['titulo']} - {obra['autor']} ({obra['anio']}) - ${obra['precio']:.2f}")


# La búsqueda devuelve una lista y deja la impresión a quien la llama.
def buscar_por_autor(catalogo, autor):
    encontradas = []
    for obra in catalogo:
        if obra["autor"].strip().lower() == autor.strip().lower():
            encontradas.append(obra)
    return encontradas


# Si no hay obras, usamos promedio cero para evitar dividir por cero.
def estadisticas(catalogo):
    cantidad = len(catalogo)
    total = 0
    for obra in catalogo:
        total += obra["precio"]
    promedio = 0
    if cantidad > 0:
        promedio = total / cantidad
    return {"cantidad": cantidad, "total": total, "promedio": promedio}


# El menú pide la opción y delega las operaciones a las funciones.
catalogo = []
while True:
    print("\n1. Agregar   2. Listar   3. Buscar   4. Estadísticas   5. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        agregar_obra(catalogo)
    elif opcion == "2":
        listar_obras(catalogo)
    elif opcion == "3":
        autor = input("Autor a buscar: ")
        listar_obras(buscar_por_autor(catalogo, autor))
    elif opcion == "4":
        datos = estadisticas(catalogo)
        print("Cantidad:", datos["cantidad"])
        print(f"Total: ${datos['total']:.2f} - Promedio: ${datos['promedio']:.2f}")
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
