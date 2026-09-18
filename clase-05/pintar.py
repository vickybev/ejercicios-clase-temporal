import pygame
import random

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("5.3 - Clic: pintar | Espacio: borrar")
reloj = pygame.time.Clock()
paleta = [(230, 70, 90), (60, 170, 120), (70, 100, 220), (245, 185, 50)]
circulos = []
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Aceptamos los tres botones habituales; la rueda no pinta.
            if evento.button in [1, 2, 3]:
                circulo = {"posicion": evento.pos, "color": random.choice(paleta)}
                circulos.append(circulo)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                circulos = []

    # La lista conserva los datos; redibujamos todos los círculos tras limpiar.
    pantalla.fill((245, 245, 245))
    for circulo in circulos:
        pygame.draw.circle(pantalla, circulo["color"], circulo["posicion"], 20)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
