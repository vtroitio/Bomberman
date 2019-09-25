import pygame


class Background():
    def __init__(self, dimensions):
        self.background = None
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def setBackground(self):
        pass

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)
        self.screen.blit(self.background, (0, 0))
