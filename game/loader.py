import logging

import pygame

assets = {}
loadingFinished = False
logger = logging.getLogger(__name__)


def load():
    global assets
    assets = {
        "bullet": pygame.image.load("assets/bullet.png"),
        "e_bullet": pygame.image.load("assets/e_bullet.png"),
        "player": pygame.image.load("assets/Ship-Blue-005.png"),
        "normal_enemy": pygame.image.load("assets/Ship-Red-001.png"),
    }
