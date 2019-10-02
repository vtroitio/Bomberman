from item import Item


class Bomb(Item):

    def __init__(self):
        super().__init__(self)
        self.time = None

    def createBomb(self, position, sprite):
        self.position = position
        self.sprite = sprite
        self.time = self.time

    def destroyBomb(self, sprite):
        self.sprite = sprite
