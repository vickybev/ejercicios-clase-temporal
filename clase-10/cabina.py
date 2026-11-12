"""10.3 de referencia. Espacio: cuatro fotos; q: salir. Guarda tira.png."""
import math
from pathlib import Path
import time
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fotos = []
activa = False
inicio = 0.0
ventana = "10.3 - Espacio: iniciar | Q o Esc: salir"
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        vista = frame.copy()  # La cuenta no contamina las fotos.
        if activa:
            transcurrido = time.time() - inicio
            if transcurrido >= 3:
                fotos.append(frame.copy())
                print("Foto", len(fotos), "de 4")
                inicio = time.time()
                if len(fotos) == 4:
                    tira = np.full((960, 320, 3), 255, dtype=np.uint8)
                    for i, foto in enumerate(fotos):
                        tira[i * 240:(i + 1) * 240, 0:320] = cv2.resize(foto, (320, 240))
                    ruta = Path(__file__).with_name("tira.png")
                    print("Guardada" if cv2.imwrite(str(ruta), tira) else "Error al guardar", ruta)
                    activa = False
            if activa:
                numero = max(1, math.ceil(3 - (time.time() - inicio)))
                cv2.putText(vista, str(numero), (50, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 5)
        cv2.imshow(ventana, vista)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla in (ord("q"), ord("Q"), 27):
            break
        try:
            visible = cv2.getWindowProperty(ventana, cv2.WND_PROP_VISIBLE)
        except cv2.error:
            break
        if visible < 1:
            break
        if tecla == ord(" ") and not activa:
            fotos = []
            inicio = time.time()
            activa = True
finally:
    cap.release()
    cv2.destroyAllWindows()
