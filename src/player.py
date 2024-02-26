from dynamicObject import DynamicObject
import pygame
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
        self.width = 30
        self.height = 30
        self.playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitboxW = 4
        self.hitboxH = 8
        self.hitbox = pygame.Rect(0, 0, self.hitboxW, self.hitboxH) # Dibujo un cuadrad
        self.setPosition(self.position)
        self.positionrespaldo = None
        self.direccion = "down"
        self.pickupTime = 0

    def createPlayer(self, lifes, speed):
        self.lifes = lifes
        self.speed = speed

# Movimiento

    def move(self, direccion):
        self.positionrespaldo = copy.deepcopy(self.position)

        newPosition = [self.x + direccion[0] * self.speed, self.y + direccion[1] * self.speed]
        self.setPosition(newPosition)

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
        return self.hitbox
    
    def getWorldPosition(self):
        self.x = self.position[0]
        self.y = self.position[1]
        self.worldPos = (self.x, self.y, self.width, self.height)
        return self.worldPos

# Setters

    def setState(self):
        self.dead = not self.dead
    
    def setDeathSprites(self, image):
        self.deathSprites = image

    def setLifes(self, life):
        self.lifes = self.lifes + life

    def setPosition(self, position):
        self.position = position
        self.x, self.y = self.position
        self.playerRect.topleft = self.x, self.y
        self.hitbox.center = self.playerRect.center

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed = speedAmmount

    def setBombermanDireccion(self, direccion):
        self.direccion = direccion

    def setPlayerRect(self, rect):
        self.playerRect = rect

    def setPlayerHitbox(self, rect):
        self.hitbox = rect

    def isDead(self):
        return self.dead
