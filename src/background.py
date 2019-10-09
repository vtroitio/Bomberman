import pygame
import game


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        self.background = None
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions
        self.bomberman = None
        self.game = game
        
        # self.game = game.Game()

    def loadBombermanImage(self, path, pos):
        self.bomberman = pygame.image.load(path)
        self.screen.blit(self.bomberman, pos)

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)
        self.background = pygame.transform.scale(self.background, self.dimensions)
        self.screen.blit(self.background, (0, 0))

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())
    
    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)