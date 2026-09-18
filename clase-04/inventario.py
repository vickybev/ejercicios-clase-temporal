# Comprobamos que la clave exista antes de consultar su cantidad.
def hay_stock(stock, material):
    """Indica si hay unidades disponibles del material."""
    return material in stock and stock[material] > 0


# Agregamos solamente los nombres que están por debajo del mínimo.
def faltantes(stock, minimo):
    """Devuelve los nombres con menos unidades que el mínimo."""
    materiales = []
    for material in stock:
        if stock[material] < minimo:
            materiales.append(material)
    return materiales


# Un acumulador suma las unidades de todos los materiales.
def total_unidades(stock):
    """Devuelve la suma de unidades del inventario."""
    total = 0
    for material in stock:
        total += stock[material]
    return total


stock = {"papel": 120, "tinta negra": 8, "tinta color": 3, "cartón": 45, "cinta": 0}
print("¿Hay papel?", hay_stock(stock, "papel"))
print("¿Hay cinta?", hay_stock(stock, "cinta"))
print("¿Hay pegamento?", hay_stock(stock, "pegamento"))
print("Con menos de 5 unidades:", faltantes(stock, 5))
print("Total de unidades:", total_unidades(stock))
