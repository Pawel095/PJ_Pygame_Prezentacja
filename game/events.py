import pygame

UP = False
DOWN = False
LEFT = False
RIGHT = False
SHOOT = False
QUIT = False

MOVEMENT_KEY_PRESSED = False


def process_events():
    global UP
    global DOWN
    global LEFT
    global RIGHT
    global SHOOT
    global QUIT
    global MOVEMENT_KEY_PRESSED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SHOOT = True
            if event.key == pygame.K_d:
                RIGHT = True
                MOVEMENT_KEY_PRESSED = True
            if event.key == pygame.K_a:
                LEFT = True
                MOVEMENT_KEY_PRESSED = True
            if event.key == pygame.K_w:
                UP = True
                MOVEMENT_KEY_PRESSED = True
            if event.key == pygame.K_s:
                DOWN = True
                MOVEMENT_KEY_PRESSED = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                SHOOT = False
            if event.key == pygame.K_d:
                RIGHT = False
                MOVEMENT_KEY_PRESSED = False
            if event.key == pygame.K_a:
                LEFT = False
                MOVEMENT_KEY_PRESSED = False
            if event.key == pygame.K_w:
                UP = False
                MOVEMENT_KEY_PRESSED = False
            if event.key == pygame.K_s:
                DOWN = False
                MOVEMENT_KEY_PRESSED = False
