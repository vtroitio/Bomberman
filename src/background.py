import pygame
import game
import obstacles


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        pygame.key.set_repeat(50)
        self.background = None
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions
        self.bomberman = None
        self.game = game        # self.game = game.Game()
        self.matriz = []
        self.obstacles = obstacles.Obstacle(0, 0)


# Reload
    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for obstaculo in self.game.getListaDeObstaculos():

            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (255, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())

# Loads
    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path)

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = pygame.image.load(path)
        self.bomberman = pygame.transform.scale(self.bomberman, [30, 30])
        self.screen.blit(self.bomberman, pos)

# Etc
    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)
