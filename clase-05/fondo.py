import pygame

# Preparamos una ventana de 600 por 400 y un reloj para limitar las vueltas.
pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("5.1 - R: rojo | V: verde | A: azul")
reloj = pygame.time.Clock()
color = (245, 245, 245)
ejecutando = True

# Leemos eventos; KEYDOWN ocurre al presionar una tecla.
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                color = (255, 0, 0)
            elif evento.key == pygame.K_v:
                color = (0, 255, 0)
            elif evento.key == pygame.K_a:
                color = (0, 0, 255)

    # La variable conserva el último color aunque soltemos la tecla.
    pantalla.fill(color)
    pygame.display.flip()
    reloj.tick(60)

# Cerramos pygame después de salir del bucle.
pygame.quit()
