import powerUp


class BombUp(powerUp.PowerUp):
    def __init__(self, posicion):
        super().__init__()
        self.posicion = posicion

    def setPosicion(self, posicion):
        self.posicion = posicion

    def getPosition(self):
        return self.posicion
