from item import *


class Bomb(Item):

    def __init__(self):
        super().__init__(self)
        self.time = None

    def createBomb(position, sprite, time):
        self.position = position
        self.sprite = sprite
        self.time = time

    def destroyBomb():
        pass
