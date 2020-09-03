import pygame

import events
import global_vars
import loader
from sprites import bullets
from sprites import enemy
from sprites.background import Background
from sprites.player import Player


pygame.init()
loader.load()

pygame.display.set_mode(global_vars.SCREEN_SIZE)
pygame.display.set_caption("Hell Of Bullets")

clk = pygame.time.Clock()
player = Player()
bg = Background()
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
    bg.update(deltaT)

    # RENDERING
    srf = pygame.display.get_surface()
    srf.fill((0, 0, 0))

    bg.draw()
    player.draw()
    bullets.draw_all_bullets()
    enemy_spawn_ctrl.draw_all_enemies()

    pygame.display.update()
