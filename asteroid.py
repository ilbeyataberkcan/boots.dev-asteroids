import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)   
        

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split") 
        random_angle = random.uniform(20, 50)

        child1_angle = self.velocity.rotate(random_angle)
        child2_angle = self.velocity.rotate(-random_angle)
        child_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, child_asteroid_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_asteroid_radius)

        child1.velocity = child1_angle * 1.2
        child2.velocity = child2_angle * 1.2
