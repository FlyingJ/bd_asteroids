import pygame

import constants as const

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        pygame.display.flip()
    # print("Starting Asteroids!")
    # print(f"Screen width: {const.SCREEN_WIDTH}")
    # print(f"Screen height: {const.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
