import pygame
import game
import background

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.game = game.Game()
        self.dimensions = [925, 555]
        self.background = background.Background(self.dimensions, self.game)
        self.loadImages()
        self.game.createObstacles(self.dimensions)
        self.background.reloadBackground(self.dimensions)
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
        self.background.loadBackgroundImage("sprites/pilar.png")
        self.background.loadBombermanImage('sprites/Bomberman.png', (37, 37))
        self.background.loadObstacle("sprites/pilar.png")

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.background.fillBlack()
                    
                    self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    # self.game.createPlayer()
                    self.background.reloadBackground(self.dimensions)
                    playerrect = self.game.getPlayerRect()
                    print(len(self.game.lalistaderects))
                    print(playerrect.collidelistall(self.game.getListaDeRects()))
                    if len(playerrect.collidelistall(self.game.getListaDeRects()))>0:
                        self.game.setBombermanPosition()
                    self.background.reloadBomberman()
                pygame.display.flip()

if __name__ == "__main__":
    controlador = GameEngine()
