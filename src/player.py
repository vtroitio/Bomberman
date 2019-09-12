import * from pygame

white = (255, 255, 255)


class player(sprite.Bomberman):
    def placeBomb(self):
        pass

    def createPlayer(self):
        pass

    def destroyPlayer(self):
        pass

    def __init__(self, color, width, height)
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.image = pygame.image.load("").conver_alpha()