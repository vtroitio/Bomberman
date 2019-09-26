import dynamicObject
import wall
import box


class Game():

    def __init__(self):
        self.level = 1
        self.wall = wall.Wall(self)
        self.box = box.Box(self)

    def placePlayer():
        pass

    def placeEnemies():
        pass

    def createBackground():
        pass

    def createWall(position, sprite):
        self.wall.setPosition(position)
        self.wall.setSprite(sprite)

    def createBox(position, sprite):
        self.box.setPosition(position)
        self.box.setSprite(sprite)

    def givePosition(self, position):
        self.dynamicObject.move(position)
