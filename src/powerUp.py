import item
import speed


class PowerUp(item.Item):
    def __init__(self):
        super().__init__()
        self.type = None

    def getType(self):
        pass
