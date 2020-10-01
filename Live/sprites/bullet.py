import pygame
import math
import loader
from sprites.__base import Base

bullets = []

class Bullet(Base):
    def __init__(self,shooter,position,velocity,acceleration):
        self.sprite = loader.assets.get("bullet")
        self.size = self.sprite.get_rect()[2:]

        self.shooter = shooter

        self.speed=300
        self.position=position
        self.velocity=velocity
        self.acceleration=acceleration

        self.alive = True
        bullets.append(self)

    def on_hit(self):
        self.alive = False

    def distance_from(self, other):
        a = self.position
        b = other.position
        return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))

    def update(self,deltaT):
        super().update(deltaT)




def update(deltaT):
    for e in bullets:
        e.update(deltaT)

    # Remove enemies that are dead or off screen
    indices_to_forget = [
        i
        for i, e in enumerate(bullets)
        if e.is_outside_screen() or not e.alive
    ]
    indices_to_forget.reverse()
    for i in indices_to_forget:
        bullets.pop(i)


def draw():
    [e.draw() for e in bullets]

def get_bullets_for_shooter(shooter):
    return [b for b in bullets if b.shooter == shooter]