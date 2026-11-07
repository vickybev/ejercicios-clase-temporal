"""Práctico de referencia. 1..7: filtros; s: captura; q: salir."""
from datetime import datetime
from pathlib import Path
import cv2
import filtros

# La consigna enumera siete opciones contando normal: ver aclaración en la guía.
FILTROS = {
    ord("1"): ("Normal", filtros.sin_filtro),
    ord("2"): ("Gris", filtros.a_gris),
    ord("3"): ("Desenfoque", filtros.desenfocar),
    ord("4"): ("Bordes", filtros.bordes),
    ord("5"): ("Umbral", filtros.umbral),
    ord("6"): ("Invertir", filtros.invertir),
    ord("7"): ("Lapiz", filtros.lapiz),
}
nombre, aplicar = FILTROS[ord("1")]
cap = cv2.VideoCapture(0)
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        salida = filtros.a_color(aplicar(frame)).copy()
        cv2.putText(salida, nombre, (12, 32), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2)
        cv2.imshow("Espejo - 1..7, s, q", salida)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord("q"):
            break
        if tecla in FILTROS:
            nombre, aplicar = FILTROS[tecla]
        elif tecla == ord("s"):
            ruta = Path(__file__).with_name(datetime.now().strftime("captura_%Y%m%d_%H%M%S_%f.png"))
            print("Guardada" if cv2.imwrite(str(ruta), salida) else "No pude guardar", ruta)
finally:
    cap.release()
    cv2.destroyAllWindows()
