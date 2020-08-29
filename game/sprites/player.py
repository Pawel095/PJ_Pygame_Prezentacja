import pygame

import events
from loader import assets

from .__base import Base


class Player(Base):
    def __init__(self, *args, **kwargs):
        sprite = assets.get("player")
        sprite = pygame.transform.rotozoom(sprite, 180, 0.50)
        super().__init__(sprite, speed=500, position=(0, 0), *args, **kwargs)

    def approach(self, current, target, step=0.1):
        delta = target - current
        return current + delta * step

    def update(self, deltaT):
        vx, vy = self.velocity

        dx, dy = (0, 0)
        if events.LEFT:
            dx += -1
        if events.RIGHT:
            dx += 1
        if events.UP:
            dy += -1
        if events.DOWN:
            dy += 1

        dx *= self.speed
        dy *= self.speed
        vx = self.approach(vx, dx)
        vy = self.approach(vy, dy)

        self.velocity = (vx, vy)
        super().update(deltaT)

    def draw(self):

