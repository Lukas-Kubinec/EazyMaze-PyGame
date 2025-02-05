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
        # Player body
        pygame.draw.rect(self.surface, self.color, self, border_radius=5)
        pygame.draw.rect(self.surface, (0, 0, 0), self,5, border_radius=5) # Player black border
        # Player Left Eye
        pygame.draw.circle(self.surface, (255, 255, 255), (int(self.x + self.width/2-8), int(self.y+18)), 12) # Left eye
        pygame.draw.circle(self.surface, (0, 0, 0), (int(self.x + self.width / 2 - 8), int(self.y + 18)), 4) # Left eye pupil
        pygame.draw.circle(self.surface, (0, 0, 0), (int(self.x + self.width / 2 - 8), int(self.y + 18)), 12, 5) # Left eye border
        # Player Right Eye
        pygame.draw.circle(self.surface, (255, 255, 255), (int(self.x + self.width/2+8), int(self.y+18)), 12)  # right eye
        pygame.draw.circle(self.surface, (0, 0, 0), (int(self.x + self.width / 2 + 8), int(self.y + 18)), 4)  # Right eye pupil
        pygame.draw.circle(self.surface, (0, 0, 0), (int(self.x + self.width / 2 + 8), int(self.y + 18)),12, 5) # Right eye border

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y