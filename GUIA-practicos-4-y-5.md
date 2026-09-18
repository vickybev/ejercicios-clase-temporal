# Prácticos 4 y 5: soluciones explicadas

Material recibido el 18/9/2026. La clase 4 corresponde a la clase pasada; la clase 5 es la de hoy, viernes 18/9/2026. Esta guía reúne el práctico pendiente de la clase 4 y el material de la clase 5.

Teóricos incorporados posteriormente: [clase 4: funciones, datos y objetos](clase-04/TEORIA.md) y [clase 5: carpetas y pygame](clase-05/TEORIA.md). Se contrastaron los ejercicios con ambos y se agregaron las 39 docstrings que pide la clase 4. Los apuntes separan el contenido docente de las precisiones verificadas.

## Material docente y decisiones de esta solución

- Clase 4: `C:\Users\Vicky\Documents\PROGRAMACION 2\clase4_practico.pptx`, 18 diapositivas.
- Clase 5: `C:\Users\Vicky\Documents\PROGRAMACION 2\clase5_practico.pdf`, 8 páginas físicas. Su numeración impresa salta de 4 a 9; los ejercicios están en las páginas físicas 5 a 7.
- Teóricos: `clase4_teoria.pptx` (42 diapositivas) y `clase5_teoria.pdf` (44 páginas), en la misma carpeta docente.
- La consigna pide una carpeta por clase, un archivo por ejercicio, commits descriptivos y push antes de la clase siguiente.
- Se permite IA, pero hay que entender y poder explicar el código, o escribir comentarios propios a mano. Los comentarios incluidos acá son explicaciones de apoyo: no sustituyen tus comentarios personales.
- Se usan funciones, clases, listas, diccionarios, bucles y condiciones. En el práctico 5 se agregan `pygame` y `random`, presentes en la consigna. No se usan comprensiones, herencia ni decoradores.
- **Catálogo:** la diapositiva 5 pide que `catalogo.py` evolucione en dos etapas, pero las diapositivas 8 y 9 nombran `catalogo_poo.py`. Conservamos A en `catalogo.py` y B en `catalogo_poo.py` para compararlas. Si el docente exige un único archivo final, la versión B es la que debe quedar como `catalogo.py`.
- **Año de referencia:** `Obra.antiguedad()` usa 2026, explícitamente, sin importar una biblioteca nueva. No se actualiza sola al cambiar de año.
- **Entradas numéricas:** el catálogo y el validador esperan números en el formato pedido. El validador controla el intervalo, no letras ni decimales. El catálogo no agrega reglas de validación de precio/año que no están en su consigna.
- **Color:** el encabezado docente dice que dos métodos usan al primero; según las definiciones concretas, `es_claro()` usa `luminosidad()`, mientras `hex()` usa directamente r, g y b. Seguimos esas definiciones.
- **Consumo:** añadimos el rechazo de cantidades cero o negativas para evitar que restar un negativo aumente el stock. Se trabaja con cantidades enteras de materiales.

## Cómo ejecutarlos

Abrí la carpeta del ejercicio en VS Code y ejecutá su archivo con Python, o usá la terminal desde la raíz de este repositorio:

```powershell
python .\clase-04\geometria.py
python .\clase-04\catalogo.py
```

Si tu Windows usa `py` en lugar de `python`, reemplazá ese comando. Para pygame, instalá la dependencia en el mismo Python con el que vas a ejecutarlo:

```powershell
python -m pip install pygame==2.6.1
python .\clase-05\fondo.py
python .\clase-05\rebote.py
python .\clase-05\pintar.py
```

Ejecutá una ventana por vez y cerrala con la X antes de abrir la siguiente. No son programas para abrir en el navegador. La instalación usada por las pruebas del asistente está en `tmp/pygame-runtime`, fuera del repositorio; tu intérprete de VS Code puede necesitar la instalación anterior.

## Base para entender el práctico 4

Una **función** tiene nombre, recibe datos mediante parámetros y puede devolver un resultado con `return`. Por ejemplo, `area_rectangulo(6, 3)` devuelve 18. `print()` muestra algo en pantalla; no reemplaza el resultado que otra parte del programa necesita recibir.

Una **lista** guarda varios elementos ordenados. Un **diccionario** relaciona claves con valores: en `obra["precio"]`, la clave es `"precio"`. Una **clase** define cómo se crean objetos y qué acciones pueden realizar. Un objeto `obra` guarda su precio como `obra.precio` y puede ejecutar `obra.ficha()`.

`__init__` asigna los datos iniciales. `self` representa el objeto particular que está recibiendo la llamada. En `material.consumir(2)`, `self.stock` es el stock de ese material, no el de todos.

### Catálogo: etapas A y B

1. `agregar_obra` pide cuatro datos y agrega un diccionario u objeto a la lista. No necesita devolver la lista: está modificando la que recibió.
2. `listar_obras` imprime las fichas numeradas; si la lista está vacía, lo informa.
3. `buscar_por_autor` arma y retorna una lista de coincidencias. La comparación ignora mayúsculas y espacios exteriores, pero no elimina acentos.
4. `estadisticas` retorna un diccionario con cantidad, suma de precios y promedio. Con cero obras, total y promedio son cero.
5. El menú conecta esas funciones. En la etapa B, las funciones consultan atributos en lugar de claves.

La etapa A empieza vacía. La B tiene tres ejemplos: 1500 + 3200 + 900 = **5600**, promedio **1866,67**. Buscar Pérez devuelve dos obras. `es_cara()` usa `>`: una obra de 2000 no supera el límite 2000. La antigüedad de una obra de 2020 es 6 años con la referencia 2026.

**Probá:** listar antes de agregar, buscar un autor que no existe, agregar una obra, listar y consultar estadísticas. En la B, buscá Pérez y comprobá que el menú sigue funcionando.

### 4.1 — geometria.py

Área = ancho × alto; perímetro = 2 × (ancho + alto). `describir()` llama a las otras dos funciones y retorna un texto. La impresión ocurre fuera de ella.

| Medidas | Área | Perímetro | Orientación |
|---|---:|---:|---|
| 6 × 3 | 18 | 18 | horizontal |
| 3 × 6 | 18 | 18 | vertical |
| 4 × 4 | 16 | 16 | cuadrado |

**Para explicar:** si `describir()` solo imprimiera, no podrías guardar su descripción como resultado de la llamada.

### 4.2 — validador.py

`anio_valido()` devuelve un booleano: `True` o `False`. Los límites 1800 y 2026 están incluidos. `pedir_anio()` repite el pedido; un `return` termina la función completa y, por lo tanto, también deja de repetir su bucle.

**Probá:** 1799 → rechazo; 2027 → rechazo; 2020 → aceptación. También deben aceptarse 1800 y 2026. Ingresá enteros, como solicita el programa.

### 4.3 — inventario.py

`hay_stock` comprueba primero que el material exista. El `and` no evalúa el acceso al diccionario si esa primera condición es falsa. Así, preguntar por pegamento devuelve `False` sin intentar leer una clave inexistente.

`faltantes` devuelve nombres con cantidad estrictamente menor al mínimo. Con mínimo 5: **tinta color y cinta**. `total_unidades` acumula **176**. Papel tiene stock; cinta no.

### 4.4 — estadisticas.py

Para buscar la obra más cara, guardamos una candidata y la reemplazamos cuando encontramos una de precio mayor. Para no repetir autores, comprobamos si el nombre ya está en la lista.

El patrón de contar empieza un autor en cero y suma uno por cada obra suya. Resultado: **Pérez: 2, Gómez: 2, Díaz: 1**. La obra más cara es **Paisaje, 4100**. Después de 2020 quedan **Retrato y Estudio**; 2020 no se incluye.

Con una lista vacía, `obra_mas_cara` retorna `None`, los filtros retornan listas vacías y el conteo retorna un diccionario vacío. En un empate de precio se conserva la primera obra encontrada.

### 4.5 — color_poo.py

`luminosidad()` aplica la fórmula docente. `es_claro()` compara el resultado con 128. `hex()` convierte cada componente a dos dígitos hexadecimales mediante `02X`: por ejemplo, 255 se escribe FF y 0 se escribe 00.

Resultados: **Blanco #FFFFFF claro; Negro #000000 oscuro; Rojo #FF0000 oscuro; Amarillo #FFFF00 claro**. Se supone que los componentes están entre 0 y 255. Esta es la clasificación simplificada de la consigna, no una comprobación de accesibilidad del contraste.

### 4.6 — material.py

`valor_total()` multiplica precio unitario por stock. `hay_stock()` pregunta si queda al menos una unidad. `consumir()` cambia el atributo `stock` únicamente si puede descontar la cantidad solicitada.

Papel empieza con 120 y queda en **118** después de consumir 2. Tinta empieza con 3 y queda en **1**. Intentar consumir 999 devuelve `False` y deja ambas cantidades iguales. Consumir exactamente lo disponible es válido y deja cero.

### 4.7 — integrador.py

La clase Material se repite con la misma definición para que el archivo funcione solo y conserve el alcance de la clase 4. El teórico 5 recién incorporado sí enseña importaciones entre archivos y `if __name__ == "__main__"`: permiten reutilizarla sin ejecutar sus pruebas al importar. Las tres funciones siguientes están fuera de la clase y recorren una lista de cinco objetos.

- Valor del inventario: 120 × 10 + 8 × 450 + 0 × 600 + 45 × 30 + 0 × 80 = **6150**.
- Sin stock: **Tinta color y Cinta**.
- Mayor precio unitario: **Tinta color, 600**, aunque esté agotada. La consigna pide comparar el precio unitario, no el valor del stock.

Con una lista vacía: valor cero, lista de agotados vacía y `mas_caro()` devuelve `None`.

## Base para entender el práctico 5

Cada vuelta del bucle sigue esta secuencia: **leer eventos → actualizar datos → limpiar y dibujar → mostrar**. `fill()` limpia el dibujo anterior. `flip()` muestra lo que acabamos de dibujar. `reloj.tick(60)` limita el bucle a un máximo aproximado de 60 vueltas por segundo; no garantiza 60 en una computadora lenta.

Las coordenadas parten de la esquina superior izquierda: x aumenta hacia la derecha e y hacia abajo. Los colores RGB son tres números entre 0 y 255.

### 5.1 — fondo.py

La ventana es de 600 × 400. R asigna rojo a `color`, V asigna verde y A asigna azul. Se usa `KEYDOWN`, como exige la consigna. Al soltar la tecla, nadie cambia esa variable, por eso el fondo permanece. Una tecla distinta no ejecuta ninguna asignación.

**Probá:** R y soltar; otra tecla; V y soltar; A y soltar; cerrar con X. El último color debe permanecer en cada caso.

### 5.2 — rebote.py

El centro empieza en (300, 200). En cada vuelta se suman 3 a x y 2 a y. Una velocidad positiva avanza hacia derecha/abajo; una negativa, hacia izquierda/arriba.

Con radio 20, el centro debe quedar entre **20 y 580** horizontalmente y entre **20 y 380** verticalmente. Cuando llega a un borde, corregimos la posición y negamos la velocidad de ese eje. Horizontal y vertical se comprueban por separado para poder rebotar en ambos ejes en una esquina.

**Probá:** dejalo recorrer los cuatro bordes. El círculo entero debe permanecer dentro, sin dejar rastros.

### 5.3 — pintar.py

Cada clic guarda posición y color en un diccionario dentro de `circulos`. `random.choice(paleta)` elige entre cuatro colores una sola vez al crear el círculo. No se vuelve a elegir al dibujar: así cada círculo conserva su color.

Después de limpiar la ventana, el `for` dibuja todos los círculos guardados. Espacio reemplaza la lista por una vacía. Se aceptan los botones izquierdo, central y derecho; los eventos de la rueda no agregan dibujos.

**Probá:** clic en varios lugares, esperar, presionar otra tecla, borrar con Espacio y volver a pintar. La X debe cerrar.

## Referencias externas verificadas

Estas referencias amplían las explicaciones; las consignas provienen de los dos archivos docentes indicados al comienzo.

- [Python: clases, objetos y atributos](https://docs.python.org/3/tutorial/classes.html).
- [pygame: cola de eventos, KEYDOWN, QUIT y eventos de mouse](https://www.pygame.org/docs/ref/event.html).
- [pygame: reloj y límite de fotogramas](https://www.pygame.org/docs/ref/time.html).

## Verificación realizada

Se ejecutaron los nueve archivos de la clase 4 y se comprobaron retornos, límites de años, listas vacías, autores ausentes, conteos, formato hexadecimal, consumo exacto y rechazo de consumo excesivo o no positivo.

Los tres programas de pygame se probaron con pygame 2.6.1 real y un controlador de video virtual (SDL dummy). Se inyectaron eventos de teclado, clic y cierre; se comprobaron los píxeles dibujados y se revisaron imágenes de los tres programas. El rebote se comprobó durante 1200 fotogramas y en un escenario adicional de choque simultáneo en una esquina.

Todas esas comprobaciones pasaron. No se operaron ventanas nativas con el teclado y el mouse físicos: esa comprobación manual queda indicada a continuación.

## Antes de entregar

- Ejecutar los archivos y practicar las comprobaciones de esta guía.
- Poder explicar qué recibe, qué devuelve y qué modifica cada función o método.
- Resolver con el docente la diferencia de nombres del catálogo si exige un solo archivo.
- Los commits locales y el push son pasos distintos: comprobar la publicación antes de dar la entrega por enviada.
