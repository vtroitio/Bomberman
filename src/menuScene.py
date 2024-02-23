import pygame
import gameScene

class MenuScene(object):
    def __init__(self):
        pass

    def render(self, background):
        background.reloadMenu()

    def update(self, background, game):
        pass

    def handleEvents(self, events, background, game):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.manager.goTo(gameScene.GameScene(background, game))
