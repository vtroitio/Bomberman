from dynamicObject import DynamicObject
from bomb import Bomb
import pygame
import background
import copy as copy


class Player(DynamicObject):
    def __init__(self):
        super().__init__()
        self.lifes = 3
        self.speed = 5
        self.positionanterior = []
        # Colisiones
        self.x = self.position[0]
        self.y = self.position[1]
        self.width = 29
        self.height = 29
        self.hitbox = (self.x + 20, self.y, self.width, self.height)  # Dibujo un cuadrado
        self.playerRect = None
        self.positionrespaldo = None
        self.direccion = "down"

    def placeBomb(self, position, sprite):  # Coloca una bomba
        self.bomb = Bomb.createBomb(position, sprite)

    def createPlayer(self, lifes, speed):
        self.lifes = lifes
        self.speed = speed
        

# Movimiento

    def move(self, direccion, ventana):
        self.direccion = direccion
        self.positionrespaldo = copy.deepcopy(self.position)

        for index in range(len(self.position)):

            # Movimiento
            self.position[index] = (self.position[index] + direccion[index] * (self.speed))
            # Hitbox y colisiones
            self.x = self.position[0]
            self.y = self.position[1]
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(ventana, (255, 0, 0), self.hitbox, 2)
            if direccion == [0, -1]:
                self.direccion = "up"
            elif direccion == [0, 1]:
                self.direccion = "down"
            elif direccion == [1, 0]:
                self.direccion = "right"
            elif direccion == [-1, 0]:
                self.direccion = "left"

# Getters

    def getBombermanPosition(self):
        return self.position

    def getBobmermanPositionAnterior(self):
        return self.positionrespaldo

    def getBombermanSpeed(self):
        return self.speed

    def getBombermanDirection(self):
        return self.direccion

    def getPlayerRect(self):
        return self.playerRect

    def getPlayerHitbox(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.hitbox = (self.x, self.y, self.width, self.height)
        return self.hitbox

# Setters

    def setLifes(self, life):
        self.lifes = self.lifes + life

    def setPosition(self, position):
        self.position = position

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed = speedAmmount

    def setBombermanPosition(self):
        self.position = self.positionrespaldo

    def setPlayerRect(self, rect):
        self.playerRect = rect