import pygame

from .__base import Base

bullets = []


class Bullet(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        center = (
            self.position[0] - self.size[0] / 2,
            self.position[1] - self.size[1] / 2,
        )
        srf = pygame.display.get_surface()
        srf.blit(self.sprite, center)

