import powerUp


class LifeUp(powerUp.PowerUp):
    def __init__(self, posicion):

        super().__init__()
        self.type = "life"
        self.posicion = posicion

    def setPosicion(self, posicion):
        self.posicion = posicion

    def getPosition(self):
        return self.posicion
