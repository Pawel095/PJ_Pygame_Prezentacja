import pygame

assets = {}

def load():
    global assets

    assets={
        "player":pygame.image.load("assets/Ship-Blue-004.png"),
        "enemy":pygame.image.load("assets/Ship-Red-001.png"),
        "bullet":pygame.image.load("assets/bullet.png"),
    }