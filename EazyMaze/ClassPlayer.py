import pygame

# Player Class
class Player(pygame.Rect):
    def __init__(self, x, y, width, height, color, surface):
        pygame.Rect.__init__(self, x, y, width, height)
        self.color = color
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move_direction(self, x, y):
        #self.move_ip(x,y)
        self.x += x
        self.y += y

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self)

    def get_position(self):
        return self.x, self.y