from constants import *
import pygame
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.checkCollisions(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.checkCollisions(bullet):
                    bullet.kill()
                    obj.split()

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
