import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((555, 407))
pygame.display.set_caption("Bomberman")

Color = pygame.Color(255, 0, 0)
backColor = pygame.Color(16, 122, 48)

backgr = pygame.image.load("Sprites/background.png")
caja = pygame.image.load("Sprites/cajafea.png")
# posX = randint(37, 483)
# posY = randint(37, 335)
posX = 37
posY = 37
# rect1 = pygame.draw.rect(ventana, Color, (0, 0, 555, 37), 1)
# rect2 = pygame.draw.rect(ventana, Color, (0, 0, 37, 407), 1)
# rect3 = pygame.draw.rect(ventana, Color, (0, 370, 555, 37), 1)
# rect4 = pygame.draw.rect(ventana, Color, (518, 0, 37, 407), 1)

velocidad = 1
derecha = True

while True:
    ventana.fill(backColor)
    ventana.blit(backgr, (0, 0))
    ventana.blit(caja, (posX, posY))
    rect = pygame.draw.rect(ventana, Color, (36, 36, 483, 335), 1)
    sqr = pygame.draw.rect(ventana, Color, (74, 74, 37, 37), 1)
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            sys.exit()

    if derecha is True:
        if posX < 483:
            posX = posX + velocidad
        else:
            derecha is False
    else:
        if posx > 1:
            posX = posX - velocidad
        else:
            derecha is True

    pygame.display.update()
