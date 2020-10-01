import pygame

QUIT = False

UP = False
DOWN = False
LEFT = False
RIGHT = False

SHOOT = False

def process_events():
    global QUIT

    global UP
    global DOWN
    global LEFT
    global RIGHT

    global SHOOT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                UP = True
            if event.key == pygame.K_a:
                LEFT = True
            if event.key == pygame.K_s:
                DOWN = True
            if event.key == pygame.K_d:
                RIGHT = True

            if event.key == pygame.K_SPACE:
                SHOOT = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                UP = False
            if event.key == pygame.K_a:
                LEFT = False
            if event.key == pygame.K_s:
                DOWN = False
            if event.key == pygame.K_d:
                RIGHT = False

            if event.key == pygame.K_SPACE:
                SHOOT = False