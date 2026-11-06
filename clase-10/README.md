# Clase 10: cámara, filtros y ventana de Pygame

## Qué estamos aprendiendo

Un video se procesa un cuadro por vez. `cv2.VideoCapture(0)` abre la primera
cámara. `ok, frame = cap.read()` devuelve si pudo leerla y la imagen recibida.
Comprobamos `ok` antes de usar `frame`; `cv2.flip(frame, 1)` lo espeja.
Al terminar, `cap.release()` libera la cámara.

## Preparación en Windows

Abrí la carpeta **ejercicios-clase** en VS Code y una terminal PowerShell.
Estas órdenes se ejecutan desde esa carpeta, no desde clase-10:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r clase-10\requirements.txt
.\.venv\Scripts\python.exe -m pip check
```

Si el entorno ya está creado, no hace falta volver a crearlo. La propuesta usa
Python 3.12 de 64 bits. El requirements es el entorno de trabajo elegido para
estos ejercicios; no fue proporcionado por el docente.

En VS Code: Ctrl+Shift+P > Python: Select Interpreter >
`.venv\Scripts\python.exe`. No hace falta activar el entorno para ejecutar
las órdenes con su ruta completa.

## Primera prueba: cámara

```powershell
.\.venv\Scripts\python.exe clase-10\camara.py
```

1. Revisá que aparezca una imagen en movimiento.
2. Levantá una mano: la imagen debe comportarse como un espejo.
3. Seleccioná la ventana y presioná **q**.
4. Volvé a ejecutar para comprobar que se liberó la cámara.

`camara.py` es una prueba previa, no un ejercicio adicional pedido por el curso.
No guarda fotos ni envía video a Internet.

## Práctico: espejo con filtros

```powershell
.\.venv\Scripts\python.exe clase-10\espejo.py
```

Las teclas 1 a 6 eligen normal, gris, desenfoque, bordes, umbral e invertir.
7 agrega lápiz; **s** guarda una captura con fecha y hora; **q** termina.
El práctico menciona seis filtros pero enumera siete opciones contando normal:
usamos 7 para conservar todas las transformaciones y dejamos documentada esa
decisión. Las capturas personales se excluyen de Git.

`filtros.py` procesa imágenes; `espejo.py` administra cámara y teclado.
`a_color()` convierte una imagen gris a tres canales para poder dibujar texto
en color; no recupera los colores originales. El diccionario guarda funciones
sin paréntesis; `aplicar(frame)` ejecuta la elegida sobre la imagen actual.

Pruebas manuales: recorrer todas las teclas, comprobar que el filtro se mantiene
al soltar, guardar con s y abrir el PNG para comprobar su contenido. Cerrá con q.

## Ejercicio 10.1: la cámara dentro de Pygame

```powershell
.\.venv\Scripts\python.exe clase-10\ventana.py
```

1. `pygame.init()` prepara la biblioteca y `set_mode` crea la ventana.
2. `pygame.event.get()` lee teclas y la X. Aquí ya no usamos `waitKey`.
3. OpenCV sigue leyendo, espejando y filtrando cada cuadro.
4. `a_color()` asegura tres canales; `frombuffer` convierte los bytes BGR en
   una superficie de Pygame con el ancho y alto correspondientes.
5. `blit` dibuja el video y después el nombre. Si invertimos el orden, el video
   tapa el texto.
6. `pygame.display.flip()` presenta el dibujo y `tick(30)` limita el ritmo.
   Este flip no espeja: el espejo lo hace `cv2.flip(frame, 1)`.
7. Al cerrar con X o Escape liberamos cámara y Pygame.

Probá 1 a 7, especialmente Gris, Bordes y Lápiz: tienen que verse sin error
de canales. Cerrá con la X y abrí de nuevo para comprobar la liberación.

## Git: por qué hacemos commits separados

Un commit registra un cambio local con un mensaje; push lo envía a GitHub.
Después de probar el práctico:

```powershell
git status
git add clase-10/filtros.py clase-10/espejo.py
git commit -m "Clase 10: agregar espejo de camara con filtros y capturas"
git push origin main
```

No uses `git add .` sin revisar: puede incluir cambios de otras clases.
El entorno `.venv`, las cachés y las fotos personales no van en los commits.
La prueba de cámara y el entorno llevan su propio commit de preparación;
cada ejercicio 10.1, 10.2 y 10.3 tendrá un commit aparte cuando se incorpore.

## Si algo falla

- `ModuleNotFoundError`: usá el Python de `.venv`, el mismo de la instalación.
- No abre la cámara: cerrá otras aplicaciones de cámara, revisá sus permisos
  en Windows y comprobá el índice 0 o 1 según las cámaras conectadas.
- No toma teclas: hacé clic en la ventana de video para darle foco.
- No uses `waitKey(0)` dentro del video: lo detiene hasta recibir una tecla.
- Leé el archivo y la línea del traceback antes de cambiar bibliotecas.

Guía completa y materiales originales en el
[seguimiento del curso](https://programacion-2-vicky.vibe-design.chatgpt.site/#clase-10).
