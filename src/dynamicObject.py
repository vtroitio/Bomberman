import player


class DynamicObject():

    def __init__(self):
        self.position = [0, 0]
        self.hitbox = ()
        self.sprite = None
        self.lifes = 1
        self.speed = 10
        self.size = 0
        self.player = player.Player()

    def die(self):
        self.lifes = 0

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        self.size = a_size

    def move(self, direccion):
        for index in range(len(self.position)):
            self.position[index] = self.position[index] + direccion[index]

    def setLifes(self, lifeAmmount):
        self.lifes = lifes_ammount

    def setSpeed(self, speedAmmount):
        self.player.setSpeed(speedAmmount)
