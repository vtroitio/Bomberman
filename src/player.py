from dynamicObject import *


class Player(DynamicObject):

    def __init__(self):
        super().__init__(self, 4)
        self.sprite = "sprites/25x35.png"
        self.lifes = 3
        self.speed = 5

    def placeBomb(self):
        pass

    def createPlayer(self):
        pass

    def destroyPlayer(self):
        pass
