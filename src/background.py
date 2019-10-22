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
        self.obstacles = obstacles.Obstacles(0, 0)


# Reload
    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for i in range(0, int((dimensions[0] / 37)) + 1):

            # Crea las filas de ariba
            self.screen.blit(self.obstacle, (i * 37, 0))

            # Crea las filas de abajo
            self.screen.blit(self.obstacle, (i * 37, dimensions[1] - 37))

            # Dibujo el hitbox de las filas de arriba
            self.obstacles.x = i * 37
            self.obstacles.y = 0
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

            # Dibujo el hitbox de las filas de abajo
            self.obstacles.x = i * 37
            self.obstacles.y = dimensions[1] - 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

        for i in range(0, int((dimensions[1] / 37)) + 1):   # Crea las columnas

            # Crea las columnas de la izquierda
            self.screen.blit(self.obstacle, (0, i * 37))

            # Crea las columnas de la derecha
            self.screen.blit(self.obstacle, (dimensions[0] - 37, i * 37))

            # Dibujo el hitbox de las columnas de la izquierda
            self.obstacles.x = 0
            self.obstacles.y = i * 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

            # Dibujo el hitbox de las columnas de la derecha
            self.obstacles.x = dimensions[0] - 37
            self.obstacles.y = i * 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

    def reloadObstacle(self, dimensions):  # Crea los obstaculos
        for x in range(1, int((dimensions[0] / 74)) + 1):
            for y in range(1, int((dimensions[1]) / 74) + 1):

                # Crea obstaculos en todo el mapa
                self.screen.blit(self.obstacle, (x * 74, y * 74))

                # Dibujo el hitbox de los obstaculos
                self.obstacles.x = x * 74
                self.obstacles.y = y * 74
                self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
                pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())

# Loads
    def loadObstacle(self, path, pos):
        self.obstacle = pygame.image.load(path)
        self.screen.blit(self.obstacle, pos)

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
