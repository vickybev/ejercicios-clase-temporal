"""11.3: mano por defecto; 1 color para probar. Salir y entrar rearma el botón."""
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
    pygame.display.set_caption("11.3 - Boton sin tocar | 1..3 detectores")
    fuente = pygame.font.Font(None, 26)
    reloj = pygame.time.Clock()
    nombre, detectar = DETECTORES[pygame.K_3]
    boton = pygame.Rect(12, 12, min(220, ancho - 24), min(80, alto - 24))
    adentro = 0
    activado = False
    clics = 0
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
                    adentro = 0
                    activado = False

        if not andando:
            break
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.flip(frame, 1)
        if frame.shape[:2] != (alto, ancho):
            frame = cv2.resize(frame, (ancho, alto))
        pos = detectar(frame)
        if pos is not None and boton.collidepoint(pos):
            adentro = min(adentro + 1, 30)
            if adentro == 30 and not activado:
                clics += 1
                print("Clic", clics)
                activado = True
        else:
            adentro = 0
            activado = False
        superficie = pygame.image.frombuffer(frame.tobytes(), (ancho, alto), "BGR")
        pantalla.blit(superficie, (0, 0))
        pygame.draw.rect(pantalla, (35, 35, 35), boton)
        progreso = pygame.Rect(boton.x, boton.y, int(boton.width * adentro / 30), boton.height)
        pygame.draw.rect(pantalla, (60, 120, 220), progreso)
        pygame.draw.rect(pantalla, (255, 255, 255), boton, 2)
        mensaje = fuente.render(f"Clics: {clics}", True, (255, 255, 255))
        pantalla.blit(mensaje, (boton.x + 8, boton.y + 25))
        if pos is not None:
            pygame.draw.circle(pantalla, (182, 255, 63), pos, 18, 3)
        estado = nombre if pos is not None else nombre + ": no veo nada"
        texto = fuente.render(estado, True, (255, 255, 255), (0, 0, 0))
        pantalla.blit(texto, (12, boton.bottom + 8))
        pygame.display.flip()
        reloj.tick(30)
finally:
    cap.release()
    pygame.quit()
    vision.cerrar()
