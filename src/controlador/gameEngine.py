import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Que onda bro")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [50, 250, 100, 100], 0)
        pygame.display.flip()
        clock.tick(15)
        if event.type == pygame.QUIT:
            carryOn = False
pygame.quit()


class GameEngine():

    def esc():
        pass

    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def validatePosition():
        pass

    def updatePosition():
        pass

