import pygame

QUIT = False


def process_events():
    global QUIT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
