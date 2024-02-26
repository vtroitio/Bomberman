import menuScene

class SceneMananger(object):
    def __init__(self):
        self.goTo(menuScene.MenuScene())

    def goTo(self, scene):
        if hasattr(self, "scene"):
            del self.scene
        self.scene = scene
        self.scene.manager = self
