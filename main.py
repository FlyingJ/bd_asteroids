import pygame

import constants as const

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        # time since tick in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
