import wall
import box
import player
import obstacles
import player
import enemy
import copy

class Game():

    def __init__(self):
        self.level = 1
        self.wall = wall.Wall()
        self.box = box.Box()
        self.player = player.Player()
        self.LaListaDeObstaculos = []
        self.lalistaderects = []
        self.lalistadeenemigos = []
        self.lalistaderectsenemigos = []

    def placePlayer(self, lifes, speed):
        # self.player.createPlayer(lifes, speed)
        pass

    def placeEnemies(self):
        self.lalistadeenemigos.append(enemy.Enemy([185, 37]))
        self.lalistadeenemigos.append(enemy.Enemy([481, 37]))

    def createBackground(self):
        pass

    def createWall(position, sprite):
        self.wall.setPosition(position)
        self.wall.setSprite(sprite)

    def createBox(position, sprite):
        self.box.setPosition(position)
        self.box.setSprite(sprite)

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37  # Tamaño del bloque utilizado

        for i in range(0, int((dimensions[0] / WidthHeightObstacle)) + 1):  # De 0 a 26

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, 0))  # Creo los bloques de la fila de arriba

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, dimensions[1] - WidthHeightObstacle))  # Creo los bloques de la fila de abajo

        for i in range(0, int((dimensions[1] / WidthHeightObstacle)) + 1):  # De 0 a 16

            self.LaListaDeObstaculos.append(obstacles.Obstacle(0, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la izquierda

            self.LaListaDeObstaculos.append(obstacles.Obstacle(dimensions[0] - WidthHeightObstacle, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la derecha

        for x in range(1, int((dimensions[0] / (WidthHeightObstacle * 2))) + 1):  # De 1 a 13
            for y in range(1, int((dimensions[1]) / (WidthHeightObstacle * 2)) + 1):  # De 1 a 8
                self.LaListaDeObstaculos.append(obstacles.Obstacle(x * (WidthHeightObstacle * 2), y * (WidthHeightObstacle * 2)))

    def createRects(self):
        for obstaculo in self.LaListaDeObstaculos:
            self.lalistaderects.append(obstaculo.getObstacleRect())
        for enemy in self.lalistadeenemigos:
            self.lalistaderectsenemigos.append(enemy.getEnemyHitbox())

# Movimiento

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def getBombermanDirection(self):
        return self.player.getBombermanDirection
        
    def setBombermanPosition(self):
        self.player.setBombermanPosition()

    def moverEnemigo(self):
        for enemy in self.lalistadeenemigos:
            print('elenemigoahoraes',enemy)
            self.positionAnteriorEnemy = copy.deepcopy(enemy.getEnemyPosition())
            self.nuevaposicion = [self.positionAnteriorEnemy[0], self.positionAnteriorEnemy[1] + 1 * enemy.getEnemySpeed()]
            enemy.setPosition(self.nuevaposicion)

# Colisiones
    def getListaDeObstaculos(self):
        return self.LaListaDeObstaculos

    def getPlayerRect(self):
        return self.player.getPlayerRect()

    def getListaDeRects(self):
        return self.lalistaderects

    def getPlayerHitbox(self):
        return self.player.getPlayerHitbox()

    def setPlayerRect(self, rect):
        self.player.setPlayerRect(rect)

    def getListaDeEnemigos(self):
        return self.lalistadeenemigos
