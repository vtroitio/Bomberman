import pygame
import game
import dynamicObject
import powerUp

CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class GameEngine():
    def __init__(self):
        self.game = game.Game()

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

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.game.givePosition(CONTROLES[str(event.key)])
