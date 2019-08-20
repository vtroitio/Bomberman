import pygame, sys 
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Figuras Geométricas")

pygame.draw.circle(ventana, (255, 0, 0) , (300, 200), 50) # Dibuja un circulo
pygame.draw.rect(ventana, (0, 255, 0) , (100, 200, 100 ,50)) # Dibuja un rectangulo
pygame.draw.polygon(ventana, (0, 0, 255) , ((400, 200), (500,200), (500, 100), (600, 100))) # Dibuja poligonos

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
