from dynamicObject import DynamicObject
from bomb import Bomb
import pygame
import background
import copy as copy


class Player(DynamicObject):
    def __init__(self):
        super().__init__()
        self.lifes = None
        self.speed = 3
        self.sprite = "sprites/Bomberman.png"
        self.positionanterior = []
        # Colisiones
        self.x = self.position[0]
        self.y = self.position[1]
        self.width = 30
        self.height = 30
        self.hitbox = (self.x + 20, self.y, self.width, self.height)  # Dibujo un cuadrado
        self.playerRect = None
        self.positionrespaldo = None

    def placeBomb(self, position, sprite):  # Coloca una bomba
        self.bomb = Bomb.createBomb(position, sprite)

    def createPlayer(self, lifes, speed):
        self.lifes = lifes
        self.speed = speed


# Movimiento

    def move(self, direccion, ventana):
        self.positionrespaldo = copy.deepcopy(self.position)

        for index in range(len(self.position)):

            # Movimiento
            self.position[index] = (self.position[index] + direccion[index] * (self.speed))

            # Hitbox y colisiones
            self.x = self.position[0]
            self.y = self.position[1]
            self.hitbox = (self.x, self.y, self.width, self.height)

# Getters

    def getBombermanPosition(self):
        return self.position

    def getBombermanSpeed(self):
        print(self.speed)
        return self.speed

    def getPlayerRect(self):
        return self.playerRect

    def getPlayerHitbox(self):
        return self.hitbox
    
# Setters

    def setLifes(self, lifeAmmount):
        self.lifes = lifesAmmount

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount

    def setBombermanPosition(self):
        self.position = self.positionrespaldo

    def setPlayerRect(self, rect):
        self.playerRect = rect