import wall
import box
from player import Player
import obstacles
import player


class Game():

    def __init__(self):
        self.level = 1
        self.wall = wall.Wall()
        self.box = box.Box()
        self.player = Player() 

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

    def givePosition(self, position):
        self.player.move(position)

    def getBombermanPosition(self):
        return self.player.getBombermanPosition()

    def getBombermanSpeed(self):
        return self.player.getBombermanSpeed()    

    def setBombermanPosition(self, pos):
        self.player.setBombermanPosition(pos)
    
    def getBombermanPositionAnterior(self):
        return self.player.getBombermanPositionAnterior
