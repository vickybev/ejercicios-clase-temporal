"""10.1 de referencia. 1..7: filtros; X o Escape: salir."""
import cv2
import pygame
import filtros

FILTROS = {
    pygame.K_1: ("Normal", filtros.sin_filtro),
    pygame.K_2: ("Gris", filtros.a_gris),
    pygame.K_3: ("Desenfoque", filtros.desenfocar),
    pygame.K_4: ("Bordes", filtros.bordes),
    pygame.K_5: ("Umbral", filtros.umbral),
    pygame.K_6: ("Invertir", filtros.invertir),
    pygame.K_7: ("Lápiz", filtros.lapiz),
}
pygame.init()
cap = cv2.VideoCapture(0)
try:
    if not cap.isOpened():
        raise RuntimeError("No pude abrir la camara")
    ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if ancho <= 0 or alto <= 0:
        raise RuntimeError("La camara no informo un tamano valido")
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("10.1 - 1..7: filtros | X: salir")
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 28)
    nombre, aplicar = FILTROS[pygame.K_1]
    andando = True
    while andando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                elif evento.key in FILTROS:
                    nombre, aplicar = FILTROS[evento.key]
        if not andando:
            break
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        if frame.shape[:2] != (alto, ancho):
            frame = cv2.resize(frame, (ancho, alto))
        salida = filtros.a_color(aplicar(frame))
        superficie = pygame.image.frombuffer(salida.tobytes(), (ancho, alto), "BGR")
        pantalla.blit(superficie, (0, 0))  # Primero el video.
        texto = fuente.render(nombre, True, (255, 255, 255), (0, 0, 0))
        pantalla.blit(texto, (12, 12))  # Después el texto.
        pygame.display.flip()
        reloj.tick(30)
finally:
    cap.release()
    pygame.quit()
