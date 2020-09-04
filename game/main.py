import pygame

import events
import global_vars


pygame.init()


pygame.display.set_mode(global_vars.SCREEN_SIZE)
pygame.display.set_caption("Hell Of Bullets")

clk = pygame.time.Clock()


fps_target = 30
last = 0
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

    pygame.display.update()
