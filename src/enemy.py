from dynamicObject import DynamicObject
from player import Player

class Enemy(DynamicObject):
    
    def __init__(self):
        super().__init__(self)
        self.player = Player()

    def createEnemy(self, position, sprite, lifes, speed, size):
        self.position = position
        self.sprite = sprite
        self.lifes = lifes
        self.speed = speed
        self.size = size

    def destroyEnemy(self):
        self.sprite = None


    def attack(self): 
       self.player.lifes = int(self.player.lifes) - 1

    def defineMovement(self):
        pass
