from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()  # Remove the asteroid if it's too small to split
        else:
            # Generate random angles for the new velocities
            random_angle = random.uniform(20, 30)


            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)

            offset_distance = self.radius / 2
            first_position = self.position + first_vector.normalize() * offset_distance
            second_position = self.position + second_vector.normalize() * offset_distance

            # Create new smaller asteroids
            first_asteroid = Asteroid(first_position.x, first_position.y, self.radius - ASTEROID_MIN_RADIUS)
            first_asteroid.velocity = first_vector * 1.2

            second_asteroid = Asteroid(second_position.x, second_position.y, self.radius - ASTEROID_MIN_RADIUS)
            second_asteroid.velocity = second_vector * 1.2

            # Add the new asteroids to their respective groups
            for container in self.containers:
                container.add(first_asteroid, second_asteroid)

            # Kill the original asteroid
            self.kill()