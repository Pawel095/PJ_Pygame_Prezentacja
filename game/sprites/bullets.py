import math

import global_vars
import loader

from .__base import Base

bullet_objects = []


class Bullet(Base):
    def __init__(
        self, sprte_key, position, velocity=(0, -100), shooter=None, *args, **kwargs
    ):
        sprite = loader.assets[sprte_key]
        self.shooter = shooter
        super().__init__(sprite, position=position, velocity=velocity, *args, **kwargs)
        bullet_objects.append(self)

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        super().draw()

    def distance_from(self, other):
        a = self.position
        b = other.position
        return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

    def on_hit(self):
        self.alive = False


def draw_all_bullets():
    [b.draw() for b in bullet_objects]


def update_all_bullets(deltaT):
    # remove bullets that are dead and outside the screen
    indices_to_forget = [
        i for i, b in enumerate(bullet_objects) if b.is_outside_screen() or not b.alive
    ]
    # remove from biggest index to avoid removing wrong elements
    indices_to_forget.reverse()
    for i in indices_to_forget:
        bullet_objects.pop(i)

    [b.update(deltaT) for b in bullet_objects]


def get_bullets_for_shooter(shooter):
    return [b for b in bullet_objects if b.shooter == shooter]
