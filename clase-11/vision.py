"""Referencia para API clásica MediaPipe 0.10.21: BGR entra, (x,y) o None sale."""
import cv2
import mediapipe as mp

COLOR_MIN = (5, 120, 120)  # Valores iniciales para naranja; calibralos.
COLOR_MAX = (20, 255, 255)
clasificador = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
if clasificador.empty():
    raise RuntimeError("No se pudo cargar el XML del detector de caras")
if not hasattr(mp, "solutions"):
    raise RuntimeError("Este ejemplo necesita MediaPipe clasico 0.10.21; revisa la guia")
manos = mp.solutions.hands.Hands(
    max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5
)

def detectar_color(frame):
    """Devuelve el centro de la caja de la mancha más grande, o None."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, COLOR_MIN, COLOR_MAX)
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contornos) == 0:
        return None
    grande = max(contornos, key=cv2.contourArea)
    if cv2.contourArea(grande) < 500:
        return None
    x, y, w, h = cv2.boundingRect(grande)
    return (x + w // 2, y + h // 2)

def detectar_cara(frame):
    """Devuelve el centro de la primera cara encontrada, o None."""
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    caras = clasificador.detectMultiScale(gris, 1.1, 5, minSize=(80, 80))
    if len(caras) == 0:
        return None
    x, y, w, h = caras[0]
    return (int(x + w // 2), int(y + h // 2))

def detectar_mano(frame):
    """Devuelve la punta del índice de la primera mano, o None."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = manos.process(rgb)
    if not resultado.multi_hand_landmarks:
        return None
    punta = resultado.multi_hand_landmarks[0].landmark[8]
    alto, ancho = frame.shape[:2]
    return (int(punta.x * ancho), int(punta.y * alto))

def cerrar():
    """Libera el detector de manos cuando termina el programa principal."""
    manos.close()
