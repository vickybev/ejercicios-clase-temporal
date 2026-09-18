# Etapa B: la clase reúne los datos y las acciones de una obra.
class Obra:
    def __init__(self, titulo, autor, anio, precio):
        """Guarda los datos iniciales de este objeto."""
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.precio = precio

    # Retorna una ficha: quien llama decide si la imprime.
    def ficha(self):
        """Devuelve el texto que describe esta obra."""
        return f"{self.titulo} - {self.autor} ({self.anio}) - ${self.precio:.2f}"

    # Usamos el año del curso para no introducir otro import.
    def antiguedad(self):
        """Devuelve los años transcurridos desde la obra hasta 2026."""
        return 2026 - self.anio

    # El límite puede cambiarse al llamar al método.
    def es_cara(self, limite=2000):
        """Indica si el precio supera el límite recibido."""
        return self.precio > limite


# Las funciones conservan sus responsabilidades, pero trabajan con objetos.
def agregar_obra(catalogo):
    """Pide los datos y agrega una obra al catálogo."""
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año (entero): "))
    precio = float(input("Precio (usá punto para decimales): "))
    catalogo.append(Obra(titulo, autor, anio, precio))


def listar_obras(catalogo):
    """Muestra las obras numeradas o avisa si no hay ninguna."""
    if len(catalogo) == 0:
        print("El catálogo está vacío.")
    for i in range(len(catalogo)):
        print(f"{i + 1}. {catalogo[i].ficha()}")


def buscar_por_autor(catalogo, autor):
    """Devuelve las obras del autor indicado."""
    encontradas = []
    for obra in catalogo:
        if obra.autor.strip().lower() == autor.strip().lower():
            encontradas.append(obra)
    return encontradas


def estadisticas(catalogo):
    """Devuelve cantidad, total y promedio del catálogo."""
    total = 0
    for obra in catalogo:
        total += obra.precio
    cantidad = len(catalogo)
    promedio = 0
    if cantidad > 0:
        promedio = total / cantidad
    return {"cantidad": cantidad, "total": total, "promedio": promedio}


# Tres obras iniciales permiten probar los métodos sin cargar datos a mano.
catalogo = [
    Obra("Sin título", "Pérez", 2020, 1500),
    Obra("Serie azul", "Gómez", 2018, 3200),
    Obra("Retrato", "Pérez", 2022, 900),
]
for obra in catalogo:
    print(obra.ficha(), "- Antigüedad:", obra.antiguedad(), "años")
print("Obras de más de $2000:")
for obra in catalogo:
    if obra.es_cara():
        print(obra.ficha())


# El mismo menú de la etapa A sigue funcionando con objetos.
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
