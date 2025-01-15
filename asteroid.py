import pygame
import random
from pygame.math import *
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.random_angle = random.uniform(20, 50)
        new_r = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroid(self.position.x, self.position.y, new_r)
        new1.velocity = self.velocity.rotate(self.random_angle) * 1.2
        new2 = Asteroid(self.position.x, self.position.y, new_r)
        new2.velocity = self.velocity.rotate(-self.random_angle) * 1.2
