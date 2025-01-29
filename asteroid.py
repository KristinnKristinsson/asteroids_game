import pygame
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.radius = random.randrange(5,10)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)
    
    def update(self, dt):
        
        self.position += self.velocity * dt
    

