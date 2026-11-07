"""Práctico: 1 color, 2 cara, 3 mano. X o Escape para salir."""
import cv2
import pygame
import vision

DETECTORES = {
    pygame.K_1: ("Color", vision.detectar_color),
    pygame.K_2: ("Cara", vision.detectar_cara),
    pygame.K_3: ("Mano", vision.detectar_mano),
}
pygame.init()
cap = cv2.VideoCapture(0)
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    ok, frame = cap.read()
    if not ok:
        raise RuntimeError("La camara no entrego un cuadro")
    alto, ancho = frame.shape[:2]
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Clase 11 - 1 Color | 2 Cara | 3 Mano")
    fuente = pygame.font.Font(None, 26)
    reloj = pygame.time.Clock()
    nombre, detectar = DETECTORES[pygame.K_1]

    andando = True
    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                elif evento.key in DETECTORES:
                    nombre, detectar = DETECTORES[evento.key]


        if not andando:
            break
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        if frame.shape[:2] != (alto, ancho):
            frame = cv2.resize(frame, (ancho, alto))
        pos = detectar(frame)

        superficie = pygame.image.frombuffer(frame.tobytes(), (ancho, alto), "BGR")
        pantalla.blit(superficie, (0, 0))

        if pos is not None:
            pygame.draw.circle(pantalla, (182, 255, 63), pos, 18, 3)
        estado = nombre if pos is not None else nombre + ": no veo nada"
        texto = fuente.render(estado, True, (255, 255, 255), (0, 0, 0))
        pantalla.blit(texto, (12, 12))
        pygame.display.flip()
        reloj.tick(30)
finally:
    cap.release()
    pygame.quit()
    vision.cerrar()
