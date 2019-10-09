import pygame
import game
# import dynamicObject
# import powerUp
import background

controls = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.game = game.Game()
        self.dimensions = (555, 407)
        self.background = background.Background(self.dimensions, self.game)

        self.loadImages()
        self.mainLoop()

    def esc():
        pass

    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def validatePosition():
        pass

    def loadImages(self):
        self.background.loadBackgroundImage("sprites/muro.png")
        self.background.loadBombermanImage("sprites/Bomberman.png", (37, 37))

    def update():
        pass

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.background.fillBlack()
                    self.game.givePosition(CONTROLES[str(event.key)])
                    self.background.reloadBomberman()
                    self.background.reloadBackground()
                pygame.display.flip()

if __name__ == "__main__":
    controlador = GameEngine()
