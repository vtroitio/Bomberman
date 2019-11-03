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

       
        self.game.createObstacles(self.dimensions)   # Creo obstaculos para despues en reload background dibujarlos y alli setear el rect de cada uno
        self.game.placeEnemies()
        self.background.reloadEnemyRect()
        self.background.reloadBackground(self.dimensions)
        self.game.createRects()
        self.menu = True

        self.mainLoop()

    def intro(self):
        clock = pygame.time.Clock()
        while self.menu:
            self.background.reloadMenu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    clock.tick(30)
                    self.menu = False
                    pygame.display.update()

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
        clock = pygame.time.Clock()
        contador = 0
        eventomovimientoenemigos = pygame.USEREVENT
        while True:
            while self.menu:
                self.intro()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if self.game.getBombermanPositionAnterior() != self.game.getBombermanPosition():
                        contador += 1
                    if contador > 3:
                        contador = 0
                    
                    self.background.reloadBackgroundImage()

                    self.game.givePosition((CONTROLES[str(event.key)]), self.background.screen)
                    self.background.reloadBombermanRect()

                    self.background.reloadBackground(self.dimensions)
                    pygame.display.update()

                    playerrect = self.game.getPlayerRect()


                    if len(playerrect.collidelistall(self.game.getListaDeRects())) > 0:  # Colision Bomberman//
                        self.game.setBombermanPosition()
                    self.background.reloadBomberman(self.game.getBombermanDirection(), contador)
                    
                     
                    self.game.moverEnemigo()
                    self.background.reloadEnemy()
                    self.background.reloadEnemyRect() 



                    enemyrect = self.game.getEnemyRect() 
                    print("Estos son mis rects " + str(enemyrect))

                    for i in range(0, len(enemyrect)):
                        if len(enemyrect[i].collidelistall(self.game.getListaDeRects())) > 0:  # Colision enemigos//
                            print("Me colisione wachin " + str(i))
                            self.game.setdireccionenemigo(self.game.getdireccionenemigo(i) * -1, i)
                            print("Le cambie la posicion a " + str(self.game.getdireccionenemigo(i)))
                            self.game.setPositionAnterior()
                    



                    
                pygame.display.flip()
                clock.tick(30)

                if event.type == pygame.KEYUP:
                    self.background.reloadBomberman(self.game.getBombermanDirection(), 0)

if __name__ == "__main__":
    controlador = GameEngine()
