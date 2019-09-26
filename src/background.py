import pygame


class Background():
    def __init__(self, dimensions):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        self.background = None
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions
        self.bomberman = None

    def loadBombermanImage(self, path, pos):
        self.bomberman = pygame.image.load(path)
        self.screen.blit(self.bomberman, pos)

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)
        self.screen.blit(self.background, (0, 0))
