"""10.2 de referencia. Espacio: congelar/descongelar; q: salir."""
import cv2

cap = cv2.VideoCapture(0)
congelado = False  # Se conserva entre vueltas.
ultimo = None
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    while True:
        if not congelado:
            ok, frame = cap.read()
            if not ok:
                break
            ultimo = cv2.flip(frame, 1)
        # Se dibuja en la copia: ultimo permanece limpio.
        vista = ultimo.copy()
        if congelado:
            cv2.putText(vista, "CONGELADO", (12, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow("10.2 - Espacio y q", vista)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord("q"):
            break
        if tecla == ord(" "):
            congelado = not congelado
finally:
    cap.release()
    cv2.destroyAllWindows()
