import powerUp


class Speed(powerUp.PowerUp):
    def __init__(self, posicion):
        super().__init__()
        self.type = "speed"
        self.duracion = 10
        self.posicion = posicion

    def setPosicion(self, posicion):
        self.posicion = posicion

    def getPosition(self):
        return self.posicion
