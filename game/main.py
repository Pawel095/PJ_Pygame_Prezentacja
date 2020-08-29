from time import sleep
from timeit import default_timer as time

import events

import pygame
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hell of Bullets")


fps_target = 30
last = 0
running = True
while running:
    now = time()
    events.process_events()

    if events.quit:
        running = False

    limiter_wait = True
    waited_times = 0
    while limiter_wait:
        sleep(1 / 480)
        waited_times += 1
        if time() - now >= 1 / fps_target:
            limiter_wait = False

    last = now
