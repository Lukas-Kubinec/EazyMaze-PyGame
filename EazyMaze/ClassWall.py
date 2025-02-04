import pygame

# Wall class
class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color, surface):
        pygame.Rect.__init__(self, x, y, width, height)
        self.color = color
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self)

