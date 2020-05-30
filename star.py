import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.slower = 0
        direction = random.choice([-1, 1])
        self.x_speed = random.randint(2, 4) * direction
        self.y_speed = random.randint(2, 4) * direction

    def check_edges(self, screen):
        """Check if a star is at edge of screen."""
        rect = screen.get_rect()
        if self.x > rect.right:
            self.x = 0
        if self.x < rect.left:
            self.x = rect.right
        if self.y > rect.bottom:
            self.y = 0
        if self.y < rect.top:
            self.y = rect.bottom

    def update(self, screen):
        self.check_edges(screen)
        if self.slower == 8:
            self.x = self.x + self.x_speed 
            self.y = self.y + self.y_speed 
            self.slower = 0
        else:
            self.slower += 1
    
    def draw(self, screen):
        pygame.draw.lines(screen, WHITE, True, [(self.x,self.y),(self.x+1, self.y+1)])


def random_stars(num, width, height):
    mystars = []
    for _ in range(num):
        x = random.randint(0, width)
        y = random.randint(0, height)
        mystars.append(Star(x,y))
    return mystars