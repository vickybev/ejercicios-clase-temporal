# Clase 5: carpetas y pygame

Fuente docente: `C:\Users\Vicky\Documents\PROGRAMACION 2\clase5_teoria.pdf`, 44 páginas. Incorporado el 18/9/2026 como material de la clase pasada, según tu aclaración.

## 1. Organizar archivos por tema

Páginas 6 a 9. La estructura docente para un proyecto mayor separa responsabilidades:

| Archivo o carpeta | Responsabilidad |
|---|---|
| `main.py` | Preparar el programa y ejecutar el bucle principal |
| `ajustes.py` | Medidas, colores y otras constantes |
| `jugador.py` | Clase Jugador y sus métodos |
| `enemigo.py` | Clase Enemigo |
| `utiles.py` | Funciones compartidas |
| `assets/` | Imágenes y sonidos |
| `README.md` | Qué hace, cómo se instala y cómo se ejecuta |
| `.gitignore` | Archivos generados que no deben enviarse a Git |

La estructura anterior está pensada para el proyecto. Los ejercicios 5.1 a 5.3 mantienen un archivo por ejercicio, como pide su práctico.

## 2. Importar módulos propios

Páginas 11 a 17. En estos ejemplos, un módulo propio es un archivo `.py`. `import colores` permite usar nombres como `colores.LIMA` y `colores.es_oscuro(...)`. No se escribe `.py` en el import.

`from colores import LIMA` solo incorpora el nombre indicado; no agrega automáticamente las demás funciones. El docente recomienda empezar con `import modulo` para reconocer de dónde sale cada nombre.

Al importar por primera vez un módulo durante una ejecución, se ejecutan sus instrucciones de nivel superior. Para evitar que sus pruebas se ejecuten al importarlo, se usa:

```python
def doble(numero):
    """Devuelve el doble del número recibido."""
    return numero * 2

if __name__ == "__main__":
    print(doble(3))
```

Ese bloque corre cuando ejecutamos directamente el archivo; al importarlo, la función queda disponible sin imprimir el ejemplo. Los imports se agrupan arriba. No hay que llamar a un archivo propio `random.py` o `pygame.py`, porque puede ocultar la biblioteca que se quiere importar.

**Relación con el práctico 4:** allí dejamos Material repetida en el integrador para mantener cada archivo independiente con el alcance de esa clase. Ahora el teórico enseña las herramientas para reutilizarla mediante un módulo, protegiendo antes sus pruebas. No hace falta reescribir el práctico 4 para comprender los ejercicios 5.1 a 5.3.

## 3. Ventana y bucle principal

Páginas 19 a 25. pygame es una biblioteca externa. La instalación debe hacerse en el mismo intérprete o entorno de Python que ejecuta el programa:

```powershell
python -m pip install pygame==2.6.1
python .\clase-05\fondo.py
```

`pygame.init()` inicializa módulos; `set_mode((ancho, alto))` crea la superficie de pantalla; `set_caption` establece el título. El bucle repite cuatro pasos:

1. **Escuchar:** recoger los eventos y procesar teclado, clics y cierre.
2. **Actualizar:** cambiar posiciones, colores, listas o puntos.
3. **Dibujar:** limpiar con `fill`, dibujar los elementos y mostrar con `flip`.
4. **Limitar el ritmo:** usar `reloj.tick(60)`.

`pygame.QUIT` es el evento de cierre. Cambiar la variable de control a `False` permite terminar el bucle. `pygame.quit()` va después del bucle.

## 4. Coordenadas, figuras y texto

Páginas 27 a 30. El origen está arriba a la izquierda; x crece hacia la derecha e y hacia abajo. El centro de una ventana de 600 × 400 es (300, 200).

- `pygame.draw.rect`: rectángulo descrito por x, y, ancho y alto.
- `pygame.draw.circle`: círculo descrito por centro y radio.
- `pygame.draw.line`: línea entre dos puntos.
- `fuente.render`: produce una superficie con texto.
- `pantalla.blit`: dibuja esa superficie sobre otra.

La fuente se crea una vez antes del bucle. Lo que se dibuja más tarde puede tapar lo anterior. Para una animación sin rastros, se limpia el fondo y se vuelve a dibujar la escena en cada vuelta.

## 5. Elegir cómo leer el teclado

Páginas 32 y 33. `KEYDOWN` informa una pulsación; `get_pressed()` consulta qué teclas siguen presionadas.

| Necesidad | Lectura usada |
|---|---|
| Elegir un color o borrar dibujos | `KEYDOWN` |
| Mover mientras se mantiene una flecha | `get_pressed()` |

Para movimiento diagonal, los ejes se comprueban con condiciones independientes. El práctico [fondo.py](fondo.py) exige `KEYDOWN`: la pulsación cambia la variable de color y esa variable conserva el valor al soltar la tecla.

## 6. Mouse, listas y colisiones

Páginas 34 a 36. `MOUSEBUTTONDOWN` indica un clic y `evento.pos` da su posición. Guardar los dibujos en una lista permite redibujarlos tras limpiar la pantalla; es el patrón que usamos en [pintar.py](pintar.py).

`pygame.Rect` reúne posición y tamaño. `colliderect` detecta superposición entre rectángulos y `collidepoint` comprueba si un punto está dentro. Para impedir que un objeto salga de la ventana, sus límites se revisan después de mover y antes de dibujar.

En [rebote.py](rebote.py) controlamos el centro y el radio del círculo: el centro no puede acercarse a un borde más que el valor del radio. Al llegar a un borde, se invierte la velocidad del eje correspondiente.

## 7. El juego de ejemplo

Páginas 38 a 43. El ejemplo prepara un jugador y una moneda como Rect, mueve al jugador con las flechas, suma un punto al superponerlos y reubica la moneda con `random.randint`. Después dibuja ambos y el texto del puntaje.

La función `mover(rect, teclas, vel=5)` modifica el Rect recibido. No necesita retornar otro para que cambie de posición. Esto conecta el estado de los objetos de la clase 4 con la actualización del juego.

Para un proyecto mayor, el docente propone repartir este funcionamiento entre `ajustes.py`, `jugador.py`, `utiles.py` y `main.py`.

## 8. Precisiones separadas del contenido docente

- **Página 11:** tener los módulos en la misma carpeta es la configuración sencilla usada en clase; Python también busca módulos en otras rutas. No es una restricción universal.
- **Página 12:** `(r + g + b) / 3` es un promedio simple; no equivale a `0.299*r + 0.587*g + 0.114*b`, la fórmula del práctico 4. Por ejemplo, para verde (0, 255, 0), dan 85 y 149,685 respectivamente: pueden clasificarlo distinto. Se conserva la fórmula que exige cada ejercicio.
- **Página 20:** pygame se instala por intérprete o entorno, no necesariamente una única vez para toda la computadora.
- **Página 23:** `tick(60)` limita el ritmo aproximadamente a un máximo de 60 vueltas por segundo; no garantiza que una computadora lenta alcance ese ritmo.
- **Página 28:** en `draw.rect(pantalla, color, rectangulo, 3)`, el grosor es el **cuarto** argumento. El comentario docente que lo llama quinto es una errata. En `draw.circle`, el grosor sí ocupa el quinto lugar.
- **Página 40:** el fragmento del juego no incluye los controles de borde explicados en la página 36; hay que agregarlos si se quiere impedir que el jugador salga de la ventana. El ejercicio de rebote sí los incluye.
- **Obligatorio 1:** el título y el índice lo anuncian, pero este PDF termina en la página 44 remitiendo al práctico. No contiene la letra completa; no se deducen sus requisitos a partir del índice.

Referencias externas: [Python: módulos y ejecución directa](https://docs.python.org/3/tutorial/modules.html), [pygame: figuras y argumentos](https://www.pygame.org/docs/ref/draw.html), [pygame: tiempo](https://www.pygame.org/docs/ref/time.html). Las consignas y los ejemplos docentes provienen del PDF identificado al comienzo.
