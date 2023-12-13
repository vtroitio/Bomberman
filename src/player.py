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
        self.width = 29
        self.height = 29
        self.hitbox = (self.x + 20, self.y, self.width, self.height)  # Dibujo un cuadrado
        self.playerRect = None
        self.positionrespaldo = None
        self.direccion = "down"

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
        print("Hubo colision del bomberman, le asigno la posicion de respaldo")
        print("La posicion actual es: " + str(self.position))
        print("La posicion de respaldo es: " + str(self.positionrespaldo))

        self.position[0] = self.positionrespaldo[0]
        self.position[1] = self.positionrespaldo[1]

        # Hitbox y colisiones
        self.x = self.position[0]
        self.y = self.position[1]

        print("La posicion post colision es: " + str(self.position))


    def setPlayerRect(self, rect):
        self.playerRect = rect