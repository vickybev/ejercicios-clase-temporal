# Cada material guarda su precio y la cantidad disponible.
class Material:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def valor_total(self):
        return self.precio_unitario * self.stock

    def hay_stock(self):
        return self.stock >= 1

    # Rechazamos cantidades no positivas para no aumentar el stock por error.
    def consumir(self, cantidad):
        if cantidad <= 0 or cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True


# Probamos los tres métodos: consumo posible y consumo que excede el stock.
materiales = [Material("Papel", 10, 120), Material("Tinta", 450, 3)]
for material in materiales:
    print("\nMaterial:", material.nombre)
    print("Valor inicial:", material.valor_total())
    print("¿Hay stock?", material.hay_stock())
    print("¿Se pudieron consumir 2?", material.consumir(2))
    print("Stock restante:", material.stock)
    print("¿Se pudieron consumir 999?", material.consumir(999))
    print("Stock después del intento:", material.stock)
