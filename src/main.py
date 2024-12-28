# TODO: create a skeleton for game interface

import pygame
from random import randint

# general
pygame.init()
WINDOW_HEIGHT, WINDOW_WIDTH = 1281, 720
display_surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
caption = pygame.display.set_caption("Shooters")
running = True

surf = pygame.Surface((100, 200))
surf.fill("blue")
x = 100

# loading an image
player_surf = pygame.image.load(
    "/home/bimal10/Desktop/Zombies/space shooter/images/player.png"
).convert_alpha()
star_surf = pygame.image.load(
    "/home/bimal10/Desktop/Zombies/space shooter/images/star.png"
).convert_alpha()
star_positions = [
    (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)
]


# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray42")
    x += 0.5
    display_surface.blit(player_surf, (x, 150))
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    pygame.display.update()
