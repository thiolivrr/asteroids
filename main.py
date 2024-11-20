import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    print("--Starting asteroids!--")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    player = Player(x, y)
    AsteroidField()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game Over!") 
                return
        screen.fill('#000000')
        tick = clock.tick(60)
        dt = tick / 1000
        for obj in drawable : obj.draw(screen)
        for obj in updatable: obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                return
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()
            
        pygame.display.flip()
        
if __name__ == "__main__":
    main()