import * from pygame

white = (255, 255, 255)


class Player(sprite.Player):

    def __init__(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.image = pygame.image.load("sprites/25x35.png").conver_alpha()
        self.rect = self.image.get_rect()

    def placeBomb(self):
        pass

    def createPlayer(self):
        pass

    def destroyPlayer(self):
        pass
