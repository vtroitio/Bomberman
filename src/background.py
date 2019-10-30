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

    def reloadEnemy(self):
        for enemy in self.game.getListaDeEnemigos():
            print(enemy.getEnemyPosition())
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
        self.bomberman = pygame.image.load(path)
        self.bomberman = pygame.transform.scale(self.bomberman, [30, 30])
        self.screen.blit(self.bomberman, pos)

    def loadImagenMenu(self, path):
        self.imagenmenu = pygame.image.load(path)
        self.imagenmenu = pygame.transform.scale(self.imagenmenu, [925, 555])

    def loadStartMenu(self, path):
        self.startmenu = pygame.image.load(path)
        self.startmenu = pygame.transform.scale(self.startmenu, [200, 200])

    def loadmovimientoizquierda(self, path1, path2, path3, path4):
        self.movimientoizquierda = [pygame.image.load(path1), pygame.image.load(path2), pygame.image.load(path3), pygame.image.load(path4)]

    def loadEnemigoBomberman(self, path):
        self.enemigobomberman = pygame.image.load(path)
        self.enemigobomberman = pygame.transform.scale(self.enemigobomberman, [40, 40])

# Etc
    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)
