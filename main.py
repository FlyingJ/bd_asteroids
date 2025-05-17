import pygame
import sys

import constants as const

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # create sprite groups to hold updatable and drawable objects
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # and add Player to both
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    # now it is safe to start creating more objects
    screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
    player = Player(const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game Over!")
                sys.exit(0)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # time since tick in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()