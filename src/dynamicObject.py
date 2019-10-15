class DynamicObject():
    def __init__(self):
        self.position = [37, 37]
        self.hitbox = ()
        self.sprite = None
        self.lifes = 3
        self.speed = 10
        self.sheet = None
        self.rect = None
        self.currentFrame = 0
        self.frames = 8
        self.frameWidth = 1
        self.frameHeith = 1
        self.x = self.position[0]
        self.y = self.position[1]

    def die(self):
        pass

    def setPosition(self, aPosition):
        pass

    def setSize(self, a_size):
        pass

# Movimiento

    def move(self, direccion):
        pass

    def setLifes(self, lifeAmmount):
        pass

    def setSpeed(self, speedAmmount):
        pass
