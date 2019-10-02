from dynamicObject import DynamicObject
from bomb import Bomb


class Player(DynamicObject):
    def __init__(self):
        super().__init__()
        self.sprite = None
        self.lifes = None
        self.speed = None

    def placeBomb(self, position, sprite):
        self.bomb = Bomb.createBomb(position, sprite)

    def createPlayer(self, lifes, speed):
        self.sprite = "sprites/25x35.png"
        self.lifes = lifes
        self.speed = speed


# Movimiento
    def move(self, direccion):
        for index in range(len(self.position)):
            print(self.position, "antes")
            self.position[index] = self.position[index] + direccion[index]
            print(self.position, "despues ")

    def getBombermanPosition(self):
        print(self.position)
        return self.position
# Setters

    def setLifes(self, lifeAmmount):
        self.lifes = lifesAmmount

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount
