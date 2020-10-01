import pygame
import global_vars
import events
import loader
import sprites.enemy
from sprites.Player import Player
from sprites.enemy import Controller
import sprites.bullet as bullets
from sprites.background import Background

pygame.init()
loader.load()


pygame.display.set_mode(global_vars.SCREEN_SIZE)
pygame.display.set_caption("Hell Of Bullets")

player = Player()
controller = Controller()
clk = pygame.time.Clock()
bg = Background()

WHITE = (255,255,255)

running=True
while running:
    deltaT = clk.tick(60)/1000

    events.process_events()

    if events.QUIT:
        running = False

    # Fizyka
    player.update(deltaT)
    controller.update(deltaT)
    bullets.update(deltaT)
    bg.update(deltaT)

    # RENDER
    srf = pygame.display.get_surface()
    srf.fill((0,0,0))

    player.draw()
    controller.draw()
    bullets.draw()
    bg.draw()

    pygame.display.update()
