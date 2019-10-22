import pygame
import game
# import dynamicObject
# import powerUp
import background
import math

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.game = game.Game()
        self.dimensions = [925, 555]
        self.background = background.Background(self.dimensions, self.game)

        self.loadImages()
        self.background.reloadBackground(self.dimensions)
        self.background.reloadObstacle(self.dimensions)
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
        self.background.loadBombermanImage('sprites/BombermanAnimado.png', (37, 37))
        self.background.loadObstacle("sprites/pilar.png", (74, 74))

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    posicion = self.game.getBombermanPosition()
                    choco = False
                    nocrash = 0
                    self.background.fillBlack()
                    self.game.givePosition(CONTROLES[str(event.key)])
                    self.background.loadObstacle("sprites/pilar.png", (74, 74))

                    # Colisiones
                    for obstaculo in self.background.matriz:
                        # for index in len(self.background.matriz):
                        if event.key == 273:
                            posicion1 = posicion[1]
                            posicion2 = obstaculo[1]
                            self.background.reloadBomberman('left')
                        elif event.key == 274:
                            posicion1 = obstaculo[1]
                            posicion2 = posicion[1]
                            self.background.reloadBomberman('right')
                        elif event.key == 275:
                            posicion1 = obstaculo[0]
                            posicion2 = posicion[0]
                            self.background.reloadBomberman('up')
                        elif event.key == 276:
                            posicion1 = posicion[0]
                            posicion2 = obstaculo[0]
                            self.background.reloadBomberman('down')
                        if abs(int(posicion1 - posicion2)) >= self.game.getBombermanSpeed():
                            pass
                        else:
                            choco = True
       
                    if choco is False:
                        self.background.reloadBomberman(posicion)
                    else:
                        print("choco")
                        print(self.game.getBombermanPositionAnterior)
                        self.background.reloadBomberman(self.game.getBombermanPositionAnterior)
                        # self.background.reloadBomberman()
                        
                    self.background.reloadBackground(self.dimensions)
                    self.background.reloadObstacle(self.dimensions)
                pygame.display.flip()
                
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.background.reloadBomberman('stand_left')
                    if event.key == pygame.K_RIGHT:
                        self.background.reloadBomberman('stand_right')
                    if event.key == pygame.K_UP:
                        self.background.reloadBomberman('stand_up')
                    if event.key == pygame.K_DOWN:
                        self.background.reloadBomberman('stand_down')

if __name__ == "__main__":
    controlador = GameEngine()
#* (self.position[0] <= 888)