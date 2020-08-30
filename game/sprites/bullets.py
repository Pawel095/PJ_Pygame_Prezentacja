from loader import assets

from .__base import Base
import global_vars

bullet_objects = []


class Bullet(Base):
    def __init__(
        self, sprte_key, position, velocity=(0, -100), shooter=None, *args, **kwargs
    ):
        sprite = assets[sprte_key]
        self.shooter = shooter
        super().__init__(sprite, position=position, velocity=velocity, *args, **kwargs)
        bullet_objects.append(self)

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        super().draw()


def draw_all_bullets():
    [b.draw() for b in bullet_objects]


def update_all_bullets(deltaT):
    # remove bullets outside the screen
    indices_to_forget = [
        i
        for i, b in enumerate(bullet_objects)
        if b.position[1] >= global_vars.SCREEN_SIZE[1]
    ]
    for i in indices_to_forget:
        del bullet_objects[i]

    [b.update(deltaT) for b in bullet_objects]
    # TODO: check for collision

