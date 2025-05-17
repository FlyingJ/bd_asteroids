import pygame

import constants as const
import player as pl

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # create sprite groups to hold updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # and add Player to both
    pl.Player.containers = (updatable, drawable)

    # now it is safe to start creating more objects
    screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))
    player = pl.Player(const.SCREEN_WIDTH/2, const.SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        # time since tick in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()