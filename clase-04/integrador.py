# Reutilizamos aquí la clase del 4.6 para que este archivo funcione por sí solo.
class Material:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def valor_total(self):
        return self.precio_unitario * self.stock

    def hay_stock(self):
        return self.stock >= 1

    def consumir(self, cantidad):
        if cantidad <= 0 or cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True


# Estas funciones están fuera de la clase: reciben la lista completa.
def valor_inventario(materiales):
    total = 0
    for material in materiales:
        total += material.valor_total()
    return total


def sin_stock(materiales):
    agotados = []
    for material in materiales:
        if not material.hay_stock():
            agotados.append(material)
    return agotados


# Comparamos el precio de una unidad, no el valor de todo el stock.
def mas_caro(materiales):
    if len(materiales) == 0:
        return None
    mayor = materiales[0]
    for material in materiales:
        if material.precio_unitario > mayor.precio_unitario:
            mayor = material
    return mayor


materiales = [Material("Papel", 10, 120), Material("Tinta negra", 450, 8),
              Material("Tinta color", 600, 0), Material("Cartón", 30, 45),
              Material("Cinta", 80, 0)]
print("Valor del inventario:", valor_inventario(materiales))
print("Materiales agotados:")
for material in sin_stock(materiales):
    print(material.nombre)
caro = mas_caro(materiales)
if caro is not None:
    print("Mayor precio unitario:", caro.nombre, caro.precio_unitario)
