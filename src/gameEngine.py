import pygame
import game
import background

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.dimensions = [925, 555]
        self.game = game.Game()

        self.background = background.Background(self.dimensions, self.game)
        self.loadImages()

        # Creo obstaculos para despues en reload background dibujarlos y alli setear el rect de cada uno
        self.game.createObstacles(self.dimensions)
        self.game.placeEnemies()
        self.background.reloadBackground(self.dimensions)
        self.game.createRects()

        self.mainLoop()

    def esc():
        pass

    def goMenu():
        pass

    def goOption():
        pass

    def exit():
        pass

    def loadImages(self):
        self.background.loadBombermanImage('sprites/BombermanAnimado/', (37, 37))  # Lo pone al principio del mapa
        self.background.loadObstacle("sprites/pilar.png")
        self.background.loadImagenMenu("sprites/MenuBomberman.png")
        self.background.loadBackgroundImage("sprites/pasto.png")
        # self.background.loadStartMenu("sprites/pressStart.png")
        self.background.loadEnemigoBomberman("sprites/enemigoBomberman.png")

    def mainLoop(self):
        menu = True
        clock = pygame.time.Clock()
        contador = 0
        while True:
            while menu:
                print("Entro al loopeano")
                self.background.reloadMenu()
                clock.tick(30)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        print("Salgo del loopeano")
                        menu = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    contador += 1
                    if contador > 3:
                        contador = 0
                    self.background.reloadBackgroundImage()

                    self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    self.background.reloadBombermanRect()

                    self.background.reloadBackground(self.dimensions)

                    playerrect = self.game.getPlayerRect()

                    # print(len(self.game.lalistaderects))

                    # print(playerrect.collidelistall(self.game.getListaDeRects()))

                    if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0:
                        self.game.setBombermanPosition()

                    self.background.reloadBomberman(
                        self.game.getBombermanDirection(), contador
                        )
                    self.game.moverEnemigo()
                    self.background.reloadEnemyRect()
                    self.background.reloadEnemy()
                pygame.display.flip()
                clock.tick(30)

                if event.type == pygame.KEYUP:
                    self.background.idleBobmerman(
                        self.game.getBombermanDirection()
                        )

if __name__ == "__main__":
    controlador = GameEngine()
