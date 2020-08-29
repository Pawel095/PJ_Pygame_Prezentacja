import pygame

from .__base import Base

bullets = []


class Bullet(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        super().draw()

