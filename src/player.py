from dynamicObject import *


class Player(DynamicObject):

    def __init__(self):
        super().__init__(self)
        self.sprite = None
        self.lifes = None
        self.speed = None

    def placeBomb(self):
        pass

    def createPlayer(self):
        self.sprite = "sprites/25x35.png"
        self.lifes = 3
        self.speed = 5

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount
