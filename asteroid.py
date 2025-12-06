from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(random_angle)
            asteroid2.velocity = self.velocity.rotate(-random_angle)
            asteroid1.velocity *= 1.2
            asteroid2.velocity *= 1.2
            
            
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)