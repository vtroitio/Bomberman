import pygame
import game
import background

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}
#             arriba          abajo          derecha        izquierda


class GameEngine():
    def __init__(self):
        self.game = game.Game()
        self.dimensions = [925, 555]
        self.background = background.Background(self.dimensions, self.game)
        self.loadImages()
        self.background.reloadBackground(self.dimensions)
        self.background.reloadObstacle(self.dimensions)
        self.mainLoop()
        self.clock = pygame.time.Clock()

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
        self.background.loadBombermanImage("sprites/BombermanAnimado/", (37, 37))
        self.background.loadObstacle("sprites/pilar.png")
        self.background.loadImagenMenu("sprites/fondoBombmanMenu.jpeg")
        self.background.loadStartMenu("sprites/pressStart.png")
        self.background.loadEnemigoBomberman("sprites/enemigoBomberman.png")

    def mainLoop(self):
        contadorMuyLoco = 0
        while True:
            contadorMuyLoco += 1
            if contadorMuyLoco > 3:
                contadorMuyLoco = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.background.fillBlack()
                    self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    self.game.createObstacles()
                    self.background.reloadObstacle(self.dimensions)
                    self.background.reloadBackground(self.dimensions)
                    self.background.reloadBomberman(self.game.getBombermanDirection(), contadorMuyLoco)
                pygame.display.flip()

if __name__ == "__main__":
    controlador = GameEngine()
