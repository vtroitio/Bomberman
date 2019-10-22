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
        self.game = game        # self.game = game.Game()
        self.frame = 0
        self.left_states = { 0: (0, 90, 30, 30), 1: (30, 90, 30, 30), 2: (60, 90, 30, 30) }
        self.right_states = { 0: (0, 60, 30, 30), 1: (30, 60, 30, 30), 2: (60, 60, 30, 30) }
        self.up_states = { 0: (0, 30, 30, 30), 1: (30, 30, 30, 30), 2: (60, 30, 30, 30) }
        self.down_states = { 0: (0, 0, 30, 30), 1: (30, 0, 30, 30), 2: (60, 0, 30, 30) }
        pygame.key.set_repeat(50)
        self.matriz = []


# Reload
    def reloadBackground(self, dimensions):
        for i in range(0, int((dimensions[0] / 37)) + 1):    # Creo Las Filas
            self.screen.blit(self.obstacle, (i * 37, 0))
            self.screen.blit(self.obstacle, (i * 37, dimensions[1] - 37))
            self.matriz.append((i * 37, dimensions[1] - 37))
            self.matriz.append((i * 37, 0))

        for i in range(0, int((dimensions[1] / 37)) + 1):   # Creo las columnas
            self.screen.blit(self.obstacle, (0, i * 37))
            self.screen.blit(self.obstacle, (dimensions[0] - 37, i * 37))
            self.matriz.append((dimensions[0] - 37, i * 37))
            self.matriz.append((0, i * 37))

    def reloadObstacle(self, dimensions):
        for x in range(1, int((dimensions[0] / 74)) + 1):
            for y in range(1, int((dimensions[1]) / 74) + 1):
                self.screen.blit(self.obstacle, (x * 74, y * 74))
                self.matriz.append((x * 74, y * 74))

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
