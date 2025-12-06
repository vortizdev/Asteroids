from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOOT_SPEED
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = direction.normalize() * SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt