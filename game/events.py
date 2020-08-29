import pygame

UP = False
DOWN = False
LEFT = False
RIGHT = False
SHOOT = False
QUIT = False


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SHOOT = True

            if event.key == pygame.K_d:
                RIGHT = True
            if event.key == pygame.K_a:
                LEFT = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                SHOOT = False

            if event.key == pygame.K_d:
                RIGHT = False
            if event.key == pygame.K_a:
                LEFT = False
