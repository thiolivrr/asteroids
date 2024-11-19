from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame
from constants import PLAYER_SHOOT_SPEED

class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt * PLAYER_SHOOT_SPEED
    
    def rotate(self, dt):
        self.rotation *= dt