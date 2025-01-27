# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    triangle_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    fps = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        triangle_player.draw(screen)
        pygame.display.flip()
        fps.tick(60)
        dt = (fps.tick(60)/1000)

    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")

if __name__ == "__main__":
    main()
