# Clase 5: carpetas y pygame

Fuente docente: `C:\Users\Vicky\Documents\PROGRAMACION 2\clase5_teoria.pdf`, 44 páginas. Incorporado el 18/9/2026 como material de la clase de hoy, viernes 18/9/2026. La clase pasada fue la 4.

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

## 9. Registro de clase: repaso, organización e imports

Fuente: fragmento de transcripción aportado durante la clase del 18/9/2026. Corresponde al inicio y a los temas de las páginas 2 a 14 del teórico. Este registro distingue lo expresado verbalmente de las precisiones técnicas.

### Adelanto verbal del Obligatorio 1, todavía tentativo

El docente indica que la letra oficial aún no está disponible y adelanta:

- Trabajo individual: crear un juego 2D de temática libre.
- Se evaluarán aspectos como la prolijidad, la organización del código y los commits.
- Se espera coherencia y cierto desarrollo. Menciona incorporar sonido y otros elementos; no hay en este fragmento un mínimo formal ni una rúbrica que permita fijarlos como requisitos definitivos.
- El dinosaurio del navegador aparece como ejemplo en la conversación, no como tema obligatorio.
- La letra se comunicará cuando esté disponible. No se confirma una fecha de entrega ni se especifican puntajes, cantidad de niveles o herramientas obligatorias.

La frase transcrita como «letra aleatorio uno» se interpreta como **letra del Obligatorio 1**, por el contexto y el título del teórico. No se reconstruyen las otras palabras ambiguas sobre el trámite de aprobación. Este adelanto no reemplaza la consigna escrita.

### Repaso: referirse a un método y ejecutarlo

El docente recupera el ejemplo de la página 4:

```python
class Obra:
    def __init__(self, titulo):
        """Guarda el título de esta obra."""
        self.titulo = titulo

    def ficha(self):
        """Devuelve la ficha como texto."""
        return f"Obra: {self.titulo}"

obra = Obra("Retrato")
print(obra.ficha)
print(obra.ficha())
```

La primera impresión muestra una representación del **método ligado a ese objeto**, parecida a `<bound method Obra.ficha of <...Obra object at 0x...>>`. No muestra todos los datos de la obra ni ejecuta `ficha`. La dirección representada puede cambiar entre ejecuciones.

La segunda ejecuta el método y muestra **Obra: Retrato**. `self.titulo` contiene el texto guardado al crear la instancia. La diferencia son los **paréntesis `()`**, no los dos puntos mencionados en un tramo de la transcripción. `obra.ficha` tampoco es la variable donde se guarda el título: ese atributo es `obra.titulo`.

### Organizar por responsabilidades

El docente explica que un archivo muy largo dificulta localizar y reutilizar código. Separar por temas también reduce la probabilidad de que varias personas editen las mismas líneas, aunque no elimina todos los conflictos de Git. No se trata de elegir siempre entre un archivo completo propio y otro ajeno: Git puede combinar cambios, y las coincidencias conflictivas se resuelven.

La propuesta es distinguir arranque, ajustes, clases o lógica, y guardar imágenes y sonidos en `assets/`. El ejemplo de colaboración ilustra la utilidad de esa separación, aunque se anuncia que el Obligatorio será individual.

`README.md` explica qué hace el proyecto y cómo ponerlo en funcionamiento. `.gitignore` contiene patrones para excluir archivos no versionados, como cachés o configuraciones locales. **Precisión:** agregar un archivo que ya está versionado al `.gitignore` no lo elimina de Git ni de su historial. [Documentación de Git](https://git-scm.com/docs/gitignore).

### Reutilizar colores desde otro archivo

Ejemplo docente ordenado para poder copiarlo, con ambos archivos en la misma carpeta:

```python
# colores.py
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
LIMA = (182, 255, 63)
NAVY = (20, 22, 43)

def es_oscuro(color):
    """Clasifica el color usando el promedio RGB del ejemplo docente."""
    r, g, b = color
    return (r + g + b) / 3 < 128
```

```python
# main.py
import colores

print(colores.LIMA)                 # (182, 255, 63)
print(colores.es_oscuro(colores.NAVY))  # True
```

Otra forma es `from colores import NAVY`: después se usa `NAVY` sin el prefijo. Ese import no incorpora el nombre `es_oscuro` al archivo que importa. **Precisión:** seleccionar un nombre no significa ejecutar únicamente ese fragmento del módulo; en la primera importación se ejecuta el código de nivel superior del módulo y se incorporan los nombres solicitados. [Documentación de Python](https://docs.python.org/3/tutorial/modules.html).

El fragmento termina cuando el docente está reformulando cómo describir el import. No se completa esa frase como si se hubiera escuchado su continuación.

## 10. Registro de clase: imports, ejecución y primera ventana

Fuente: segundo fragmento extenso de transcripción del 18/9/2026. Continúa los imports y avanza hasta el dibujo de texto, aproximadamente páginas 14 a 29 del teórico.

### Qué se explicó sobre imports y qué conviene precisar

El docente compara importar un módulo con incorporar un nombre concreto y advierte sobre cadenas de dependencias. La recomendación de organizar los archivos y conocer sus dependencias es útil. Sin embargo, **usar `from modulo import funcion` no evita por sí mismo cargar e inicializar ese módulo**. Ambas formas ejecutan sus instrucciones de nivel superior en la primera importación normal, incluidos sus imports. Cambia qué nombres quedan disponibles en el archivo que importa.

Si un import está dentro del cuerpo de una función, se ejecuta cuando la ejecución llega a esa instrucción al llamar a la función. Importar la función no ejecuta su cuerpo ni analiza sus dependencias para traer únicamente lo que va a necesitar. Esta diferencia depende de dónde está escrito el import, no de elegir `from`.

Los módulos normalmente se reutilizan desde una caché durante la misma ejecución. Por eso un import circular no significa necesariamente un bucle infinito: puede fallar al intentar usar un nombre de un módulo que todavía se está inicializando. Para estos ejercicios, conviene evitar ciclos y trasladar lo compartido a un tercer archivo. [Sistema de imports de Python](https://docs.python.org/3/reference/import.html).

### Qué significa `if __name__ == "__main__"`

El docente usa la idea de «arrancar por acá» para distinguir ejecución e importación. La precisión es que Python sigue ejecutando el archivo de arriba hacia abajo: esa condición no lo hace saltar a un punto de entrada.

```python
def saludar():
    """Muestra un saludo."""
    print("Hola")

if __name__ == "__main__":
    saludar()
```

Al ejecutar directamente ese archivo, la condición es verdadera y se llama a `saludar`. Al importarlo normalmente, el nombre es el del módulo y ese bloque se omite. Las instrucciones que estén fuera del bloque siguen ejecutándose durante la importación.

**No existe una regla que permita escribir ese bloque una sola vez en todo el proyecto.** Varios módulos pueden tenerlo para sus propias pruebas; incluso es válido tener más de uno en un archivo, aunque normalmente se agrupa el arranque en uno. Un mismo archivo puede servir como módulo importable y como programa ejecutable. [Python: entorno `__main__`](https://docs.python.org/3/library/__main__.html).

### Reglas de organización recordadas en clase

- Agrupar los imports al comienzo como convención de organización.
- Evitar dependencias circulares entre archivos.
- Usar nombres de archivo claros, sin espacios, y no ocultar bibliotecas con nombres como `random.py`, `json.py`, `math.py` o `pygame.py`.
- El docente propone un prefijo propio como posibilidad; no se registra un prefijo obligatorio.

### Instalar pygame y abrir una ventana

pygame se instala desde una terminal, incluida la integrada en VS Code. No es una extensión de VS Code: es una biblioteca de Python que se instala con pip. Además del dibujo, ofrece recursos para eventos, teclado, mouse, sonido y tiempo; la descripción oral se concentra aquí en el dibujo.

```powershell
python -m pip install pygame
```

El ejemplo mínimo del docente abre una ventana, espera dos segundos y termina:

```python
import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primera ventana")
pygame.time.wait(2000)
pygame.quit()
```

No tiene un bucle que atienda los eventos. Durante la espera no procesa normalmente el cierre ni las interacciones. Que el sistema la marque como no respondiente depende del sistema y del tiempo sin atender eventos; no es una consecuencia segura de que sea negra o dure dos segundos.

### El bucle: escuchar, actualizar, dibujar y limitar el ritmo

En cada vuelta se recogen eventos, se modifica el estado según la lógica y los inputs, se dibuja la escena y se limita la frecuencia. El estado también puede cambiar sin input: el círculo de `rebote.py` se mueve solo.

La comparación con la doble exposición fotográfica ayuda a entender los rastros, pero en un tramo de la explicación oral se intercambian los nombres:

| Instrucción | Responsabilidad |
|---|---|
| `pantalla.fill(color)` | Rellena la superficie; usado al inicio del dibujo, tapa la imagen anterior. |
| `pygame.draw.circle(...)` y otras figuras | Dibujan el estado de esta vuelta sobre la superficie. |
| `pygame.display.flip()` | Actualiza la pantalla completa con lo dibujado; no limpia el fondo. |
| `reloj.tick(60)` | Limita aproximadamente a un máximo de 60 vueltas por segundo. |

Fuentes: [pygame: fill](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill) y [pygame: flip](https://www.pygame.org/docs/ref/display.html#pygame.display.flip). Esta separación coincide con las páginas 24 y 25 del teórico.

### Dibujar figuras y texto

El origen `(0, 0)` está en la esquina superior izquierda; x crece hacia la derecha e y hacia abajo. Se muestran rectángulos, círculos, líneas y contornos. Un contorno se obtiene indicando un grosor en la función correspondiente; no es una figura nueva llamada «hueco».

Para el texto, la página 29 usa tres pasos:

```python
# Después de pygame.init(), antes del bucle:
fuente = pygame.font.SysFont("Arial", 32)

# Dentro del bucle, después de fill() y antes de flip():
imagen = fuente.render("Puntos: 7", True, (182, 255, 63))
pantalla.blit(imagen, (20, 20))
```

`render` convierte el texto en una superficie; `True` pide suavizar los bordes. `blit` la dibuja en la posición indicada: `(20, 20)` ubica la esquina superior izquierda de esa imagen a 20 píxeles de ambos bordes. El texto puede colocarse en otras posiciones. La fuente se crea una sola vez y se reutiliza.

## 11. Registro de clase: interacción y comienzo del práctico

Fuente: siguiente fragmento de transcripción del 18/9/2026; corresponde a teclado, mouse, colisiones, bordes y organización del juego, temas de las páginas 32 a 44 del teórico.

### Teclado: una acción o movimiento continuo

El docente explica que el input cambia el estado: mover un objeto, modificar su velocidad o ejecutar otra acción. Hay que distinguir una pulsación del estado de una tecla mantenida.

- `KEYDOWN` permite reaccionar al presionar una tecla, por ejemplo cambiar el color o borrar la pantalla.
- `pygame.key.get_pressed()` consulta cuáles están presionadas ahora y sirve para movimiento continuo. No entrega un historial de teclas pulsadas.

En la configuración inicial de pygame la repetición de teclas está desactivada; si se activa explícitamente con `set_repeat`, pueden generarse varios eventos `KEYDOWN` al mantener una tecla. Los ejercicios no activan esa opción. [Referencia de teclado](https://www.pygame.org/docs/ref/key.html).

### Mouse y dibujos persistentes

Se menciona `MOUSEBUTTONDOWN`: técnicamente es un tipo de evento, no una función. Se obtiene al recorrer `pygame.event.get()` y su atributo `pos` indica dónde ocurrió el clic.

El ejemplo oral coincide con el ejercicio 5.3: cada clic agrega un círculo, los anteriores permanecen y Espacio borra todos para empezar de nuevo. La lista guarda los datos y se redibuja después de limpiar el fondo. Nuestra solución está en [pintar.py](pintar.py), que además conserva un color de la paleta para cada círculo.

### Clic sobre un objeto y colisiones

Para un objeto representado por un rectángulo, podemos comprobar si el clic cayó dentro:

```python
# Dentro del bucle de eventos, con boton definido antes como pygame.Rect:
if evento.type == pygame.MOUSEBUTTONDOWN:
    if boton.collidepoint(evento.pos):
        print("Clic dentro del botón")
```

`collidepoint` comprueba un punto contra un rectángulo; `colliderect` comprueba la superposición de dos rectángulos. No detectan automáticamente la forma exacta de cualquier dibujo. En Rect, tocar solamente los bordes exteriores entre dos rectángulos no cuenta como superposición. [Referencia de Rect](https://www.pygame.org/docs/ref/rect.html).

### Respetar los bordes

El docente propone detener o hacer rebotar un objeto al llegar al límite de la ventana. Se actualiza su posición, se comprueban y corrigen los límites y después se dibuja. Para un círculo se contempla el radio; para un rectángulo, sus bordes. En el rebote cambia el signo de la velocidad del eje correspondiente. Esto está aplicado en [rebote.py](rebote.py).

### Del ejemplo corto a varios módulos

El docente vuelve a separar el juego por responsabilidades: constantes en `ajustes.py`, jugador en `jugador.py`, funciones auxiliares en `utiles.py` y arranque y bucle en `main.py`, que importa los demás.

Anuncia una demostración de un juego de nave y disparos identificado en la conversación como **Space Invaders**. En este fragmento todavía no muestra el código ni los prompts de esa demostración. No debe confundirse con el ejemplo del PDF, donde un jugador recoge una moneda, ni registrarse como una nueva consigna obligatoria.

### Trabajo indicado en este momento

Mientras prepara su computadora y la pantalla, el docente pide comenzar el práctico. Los tres ejercicios ya preparados son:

| Ejercicio | Archivo | Qué comprobar al ejecutarlo |
|---|---|---|
| 5.1 | [fondo.py](fondo.py) | R/V/A cambian el fondo y el color permanece al soltar la tecla. |
| 5.2 | [rebote.py](rebote.py) | El círculo rebota en los cuatro lados sin salirse. |
| 5.3 | [pintar.py](pintar.py) | Los clics agregan círculos, permanecen y Espacio los borra. |

Se permite apoyarse en ChatGPT, Copilot o Claude para generar y corregir código. La indicación es experimentar, ejecutar y observar los resultados. Sigue vigente la condición del material docente de comprender el código o escribir comentarios propios.

Después del práctico se anuncia trabajar sobre prompts, ajustes sucesivos y errores del juego. Esa parte queda pendiente de los próximos fragmentos: todavía no hay un prompt concreto ni un error de la demostración para documentar.
