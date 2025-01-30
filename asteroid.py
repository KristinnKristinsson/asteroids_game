import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)
    
    def update(self, dt): 
        self.position += self.velocity * dt

    #def rotate(self, angle, dt):
     #   self.position += angle * dt

    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        if self.radius <= ASTEROID_MAX_RADIUS:
            new_angle = random.uniform(20, 50)
            self.radius -= ASTEROID_MIN_RADIUS
            asteroid_plus = Asteroid(self.position[0], self.position[1], self.radius)
            asteroid_minus = Asteroid(self.position[0], self.position[1], self.radius)
            asteroid_plus.velocity = pygame.math.Vector2.rotate(self.velocity, new_angle) * 1.2
            asteroid_minus.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angle) * 1.2



