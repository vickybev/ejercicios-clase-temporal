"""Funciones de referencia: reciben una imagen y devuelven una imagen."""
import cv2

def cargar(ruta):
    """Carga una imagen o informa si no pudo leerla."""
    img = cv2.imread(str(ruta))
    if img is None:
        raise FileNotFoundError(f"No pude leer {ruta}")
    return img

def miniatura(img, ancho=320):
    """Redimensiona conservando la proporción de la imagen."""
    alto_original, ancho_original = img.shape[:2]
    alto = max(1, int(alto_original * ancho / ancho_original))
    return cv2.resize(img, (ancho, alto))

def sin_filtro(img):
    """Devuelve la imagen recibida."""
    return img

def a_gris(img):
    """Convierte los tres canales BGR a intensidad gris."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def desenfocar(img):
    """Suaviza usando un vecindario positivo e impar."""
    return cv2.GaussianBlur(img, (21, 21), 0)

def bordes(img):
    """Encuentra cambios fuertes de intensidad."""
    return cv2.Canny(a_gris(img), 100, 200)

def umbral(img):
    """Separa intensidades en negro y blanco con corte 127."""
    _, bn = cv2.threshold(a_gris(img), 127, 255, cv2.THRESH_BINARY)
    return bn

def invertir(img):
    """Calcula el negativo sobre toda la tabla, sin bucles de píxeles."""
    return 255 - img

def lapiz(img):
    """Combina cuatro pasos para simular un dibujo a lápiz."""
    gris = a_gris(img)  # 1. Intensidad en vez de color.
    negativo = 255 - gris  # 2. Invertir intensidad.
    borroso = cv2.GaussianBlur(negativo, (21, 21), 0)  # 3. Suavizar.
    return cv2.divide(gris, 255 - borroso, scale=256.0)  # 4. Combinar.

def a_color(img):
    """Normaliza a tres canales; no recupera colores perdidos."""
    if len(img.shape) == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img
