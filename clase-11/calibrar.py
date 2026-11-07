"""11.1: clic elige tono; m alterna máscara; X o Escape sale."""
import cv2
import pygame

pygame.init()
cap = cv2.VideoCapture(0)
minimo = (5, 100, 100)
maximo = (20, 255, 255)
ver_mascara = False
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    ok, frame = cap.read()
    if not ok:
        raise RuntimeError("No llego una imagen")
    frame = cv2.flip(frame, 1)
    alto, ancho = frame.shape[:2]
    # El clic usa la imagen que la persona acaba de ver, no otra posterior.
    hsv_mostrado = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("11.1 - Clic: tono | m: mascara | X: salir")
    reloj = pygame.time.Clock()
    andando = True
    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                elif evento.key == pygame.K_m:
                    ver_mascara = not ver_mascara
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                x, y = evento.pos
                if 0 <= x < ancho and 0 <= y < alto:
                    h, s, v = [int(valor) for valor in hsv_mostrado[y, x]]
                    minimo = (max(0, h - 10), 100, 100)
                    maximo = (min(179, h + 10), 255, 255)
                    print("HSV:", (h, s, v))
                    print("COLOR_MIN =", minimo)
                    print("COLOR_MAX =", maximo)
        if not andando:
            break
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        if frame.shape[:2] != (alto, ancho):
            frame = cv2.resize(frame, (ancho, alto))
        hsv_mostrado = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if ver_mascara:
            mascara = cv2.inRange(hsv_mostrado, minimo, maximo)
            salida = cv2.cvtColor(mascara, cv2.COLOR_GRAY2BGR)
        else:
            salida = frame
        superficie = pygame.image.frombuffer(salida.tobytes(), (ancho, alto), "BGR")
        pantalla.blit(superficie, (0, 0))
        pygame.display.flip()
        reloj.tick(30)
finally:
    cap.release()
    pygame.quit()
