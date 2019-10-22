from dynamicObject import DynamicObject
from bomb import Bomb


class Player(DynamicObject):
    def __init__(self):
        super().__init__()
        self.lifes = None
        self.speed = 3
        self.sprite = "sprites/Bomberman.png"
        self.positionanterior = []

    def placeBomb(self, position, sprite):
        self.bomb = Bomb.createBomb(position, sprite)

    def createPlayer(self, lifes, speed):
        self.lifes = lifes
        self.speed = speed


# Movimiento
    def move(self, direccion):
        self.positionanterior = self.position
        for index in range(len(self.position)):
            print(self.position, "antes")
            self.position[index] = (self.position[index] + direccion[index] * (self.speed))
            print(self.position, "despues ")

    def getBombermanPosition(self):
        print(self.position)
        return self.position
    
    def getBombermanPositionAnterior(self):
        print(self.positionanterior)
        return self.positionanterior
    
    def getBombermanSpeed(self):
        print(self.speed)
        return self.speed
# Setters

    def setLifes(self, lifeAmmount):
        self.lifes = lifesAmmount

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount

    def setBombermanPosition(self, pos):
        self.positionanterior = self.position
        self.position = pos
