import pygame
import game
import obstacles


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        pygame.key.set_repeat(50)

        # Loads
        self.background = None
        self.imagenmenu = None
        self.bomberman = None
        self.obstacle = None
        self.startmenu = None
        self.caja = None
        self.movimientoizquierda = None
        self.enemigobomberman = None
        self.gameOverScreen = None

        # Setear tamaño de la pantalla
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions

        self.time = 0
        self.game = game        # self.game = game.Game()
        self.blue = (0, 0, 255)
        self.contadordepasos = 0
# Reload

    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for obstaculo in self.game.getListaDeObstaculos():

            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (255, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador],
                         self.game.getBombermanPosition())

    def reloadBackgroundImage(self):
        self.screen.blit(self.background, (0, 0))

    def reloadBombermanRect(self):
        rect = pygame.draw.rect(self.screen, (0, 0, 0),
                                self.game.getPlayerHitbox(), 2)
        self.game.setPlayerRect(rect)

    def reloadMenu(self):
        self.screen.fill(self.blue)
        self.screen.blit(self.imagenmenu, (0, 0))

    def reloadEnemy(self, direction, contador, numeroenemigo):
        listadeenemigos = self.game.getListaDeEnemigos()
        print(numeroenemigo)
        enemy = listadeenemigos[numeroenemigo]
        self.screen.blit(self.enemigobomberman[direction][contador], enemy.getEnemyPosition())
        enemy.setEnemyRect(pygame.draw.rect(self.screen, (255, 0, 0),
                           enemy.getEnemyHitbox(), 1))

    def idleBobmerman(self, direction):
        self.screen.blit(self.bomberman[direction][0],
                         self.game.getBombermanPosition())

    def reloadEnemyRect(self):
        for enemy in self.game.getListaDeEnemigos():
            cosa = pygame.draw.rect(self.screen, (0, 0, 0), enemy.getEnemyHitbox(), 1)
            enemy.setEnemyRect(cosa)
            self.game.setlalistaderectsenemigos(cosa)

    def reloadBoxes(self):
        for cajas in self.game.getListaDeCajas():
            self.screen.blit(self.caja, cajas.getPosition())
            cajas.setObstacleRect(pygame.draw.rect(self.screen, (0, 0, 0), cajas.getHitbox(), 1))

    def reloadBomba(self):
        self.screen.blit(self.bomba, self.game.getBombermanPosition())

    def reloadSpeedPowerUp(self):
        self.screen.blit(self.speedPowerUp, self.game.getCajaRota())

    def reloadGameOverScreen(self):
        self.screen.blit(self.gameOverScreen, (0, 0))

# Loads

    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = {
            "up": [pygame.image.load(path + "b1.png"),
                   pygame.image.load(path + "b2.png"),
                   pygame.image.load(path + "b1.png"),
                   pygame.image.load(path + "b3.png")],
            "down": [pygame.image.load(path + "f1.png"),
                     pygame.image.load(path + "f2.png"),
                     pygame.image.load(path + "f1.png"),
                     pygame.image.load(path + "f3.png")],
            "left": [pygame.image.load(path + "l1.png"),
                     pygame.image.load(path + "l2.png"),
                     pygame.image.load(path + "l1.png"),
                     pygame.image.load(path + "l3.png")],
            "right": [pygame.image.load(path + "r1.png"),
                      pygame.image.load(path + "r2.png"),
                      pygame.image.load(path + "r1.png"),
                      pygame.image.load(path + "r3.png")]
        }
        self.screen.blit(self.bomberman["down"][0], pos)

    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path)
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

    def loadCaja(self, path):
        self.caja = pygame.image.load(path)

    def loadEnemigoBomberman(self, path):
        self.enemigobomberman = {
            "vertical2": [pygame.image.load(path + "b1.png"),
                          pygame.image.load(path + "b2.png"),
                          pygame.image.load(path + "b1.png"),
                          pygame.image.load(path + "b3.png")],
            "vertical1": [pygame.image.load(path + "f1.png"),
                          pygame.image.load(path + "f2.png"),
                          pygame.image.load(path + "f1.png"),
                          pygame.image.load(path + "f3.png")],
            "horizontal2": [pygame.image.load(path + "l1.png"),
                            pygame.image.load(path + "l2.png"),
                            pygame.image.load(path + "l1.png"),
                            pygame.image.load(path + "l3.png")],
            "horizontal1": [pygame.image.load(path + "r1.png"),
                            pygame.image.load(path + "r2.png"),
                            pygame.image.load(path + "r1.png"),
                            pygame.image.load(path + "r3.png")]
        }

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)

    def loadBomba(self, path):
        self.bomba = pygame.image.load(path)

    def loadSpeedPowerUp(self, path):
        self.speedPowerUp = pygame.image.load(path)
        self.speedPowerUp = pygame.transform.scale(self.speedPowerUp, [30, 30])

    def loadGameOverScreen(self, path):
        self.gameOverScreen = pygame.image.load(path)
