import powerUp


class LifeUp(powerUp.PowerUp):
    def __init__(self, posicion):

        super().__init__()
        self.type = "life"
        self.posicion = posicion

    def setPosicion(self, posicion):
        self.posicion = posicion

    def getPosicion(self):
        return self.posicion
