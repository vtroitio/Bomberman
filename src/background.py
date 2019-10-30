import pygame
import game
import obstacles


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        pygame.key.set_repeat(50)

        # Loads
        self.imagenmenu = None
        self.bomberman = None
        self.obstacle = None
        self.startmenu = None
        self.movimientoizquierda = None
        self.enemigobomberman = None

        # Setear tamaño de la pantalla
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions

        self.game = game        # self.game = game.Game()
        self.blue = (0, 0, 255)
        self.contadordepasos = 0
# Reload

    def reloadBackground(self, dimensions):  # Crea las filas y columnas
        for obstaculo in self.game.getListaDeObstaculos():

            self.screen.blit(self.obstacle, obstaculo.getPosition())
            obstaculo.setObstacleRect(pygame.draw.rect(self.screen, (0, 0, 0), obstaculo.getHitbox(), 1))

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())

    def reloadBombermanRect(self):
        rect = pygame.draw.rect(self.screen, (0, 0, 0), self.game.getPlayerHitbox(), 2)
        self.game.setPlayerRect(rect)

    def reloadMenu(self):
        self.screen.fill(self.blue)
        self.screen.blit(self.imagenmenu, (0, 0))
        self.screen.blit(self.startmenu, (370, 170))

    def reloadBomberman(self, direction, contador):
        self.screen.blit(self.bomberman[direction][contador], self.game.getBombermanPosition())
    
    def reloadEnemy(self):
        for enemy in self.game.getListaDeEnemigos():
            self.screen.blit(self.enemigobomberman, enemy.getEnemyPosition())
            enemy.setEnemyRect(pygame.draw.rect(self.screen, (255, 0, 0), enemy.getEnemyHitbox(), 1))

    def reloadEnemyRect(self):
        for enemy in self.game.getListaDeEnemigos():
            cosa = pygame.draw.rect(self.screen, (255, 0, 0), enemy.getEnemyHitbox(), 1)
            enemy.setEnemyRect(cosa)
# Loads

    def loadObstacle(self, path):
        self.obstacle = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = {
            "down": [pygame.image.load(path + "f1.png"), pygame.image.load(path + "f2.png"), pygame.image.load(path + "f1.png"), pygame.image.load(path + "f3.png")],
            "up": [pygame.image.load(path + "b1.png"), pygame.image.load(path + "b2.png"), pygame.image.load(path + "b1.png"), pygame.image.load(path + "b3.png")],
            "left": [pygame.image.load(path + "l1.png"), pygame.image.load(path + "l2.png"), pygame.image.load(path + "l1.png"), pygame.image.load(path + "l3.png")],
            "right": [pygame.image.load(path + "r1.png"), pygame.image.load(path + "r2.png"), pygame.image.load(path + "r1.png"), pygame.image.load(path + "r3.png")]
            }
        self.screen.blit(self.bomberman["down"][0], pos)

    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path)
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

    def loadStartMenu(self, path):
        self.startmenu = pygame.image.load(path)
        self.startmenu = pygame.transform.scale(self.startmenu, [200, 200])

    def loadEnemigoBomberman(self, path):
        self.enemigobomberman = pygame.image.load(path)
        self.enemigobomberman = pygame.transform.scale(self.enemigobomberman, [40, 40])
    
    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)

# Etc

    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)
