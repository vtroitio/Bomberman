class DynamicObject():

    def __init__(self):
        self.position = [0, 0]
        self.hitbox = ()
        self.sprite = None
        self.lifes = 1
        self.speed = 10

    def die(self):
        pass

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        pass

    def move(self, direccion):
        for index in range(len(self.position)):
            self.position[index] = self.position[index] + direccion[index]

    def setLifes(self, lifeAmmount):
        self.lifes = lifes_ammount

    def setSpeed(self, speedAmmount):
        pass  # Lo dejamos así porque pinta
