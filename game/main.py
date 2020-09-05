import pygame

import events
import global_vars
import loader
from sprites import enemy
from sprites.player import Player

pygame.init()
loader.load()

pygame.display.set_mode(global_vars.SCREEN_SIZE)
pygame.display.set_caption("Hell Of Bullets")

clk = pygame.time.Clock()
player = Player()
enemy_spawn_ctrl = enemy.Controller()



running = True
while running:
    deltaT = clk.tick(60) / 1000
    events.process_events()

    if events.QUIT:
        running = False

    # PHYSICS AND CONTROLLER UPDATES
    player.update(deltaT)
    enemy_spawn_ctrl.update(deltaT)

    # RENDERING
    srf = pygame.display.get_surface()
    srf.fill((0, 0, 0))

    player.draw()
    enemy_spawn_ctrl.draw_all_enemies()

    pygame.display.update()
