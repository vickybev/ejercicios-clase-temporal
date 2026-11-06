"""Prueba previa: cámara espejada. Seleccioná su ventana y apretá q para salir."""
import cv2

cap = cv2.VideoCapture(0)  # 0: primera cámara; 1: otra si existe.
try:
    if not cap.isOpened():
        raise RuntimeError("No abre la camara: revisa permisos, indice y otras apps.")
    print("Camara abierta. Hace clic en su ventana y apreta q para salir.", flush=True)
    cuadros = 0
    while True:
        ok, frame = cap.read()  # Booleano de éxito e imagen.
        if not ok:
            print("No llego un cuadro; termino la captura.")
            break
        cuadros += 1
        if cuadros == 1:
            print("Primer cuadro (alto, ancho, canales):", frame.shape, flush=True)
        frame = cv2.flip(frame, 1)  # Espejo horizontal.
        cv2.imshow("Camara - q para salir", frame)
        tecla = cv2.waitKey(1) & 0xFF  # Una lectura por vuelta.
        if tecla == ord("q"):
            break
finally:  # También libera los recursos si falla el bloque anterior.
    cap.release()
    cv2.destroyAllWindows()
    print("Camara liberada y ventanas cerradas.", flush=True)
