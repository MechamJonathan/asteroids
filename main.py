import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
     pygame.init()
     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     clock = pygame.time.Clock()
     updateable = pygame.sprite.Group()
     drawable = pygame.sprite.Group()
     asteroids = pygame.sprite.Group()
     shots = pygame.sprite.Group()
     Player.containers = (updateable, drawable)
     Asteroid.containers = (asteroids, updateable, drawable)
     AsteroidField.containers = (updateable)
     Shot.containers = (shots, updateable, drawable)
     player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
     asteroid_field = AsteroidField()
     dt = 0


     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over !")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")
        for obj in drawable:
            if obj.draw(screen):
                print("Game Over!")
                SystemExit()
    
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()