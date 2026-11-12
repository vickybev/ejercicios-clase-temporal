"""10.2 de referencia. Espacio congela. Q, Esc o la cruz cierran."""
import cv2

cap = cv2.VideoCapture(0)
congelado = False  # Se conserva entre vueltas.
ultimo = None
ventana = "10.2 - Espacio: congelar | Q o Esc: salir"
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
        cv2.imshow(ventana, vista)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla in (ord("q"), ord("Q"), 27):
            break
        try:
            visible = cv2.getWindowProperty(ventana, cv2.WND_PROP_VISIBLE)
        except cv2.error:
            # Al cerrar con la cruz, Windows puede destruir la ventana de inmediato.
            break
        if visible < 1:
            break
        if tecla == ord(" "):
            congelado = not congelado
finally:
    cap.release()
    cv2.destroyAllWindows()
