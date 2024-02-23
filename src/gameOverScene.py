import pygame
import gameScene

class GameOverScene(object):
    def __init__(self):
        pass

    def render(self, background):
        background.reloadGameOverScreen()

    def update(self, background, game):
        pass

    def handleEvents(self, events, background, game):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_INSERT:
                self.manager.goTo(gameScene.GameScene())
