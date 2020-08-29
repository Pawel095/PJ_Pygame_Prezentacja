import logging

import pygame

import events
import loader
from sprites import Player

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

loader.load()
pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hell of Bullets")

clk = pygame.time.Clock()
player = Player()


fps_target = 30
last = 0
running = True
while running:
    deltaT = clk.tick(60) / 1000
    events.process_events()

    if events.QUIT:
        running = False

    # PHYSICS UPDATES
    player.update(deltaT)

    # RENDERING
    srf = pygame.display.get_surface()
    srf.fill((0, 0, 0))

    player.draw()

    pygame.display.update()
