import pygame

# Wall class
class Point:
    def __init__(self, x, y, radius, color, surface):
        self.color = color
        self.surface = surface
        self.x = x+32
        self.y = y+32
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.polygon(self.surface, (150, 200, 100),[(self.x, self.y - 15), (self.x, self.y - 5), (self.x + 10, self.y - 15)])

