# Cada objeto guarda el nombre del color y sus componentes entre 0 y 255.
class Color:
    def __init__(self, nombre, r, g, b):
        """Guarda los datos iniciales de este objeto."""
        self.nombre = nombre
        self.r = r
        self.g = g
        self.b = b

    def luminosidad(self):
        """Calcula la luminosidad con la fórmula ponderada docente."""
        return 0.299 * self.r + 0.587 * self.g + 0.114 * self.b

    # Reutilizamos luminosidad en lugar de repetir la fórmula.
    def es_claro(self):
        """Indica si la luminosidad supera 128."""
        return self.luminosidad() > 128

    # 02X escribe cada componente con dos dígitos hexadecimales en mayúscula.
    def hex(self):
        """Devuelve el color en formato hexadecimal #RRGGBB."""
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"


colores = [Color("Blanco", 255, 255, 255), Color("Negro", 0, 0, 0),
           Color("Rojo", 255, 0, 0), Color("Amarillo", 255, 255, 0)]
for color in colores:
    tipo = "oscuro"
    if color.es_claro():
        tipo = "claro"
    print(color.nombre, color.hex(), tipo)
