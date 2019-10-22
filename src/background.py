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
<<<<<<< HEAD
        self.frame = 0
        self.left_states = { 0: (0, 90, 30, 30), 1: (30, 90, 30, 30), 2: (60, 90, 30, 30) }
        self.right_states = { 0: (0, 60, 30, 30), 1: (30, 60, 30, 30), 2: (60, 60, 30, 30) }
        self.up_states = { 0: (0, 30, 30, 30), 1: (30, 30, 30, 30), 2: (60, 30, 30, 30) }
        self.down_states = { 0: (0, 0, 30, 30), 1: (30, 0, 30, 30), 2: (60, 0, 30, 30) }
        pygame.key.set_repeat(50)
=======
>>>>>>> 7524f22f2fa2599b4bcc80b13b4071b116124bc5
        self.matriz = []
        self.obstacles = obstacles.Obstacles()


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
            self.obstacles.filasArribaRect = pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

            # Dibujo el hitbox de las filas de abajo
            self.obstacles.x = i * 37
            self.obstacles.y = dimensions[1] - 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            self.obstacles.filasAbajoRect = pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

        for i in range(0, int((dimensions[1] / 37)) + 1):   # Crea las columnas

            # Crea las columnas de la izquierda
            self.screen.blit(self.obstacle, (0, i * 37))

            # Crea las columnas de la derecha
            self.screen.blit(self.obstacle, (dimensions[0] - 37, i * 37))

            # Dibujo el hitbox de las columnas de la izquierda
            self.obstacles.x = 0
            self.obstacles.y = i * 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            self.obstacles.columnasIzquierdaRect = pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

            # Dibujo el hitbox de las columnas de la derecha
            self.obstacles.x = dimensions[0] - 37
            self.obstacles.y = i * 37
            self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
            self.obstacles.columnasDerechaRect = pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

    def reloadObstacle(self, dimensions):  # Crea los obstaculos
        for x in range(1, int((dimensions[0] / 74)) + 1):
            for y in range(1, int((dimensions[1]) / 74) + 1):

                # Crea obstaculos en todo el mapa
                self.screen.blit(self.obstacle, (x * 74, y * 74))

<<<<<<< HEAD
    def reloadBomberman(self, direction):
        # self.screen.blit(self.bomberman, self.game.getBombermanPosition())
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states) 
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.bombermanImage = self.bomberman.subsurface(self.bomberman.get_clip())

    # def reloadBomberman(self, pos):
    #     self.screen.blit(self.bomberman, pos)
=======
                # Dibujo el hitbox de los obstaculos
                self.obstacles.x = x * 74
                self.obstacles.y = y * 74
                self.obstacles.hitbox = (self.obstacles.x, self.obstacles.y, self.obstacles.width, self.obstacles.height)
                obstacleRect = pygame.draw.rect(self.screen, (255, 0, 0), self.obstacles.hitbox, 1)

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())
>>>>>>> 7524f22f2fa2599b4bcc80b13b4071b116124bc5

# Loads
    def loadObstacle(self, path, pos):
        self.obstacle = pygame.image.load(path)
        self.screen.blit(self.obstacle, pos)

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = pygame.image.load(path)
        self.bomberman.set_clip(pygame.Rect(0, 0, 30, 30))
        self.bombermanImage = self.bomberman.subsurface(self.bomberman.get_clip())
        self.rect = self.bombermanImage.get_rect()
        self.rect.topleft = pos
        self.screen.blit(self.bombermanImage, self.rect)

# Etc
    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)

    def getFrame(self, frameSet):
        self.frame += 1
        if self.frame > (len(frameSet) - 1):
            self.frame = 0
        return frameSet[self.frame]

    def clip(self, clippedRect):
        if type(clippedRect) is dict:
            self.bomberman.set_clip(pygame.Rect(self.getFrame(clippedRect)))
        else:
            self.bomberman.set_clip(pygame.Rect(clippedRect))
        return clippedRect
