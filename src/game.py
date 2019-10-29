import wall
import box
import player
import obstacles
import player


class Game():

    def __init__(self):
        self.level = 1
        self.wall = wall.Wall()
        self.box = box.Box()
        self.player = player.Player()
        self.LaListaDeObstaculos = []
        self.lalistaderects = []

    def placePlayer(self, lifes, speed):
        # self.player.createPlayer(lifes, speed)
        pass

    def placeEnemies(self):
        pass

    def createBackground(self):
        pass

    def createWall(position, sprite):
        self.wall.setPosition(position)
        self.wall.setSprite(sprite)

    def createBox(position, sprite):
        self.box.setPosition(position)
        self.box.setSprite(sprite)

    def createObstacles(self, dimensions):
        WidthHeightObstacle = 37
        for i in range(0, int((dimensions[0] / WidthHeightObstacle)) + 1):  # De 0 a 26

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, 0))  # Creo los bloques de la fila de arriba

            self.LaListaDeObstaculos.append(obstacles.Obstacle(i * WidthHeightObstacle, dimensions[1] -  WidthHeightObstacle))  # Creo los bloques de la fila de abajo

        for i in range(0, int((dimensions[1] / WidthHeightObstacle)) + 1):  # De 0 a 16

            self.LaListaDeObstaculos.append(obstacles.Obstacle(0, i * WidthHeightObstacle))  # Creo los bloques de las columnas de la izquierda

            self.LaListaDeObstaculos.append(obstacles.Obstacle(dimensions[0] - WidthHeightObstacle, i *  WidthHeightObstacle))  # Creo los bloques de las columnas de la derecha

        for x in range(1, int((dimensions[0] / (WidthHeightObstacle * 2))) + 1):  # De 1 a 13
            for y in range(1, int((dimensions[1]) / (WidthHeightObstacle * 2)) + 1):  # De 1 a 8
                self.LaListaDeObstaculos.append(obstacles.Obstacle(x * (WidthHeightObstacle * 2), y * (WidthHeightObstacle * 2)))

    def createRects(self):
        for obstaculo in self.LaListaDeObstaculos:
            self.lalistaderects.append(obstaculo.getObstacleRect())
    #def createPlayer(self):
        #pass
        # self.LaListaDeObstaculos.append(self.player)
        
    
# Movimiento

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def setBombermanPosition(self):
        self.player.setBombermanPosition()

# Colisiones
    def getListaDeObstaculos(self):
        return self.LaListaDeObstaculos

    def getPlayerRect(self):
        return self.player.getPlayerRect()

    def getListaDeRects(self):
        return self.lalistaderects
