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
# Movimiento

    def givePosition(self, position, ventana):
        self.player.move(position, ventana)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()

    def setBombermanPosition(self, pos):
        self.player.setBombermanPosition(pos)
