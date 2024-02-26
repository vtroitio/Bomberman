import pygame
import game
import background
import sceneManager

class Init():
    def __init__(self):
        self.DIMENSIONS = (925, 555)
        self.game = game.Game()
        self.background = background.Background(self.DIMENSIONS, self.game)
        self.manager = sceneManager.SceneMananger()

        self.loadImages()
    
        self.game.createObstacles(self.DIMENSIONS)   # Creo los pilares y los bordes (solo hace falta crearlos una vez -> no van a estar en crearNivel() )
        self.background.reloadBackground() # Les asigno su rect a los pilares

        self.gameLoop()

    def loadImages(self):
        self.background.loadBombermanImage('sprites/BombermanAnimado.png', (37, 37))  # Lo pone al principio del mapa
        self.background.loadBombermanDeathImage('sprites/BombermanMuerto.png')
        self.background.loadObstacle("sprites/pilar.png")
        self.background.loadImagenMenu("sprites/MenuBomberman.png")
        self.background.loadBackgroundImage("sprites/pasto.png")
        self.background.loadEnemigoBomberman("sprites/EnemigoBombermanAnimado.png")
        self.background.loadCaja("sprites/caja.png")
        self.background.loadBomba("sprites/Bomba Animada.png")
        self.background.loadSpeedPowerUp("sprites/PowerUps/SpeedUp2.png")
        self.background.loadGameOverScreen("sprites/GameOver.jpg")
        self.background.loadBombPowerUp("sprites/PowerUps/BombUp2.png")
        self.background.loadLifePowerUp("sprites/PowerUps/HealthUp2.png")
        self.background.loadExplosion("sprites/Explosion.png")
        self.background.loadSalida("sprites/Salida.png")
        self.background.loadWinScreen("sprites/victory.jpg")

    def gameLoop(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(60)
            if pygame.event.get(pygame.QUIT):
                running = False
                return

            self.manager.scene.handleEvents(pygame.event.get(), self.background, self.game)
            self.manager.scene.render(self.background)
            self.manager.scene.update(self.background, self.game)


            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Init()
