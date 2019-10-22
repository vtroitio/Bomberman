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

    def createObstacles(self):
        dimensions = [925, 555]
        for i in range(0, int((dimensions[0] / 37)) + 1):

            self.obstacles = obstacles.Obstacles(i, 0)  # Creo hitboxes de la fila de arriba
            self.obstacles.setListaDeObstaculos([i, 0])

            self.obstacles = obstacles.Obstacles(i * 37, dimensions[1] - 37)  # Creo hitboxes de la fila de abajo
            self.obstacles.setListaDeObstaculos([(i * 37, dimensions[1] - 37)])

        for i in range(0, int((dimensions[1] / 37)) + 1):

            self.obstacles = obstacles.Obstacles(0, i * 37)  # Crea hitboxes de las columnas de arriba
            self.obstacles.setListaDeObstaculos([0, i * 37])

# Movimiento

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def setBombermanPosition(self, pos):
        self.player.setBombermanPosition(pos)
