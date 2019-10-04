class Bomb():
    def __init__(self):
        super().__init__(self)
        self.time = 3

    def createBomb(self, position):
        self.position = position
        

    def destroyBomb(self, sprite):
        self.sprite = sprite
