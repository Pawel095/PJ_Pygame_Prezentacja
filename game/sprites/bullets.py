from loader import assets

from .__base import Base

bullet_objects = []


class Bullet(Base):
    def __init__(self, sprte_key, position, velocity=(0, -100), *args, **kwargs):
        sprite = assets[sprte_key]
        super().__init__(sprite, position=position, velocity=velocity, *args, **kwargs)
        bullet_objects.append(self)

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        super().draw()


def draw_all_bullets():
    [b.draw() for b in bullet_objects]


def update_all_bullets(deltaT):
    [b.update(deltaT) for b in bullet_objects]
