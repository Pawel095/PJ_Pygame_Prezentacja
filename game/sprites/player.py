import pygame

import events
from loader import assets

from .__base import Base
from .bullets import Bullet


class Player(Base):
    def __init__(self, *args, **kwargs):
        sprite = assets.get("player")
        sprite = pygame.transform.rotozoom(sprite, 180, 0.50)

        self.shoot_cooldown = 0.5
        self.shoot_cooldown_timer = 0

        super().__init__(sprite, speed=500, position=(400, 300), *args, **kwargs)

    def approach(self, current, target, step=0.1):
        delta = target - current
        return current + delta * step

    def update_timers(self, deltaT):
        self.shoot_cooldown_timer += deltaT

    def shooting(self):
        if events.SHOOT:
            if self.shoot_cooldown_timer >= self.shoot_cooldown:
                self.shoot_cooldown_timer = 0
                Bullet("bullet", self.position, velocity=(0, -400), shooter="p")

    def movement(self):
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

    def update(self, deltaT):
        self.update_timers(deltaT)
        self.movement()
        self.shooting()
        super().update(deltaT)

    def draw(self):
        super().draw()
