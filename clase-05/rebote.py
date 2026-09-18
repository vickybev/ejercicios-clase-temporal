import pygame

pygame.init()
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("5.2 - El círculo que rebota")
reloj = pygame.time.Clock()

# x e y son el centro; el radio mide la distancia hasta el borde del círculo.
radio = 20
x = ancho // 2
y = alto // 2
vel_x = 3
vel_y = 2
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Sumamos las velocidades para avanzar en diagonal.
    x += vel_x
    y += vel_y

    # Corregimos la posición y cambiamos el sentido al tocar cada borde.
    if x + radio >= ancho:
        x = ancho - radio
        vel_x = -vel_x
    elif x - radio <= 0:
        x = radio
        vel_x = -vel_x
    if y + radio >= alto:
        y = alto - radio
        vel_y = -vel_y
    elif y - radio <= 0:
        y = radio
        vel_y = -vel_y

    # Limpiamos el fotograma anterior y dibujamos la posición nueva.
    pantalla.fill((245, 245, 245))
    pygame.draw.circle(pantalla, (80, 70, 210), (x, y), radio)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
