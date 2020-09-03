from .__base import Base
import global_vars as g
import random
import pygame


class BackgroundParticle(Base):
    def __init__(self):
        super().__init__(None)
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
                0+self.size[1],
            )

    def draw(self):
        srf = pygame.display.get_surface()
        x, y = self.position
        w, h = self.size
        pygame.draw.rect(srf, (255, 255, 255), (x, y, w, h))


class Background:
    def __init__(self):
        self.particles = []
        for _ in range(30):
            self.particles.append(BackgroundParticle())

    def draw(self):
        [p.draw() for p in self.particles]

    def update(self, deltaT):
        [p.update(deltaT) for p in self.particles]
