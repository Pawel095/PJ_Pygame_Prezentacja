import logging

import pygame

import events
import loader
from sprites import bullets
from sprites import enemy
from sprites.player import Player

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

loader.load()
pygame.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hell of Bullets")

clk = pygame.time.Clock()
player = Player()

enemy_spawn_ctrl = enemy.Controller()

fps_target = 30
last = 0
running = True
while running:
    deltaT = clk.tick(60) / 1000
    events.process_events()

    if events.QUIT:
        running = False

    # PHYSICS AND CONTROLLER UPDATES
    player.update(deltaT)
    bullets.update_all_bullets(deltaT)
    enemy_spawn_ctrl.update(deltaT)

    # RENDERING
    srf = pygame.display.get_surface()
    srf.fill((0, 0, 0))

    player.draw()
    bullets.draw_all_bullets()
    enemy_spawn_ctrl.draw_all_enemies()

    pygame.display.update()