import dynamicObject


class Player(dynamicObject.DynamicObject):

    def __init__(self):
        super().__init__(self)
        self.sprite = None
        self.lifes = 3
        self.speed = 5

    def placeBomb(self):
        pass

    def createPlayer(self):
        pass

    def destroyPlayer(self):
        pass

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount
