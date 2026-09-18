# Clase 4: funciones, datos y objetos

Fuente docente: `C:\Users\Vicky\Documents\PROGRAMACION 2\clase4_teoria.pptx`, 42 diapositivas. Incorporado el 18/9/2026 como material de la clase pasada, según tu aclaración.

## 1. Funciones: escribir una operación una sola vez

Diapositivas 6 a 14. Una función reúne instrucciones bajo un nombre. Los **parámetros** son los nombres que aparecen en su definición; los **argumentos** son los valores concretos que le pasamos al llamarla.

```python
def area_rectangulo(ancho, alto):
    """Devuelve el área del rectángulo."""
    return ancho * alto

medida = area_rectangulo(30, 20)
print(medida)  # 600
```

`def` define la función. La sangría indica qué instrucciones le pertenecen. El texto entre triples comillas es su **docstring**, una descripción que el docente pide incluir siempre. `return` entrega el resultado y termina la ejecución de esa llamada.

**Diferencia central:** `print()` muestra; `return` permite usar el resultado después. Si una función llega al final sin `return`, devuelve `None`. Por eso asignar el resultado de una función que solo imprime no guarda el número impreso.

Una variable creada dentro de una función es local. Para usar su resultado afuera, normalmente lo retornamos. Un parámetro con valor por defecto permite omitir ese argumento: `es_cara(precio, limite=2000)` compara con 2000 salvo que se indique otro límite.

Aplicación: [geometria.py](geometria.py) combina funciones; [validador.py](validador.py) usa `return` para terminar un pedido repetido.

## 2. Diccionarios: acceder por nombre

Diapositivas 16 a 20. En la lista se consulta por índice; en el diccionario se consulta por clave.

```python
obra = {"titulo": "Retrato", "anio": 2022}
print(obra["titulo"])
obra["precio"] = 900
print(obra.get("autor", "Sin autor"))
```

Una clave inexistente consultada con corchetes produce `KeyError`. Podemos comprobar `"autor" in obra` o usar `.get()` con un valor alternativo. Asignar una clave la agrega si no existe, o cambia su valor si ya existe. `del` elimina una clave.

Al recorrer `for clave in obra`, recibimos claves. `.values()` entrega valores y `.items()` permite obtener clave y valor juntos.

Aplicación: [inventario.py](inventario.py) comprueba la existencia de un material antes de consultar el stock.

## 3. Lista de diccionarios: recorrer, filtrar y contar

Diapositivas 22 a 24. En `obras[0]["titulo"]`, primero elegimos el primer diccionario y después su título.

**Filtrar:** crear una lista vacía, recorrer los elementos, comprobar una condición y agregar las coincidencias con `append`.

**Contar:** usar cada autor como clave de un diccionario y su cantidad de obras como valor. Si aparece por primera vez, iniciar el contador; si vuelve a aparecer, incrementarlo.

Aplicación: [estadisticas.py](estadisticas.py) y [catalogo.py](catalogo.py).

## 4. Clases y objetos

Diapositivas 26 a 31. Una clase reúne una forma de inicializar datos y los métodos que trabajan con ellos. Los objetos creados a partir de esa clase tienen sus propios valores.

```python
class Obra:
    def __init__(self, titulo, anio):
        """Guarda el título y el año de esta obra."""
        self.titulo = titulo
        self.anio = anio

    def antiguedad(self):
        """Devuelve la antigüedad usando 2026 como referencia."""
        return 2026 - self.anio

obra = Obra("Retrato", 2022)
print(obra.titulo)         # Retrato
print(obra.antiguedad())   # 4
```

`__init__` inicializa el objeto. `self` identifica la instancia sobre la que trabaja el método. Desde afuera usamos `obra.anio`; dentro de un método usamos `self.anio`.

## 5. Métodos y cambios de estado

Diapositivas 33 a 40. Los métodos se definen dentro de la clase y se llaman con paréntesis: `obra.ficha()`. Sin paréntesis, `obra.ficha` se refiere al método, pero no lo ejecuta.

Un método puede consultar datos, retornar un resultado o modificar el objeto. En `consumir`, el nuevo stock permanece guardado después de que termina la llamada. A esos datos actuales del objeto los llamamos **estado**.

Una lista también puede contener objetos. El bucle `for` no cambia: en lugar de `obra["precio"]`, consultamos `obra.precio`. `__str__` aparece como un extra opcional para decidir el texto de `print(obra)`.

Aplicación: [catalogo_poo.py](catalogo_poo.py), [color_poo.py](color_poo.py), [material.py](material.py) e [integrador.py](integrador.py).

## 6. Requisitos docentes comprobados

- Funciones pequeñas, con nombres que describan su tarea y una línea de docstring.
- No usar `@dataclass`, `@property`, herencia ni `super()`: el docente los excluye en la diapositiva 40. Las soluciones no los usan.
- Guardar los ejercicios en `clase-04`, un archivo por ejercicio y commits descriptivos.
- Poder explicar el código o escribir comentarios propios. Los comentarios generados sirven para estudiar, no acreditan que sean personales.

Se agregaron las docstrings que faltaban en las soluciones iniciales. Los comentarios que empiezan con `#` se conservaron: explican bloques, pero no sustituyen una docstring.

## 7. Precisiones separadas del contenido docente

Estas aclaraciones evitan tomar simplificaciones del material como reglas universales:

- **Diapositiva 9:** el código de la columna con `return` imprime solo **700**. El 600 es el valor que se guarda en `x`; no hay un `print(x)` adicional. Se comprobó ejecutando el fragmento.
- **Diapositiva 12:** `return` no es la única forma de producir un efecto fuera de una función. También se puede modificar una lista u objeto recibido, como hacen `agregar_obra` y `consumir`. Conviene distinguir devolver un resultado de modificar datos compartidos.
- **Diapositiva 17:** `obra[0]` falla en el diccionario mostrado porque no tiene la clave 0. Un diccionario sí puede tener claves enteras; el 0 sería una clave, no una posición.
- **Diapositivas 27 a 29:** una clase común inicializa atributos de forma consistente, pero no impide por sí sola crear otros por error ni valida sus valores automáticamente.
- **Diapositiva 34:** `Obra(2020)` es un esquema comparativo. No puede copiarse sin adaptar la clase que antes recibe título, autor y año.
- **Diapositiva 42:** anuncia archivos y errores para la próxima clase; el teórico 5 realmente recibido trata módulos y pygame. Para estudiar esa clase seguimos el archivo recibido.

Referencias externas: [Python: funciones y documentación](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) y [Python: clases](https://docs.python.org/3/tutorial/classes.html). Los ejemplos y requisitos del curso provienen del PowerPoint identificado al comienzo.
