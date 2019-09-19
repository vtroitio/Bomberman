import powerUp


class Speed(powerUp):
    def __init__(self, duracionSpeed):
        self.duracion = duracionSpeed + 5
        super().__init__(self)

    def establecer_efecto(self, personajeQueLoAgarra):
        personajeQueLoAgarra.setSpeed(10)

    def powerUpTime(self):
        pass
