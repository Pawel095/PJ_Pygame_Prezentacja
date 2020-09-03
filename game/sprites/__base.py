from abc import ABC

import pygame


class Base(ABC):
    def __init__(
        self,
        sprite,
        speed=100,
        position=(100, 100),
        velocity=(0, 0),
        acceleration=(0, 0),
    ):
        self.sprite = sprite
        self.size = self.sprite.get_rect()[2:]
        self.hitbox_size = max(self.size)
        self.collision_radius = max(self.size) / 2
        self.speed = speed
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.alive = True
        super().__init__()

    @classmethod
    def approach(cls, current, target, step=0.1):
        delta = target - current
        return current + delta * step

    def update(self, deltaT):
        self.__linear_update(deltaT)

    def __linear_update(self, deltaT):
        px, py = self.position
        vx, vy = self.velocity
        ax, ay = self.acceleration

        self.velocity = (ax * deltaT + vx, ay * deltaT + vy)
        self.position = (
            px + vx * deltaT + 0.5 * ax * deltaT ** 2,
            py + vy * deltaT + 0.5 * ay * deltaT ** 2,
        )

    def draw(self):
        center = (
            self.position[0] - self.size[0] / 2,
            self.position[1] - self.size[1] / 2,
        )
        srf = pygame.display.get_surface()
        srf.blit(self.sprite, center)
