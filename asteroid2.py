from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random
import math

class Asteroid:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(50, 150)
        self.vertices = self.generate_polygon()

   

    def generate_polygon(self):
        num_vertices = random.randint(8, 12)  # Number of points in the asteroid
        vertices = []
        for i in range(num_vertices):
            angle = random.uniform(0, 360)  # Random angle in degrees
            distance = random.uniform(self.radius * 0.6, self.radius)  # Random distance from center
            x = self.position.x + distance * math.cos(math.radians(angle))
            y = self.position.y + distance * math.sin(math.radians(angle))
            vertices.append((x, y))
        return vertices


    def draw(self, screen):
        # Draw the polygon representing the asteroid
        pygame.draw.polygon(screen, "white", self.vertices, width=2)

    def update(self, dt):
        # Update position
        self.position += self.velocity * dt

        # Move vertices with the asteroid
        self.vertices = [
            (vertex[0] + self.velocity.x * dt, vertex[1] + self.velocity.y * dt)
            for vertex in self.vertices
        ]

    def rotate(self, angle):
        # Rotate the vertices around the asteroid's center
        center = self.position
        angle_radians = pygame.math.radians(angle)
        cos_theta = pygame.math.cos(angle_radians)
        sin_theta = pygame.math.sin(angle_radians)
        self.vertices = [
            (
                cos_theta * (vertex[0] - center.x) - sin_theta * (vertex[1] - center.y) + center.x,
                sin_theta * (vertex[0] - center.x) + cos_theta * (vertex[1] - center.y) + center.y
            )
            for vertex in self.vertices
        ]


    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            random_angle = random.uniform(20, 30)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)

            # First asteroid
            first_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            first_asteroid.velocity = first_vector * 1.2

            # Second asteroid
            second_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            second_asteroid.velocity = second_vector * 1.2

            # Add to sprite groups
            for container in self.containers:
                container.add(first_asteroid, second_asteroid)

            # Kill the current asteroid
            self.kill()
