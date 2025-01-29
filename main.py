# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    ast_field = AsteroidField()
    triangle_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    fps = pygame.time.Clock()
    dt = 0

    
    #screen.containers = (drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        
        for obj in updatable:
            obj.update(dt)
            
            print(triangle_player.cooldown)
        for asteroid in asteroids:
            if triangle_player.collision(asteroid):
                print("Game Over!")
                pygame.time.delay(500)
                pygame.quit()
        for obj in drawable:
            obj.draw(screen) 
            

        pygame.display.flip()
        fps.tick(60)
        dt = (fps.tick(60)/1000)

    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")

if __name__ == "__main__":
    main()
