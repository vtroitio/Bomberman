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
        self.movimientoizquierda = None
        self.enemigobomberman = None

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
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (0, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador], self.game.getBombermanPosition())

    def reloadBackgroundImage(self):
        self.screen.blit(self.background, (0, 0))

    def reloadBombermanRect(self):
        rect = pygame.draw.rect(self.screen, (0, 0, 0), self.game.getPlayerHitbox(), 2)
        self.game.setPlayerRect(rect)

    def reloadMenu(self):
        self.screen.fill(self.blue)
        self.screen.blit(self.imagenmenu, (0, 0))

    def reloadEnemy(self):
        for enemy in self.game.getListaDeEnemigos():
            self.screen.blit(self.enemigobomberman, enemy.getEnemyPosition())

    def reloadEnemyRect(self):
        for enemy in self.game.getListaDeEnemigos():
            print("El hitbox del background = " + str(enemy.getEnemyHitbox()))
            cosa = pygame.draw.rect(self.screen, (0, 0, 0), enemy.getEnemyHitbox(), 1)
            enemy.setEnemyRect(cosa)
            self.game.setlalistaderectsenemigos(cosa)

# Loads

    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = {
            "up": [pygame.image.load(path + "b1.png"), pygame.image.load(path + "b2.png"), pygame.image.load(path + "b1.png"), pygame.image.load(path + "b3.png")],
            "down": [pygame.image.load(path + "f1.png"), pygame.image.load(path + "f2.png"), pygame.image.load(path + "f1.png"), pygame.image.load(path + "f3.png")],
            "left": [pygame.image.load(path + "l1.png"), pygame.image.load(path + "l2.png"), pygame.image.load(path + "l1.png"), pygame.image.load(path + "l3.png")],
            "right": [pygame.image.load(path + "r1.png"), pygame.image.load(path + "r2.png"), pygame.image.load(path + "r1.png"), pygame.image.load(path + "r3.png")]
        }
        self.screen.blit(self.bomberman["down"][0], pos)

    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path)
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

    # def loadStartMenu(self, path):
    #     self.startmenu = pygame.image.load(path)
    #     self.startmenu = pygame.transform.scale(self.startmenu, [200, 200])

    def loadmovimientoizquierda(self, path1, path2, path3, path4):
        self.movimientoizquierda = [pygame.image.load(path1), pygame.image.load(path2), pygame.image.load(path3), pygame.image.load(path4)]

    def loadEnemigoBomberman(self, path):
        self.enemigobomberman = pygame.image.load(path)
        self.enemigobomberman = pygame.transform.scale(self.enemigobomberman, [32, 32])

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)
