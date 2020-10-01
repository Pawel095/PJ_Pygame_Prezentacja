import random

import pygame

import global_vars as g

from sprites.__base import Base

class BackgroundParticle(Base):
    def __init__(self):
        super().__init__()
        self.position = (
            random.randint(0, g.SCREEN_SIZE[0]),
            random.randrange(0, g.SCREEN_SIZE[1]),
        )
        self.velocity = (0, random.randrange(10, 400))
        self.size = (random.randint(4, 7), random.randint(4, 7))

    def update(self, deltaT):
        super().update(deltaT)
        if self.is_outside_screen():
            self.position = (
                random.randint(0, g.SCREEN_SIZE[0]),
                0 + self.size[1],
            )
    
    def draw(self):
        srf = pygame.display.get_surface()
        x, y = self.position
        w, h = self.size
        pygame.draw.rect(srf, (255, 255, 255), (x, y, w, h))


class Background:
    particles = []
    def __init__(self):
        for i in range(30):
            self.particles.append(BackgroundParticle())
    

    def update(self, deltaT):
        for e in self.particles:
            e.update(deltaT)

    def draw(self):
        [e.draw() for e in self.particles]