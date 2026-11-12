# Clase 11: detectar e interactuar con la cámara

Usá el entorno de la [clase 10](../clase-10/README.md). Desde la raíz de
`ejercicios-clase`, podés repetir la instalación verificada con:

```powershell
.\.venv\Scripts\python.exe -m pip install -r clase-10\requirements-lock.txt
```

Cada detector de `vision.py` recibe el mismo cuadro BGR espejado. Devuelve una
posición `(x, y)` si encuentra el objetivo o `None` si no. Pygame dibuja el
video primero y el círculo encima. **X** o **Escape** cierran los programas.

| Programa | Cómo probarlo | Qué estás aprendiendo |
| --- | --- | --- |
| `reacciona.py` | **1** color, **2** cara, **3** mano. Mostrá y retirá cada objetivo. | El diccionario guarda funciones; las tres comparten el mismo contrato. |
| `calibrar.py` | Hacé clic en una zona del objeto; **m** muestra la máscara. Copiá el rango impreso a `vision.py` cuando el objeto se separe del fondo. | Un clic es `(x,y)`, pero una imagen se indexa `[y,x]`. |
| `estela.py` | Mové el índice; **b** borra todo el dibujo. | Un lienzo transparente conserva el trazo hasta borrarlo. |
| `boton.py` | Dejá el índice dentro del rectángulo hasta completar la barra. Sacalo y volvé a entrar. | Un contador mide cuadros dentro; una bandera evita repetir el clic hasta salir. |

```powershell
.\.venv\Scripts\python.exe clase-11\reacciona.py
# Cerrá la ventana antes de abrir el siguiente programa.
.\.venv\Scripts\python.exe clase-11\calibrar.py
.\.venv\Scripts\python.exe clase-11\estela.py
.\.venv\Scripts\python.exe clase-11\boton.py
```

Empezá con un objeto naranja sobre fondo neutro. Los valores iniciales son
orientativos: calibrá con tu luz. El botón cuenta treinta cuadros, cerca de
un segundo si se procesan a 30 FPS; puede demorar más si el detector va lento.

Las pruebas en vivo confirmaron la calibración con una botella naranja, la
detección de cara e índice y el botón por permanencia. La distancia y el
contraluz pueden dificultar el seguimiento de la mano.
La estela original de cuarenta puntos se amplió a pedido para conservar el dibujo
hasta presionar B. Al perder la detección, el siguiente punto inicia otro trazo.
El calibrador muestra el punto del clic y el color elegido antes de activar M.
La [guía del curso](https://programacion-2-vicky.vibe-design.chatgpt.site/#clase-11)
explica cada bloque y sus errores frecuentes.
