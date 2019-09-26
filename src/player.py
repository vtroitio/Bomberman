import dynamicObject


class Player(dynamicObject.DynamicObject):

    def __init__(self):
        super().__init__(self)
        self.sprite = None
<<<<<<< HEAD
        self.lifes = None
        self.speed = None
=======
        self.lifes = 3
        self.speed = 5
>>>>>>> 670affa45312be683f8fb8c44926cd67a8c6b16f

    def placeBomb(self):
        pass

    def createPlayer(self):
        self.sprite = "sprites/25x35.png"
        self.lifes = 3
        self.speed = 5

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount
