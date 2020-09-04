import pygame

import events
import global_vars
import loader

pygame.init()
loader.load()

pygame.display.set_mode(global_vars.SCREEN_SIZE)
pygame.display.set_caption("Hell Of Bullets")

clk = pygame.time.Clock()
WHITE = (255, 255, 255)

running = True
while running:
    deltaT = clk.tick(60) / 1000
    events.process_events()

    if events.QUIT:
        running = False

    # PHYSICS AND CONTROLLER UPDATES

    # RENDERING
    srf = pygame.display.get_surface()
    srf.fill((0, 0, 0))

    if events.UP:
        pygame.draw.rect(srf, WHITE, (349, 210, 100, 100), 1)

    if events.DOWN:
        pygame.draw.rect(srf, WHITE, (213, 346, 100, 100), 1)
    if events.LEFT:
        pygame.draw.rect(srf, WHITE, (349, 346, 100, 100), 1)
    if events.RIGHT:
        pygame.draw.rect(srf, WHITE, (485, 346, 100, 100), 1)
    if events.SHOOT:
        pygame.draw.rect(srf, WHITE, (213, 482, 372, 100), 1)

    pygame.display.update()
