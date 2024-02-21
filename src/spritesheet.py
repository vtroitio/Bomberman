import pygame

class SpriteSheet():
    def __init__(self, sheet: pygame.Surface, sprite_width: int, sprite_height: int, sprite_scale = 1.0):
        self.x = 0
        self.y = 0
        self.sheet = sheet
        self.width = self.sheet.get_size()[0]
        self.height = self.sheet.get_size()[1]
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprite_width_count = self.width // self.sprite_width
        self.sprite_height_count = self.height // self.sprite_height
        self.sprite_scale = sprite_scale

    def getSprites(self):
        sprites = ([],[],[]) if self.sprite_height_count > 1 else []
        for y in range(self.sprite_height_count):
            for x in range(self.sprite_width_count):
                sprite_area = pygame.Rect(self.x, self.y, self.sprite_width, self.sprite_height)
                sprite = pygame.Surface(sprite_area.size, pygame.SRCALPHA, 32).convert_alpha()
                sprite.blit(self.sheet, (0, 0), sprite_area)

                self.x += self.sprite_width
                if self.x >= self.width:
                    self.x = 0
                    self.y += self.sprite_height
                
                if self.sprite_scale != 1.0:
                    scaled_sprite = pygame.transform.scale(sprite, (self.sprite_width * self.sprite_scale, self.sprite_height * self.sprite_scale))
                    sprites[y].append(scaled_sprite) if self.sprite_height_count > 1 else sprites.append(scaled_sprite)
                else:
                    sprites[y].append(sprite) if self.sprite_height_count > 1 else sprites.append(sprite)

        return sprites
