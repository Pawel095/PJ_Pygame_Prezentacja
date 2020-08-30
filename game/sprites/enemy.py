from loader import assets
import random
import global_vars

from .__base import Base
from .bullets import Bullet


class Enemy(Base):
    def __init__(self, sprite_key):
        sprite = assets[sprite_key]
        self.alive = True
        super().__init__(sprite, speed=300, position=(400, 100))

    def update(self, deltaT):
        super().update(deltaT)

    def draw(self):
        super().draw()

    def can_be_forgotten(self):
        pass


class Normal(Enemy):
    def __init__(self):
        super().__init__("normal_enemy")
        randx = random.randint(self.size[0], global_vars.SCREEN_SIZE[0] - self.size[0])
        self.position = (randx, -self.size[1])
        self.shoot_cooldown = 1
        self.shoot_cooldown_timer = 0
        self.velocity = (0, 50)

    def shoot(self):
        if self.shoot_cooldown_timer >= self.shoot_cooldown:
            self.shoot_cooldown_timer = 0
            Bullet("e_bullet", self.position, (0, 300), shooter="e")

    def update(self, deltaT):
        self.shoot_cooldown_timer += deltaT
        self.shoot()
        super().update(deltaT)


class Controller:
    enemies = []

    def __init__(self):
        self.cooldown = {
            "normal": 3,
            "turret": 10,
        }
        self.cooldown_timers = {
            "normal": 0,
            "turret": 0,
        }
        self.enemy_types = {
            "normal": Normal,
            "turret": Normal,
        }

    def spawn_enemies(self):
        for k, i in self.cooldown.items():
            if self.cooldown_timers[k] >= self.cooldown[k]:
                self.cooldown_timers[k] = 0
                e = self.enemy_types[k]()
                self.enemies.append(e)

    def update(self, deltaT):
        [e.update(deltaT) for e in self.enemies]
        for k, i in self.cooldown_timers.items():
            self.cooldown_timers[k] += deltaT

        self.spawn_enemies()
        # TODO: Remove dead enemies

    def draw_all_enemies(self):
        [e.draw() for e in self.enemies]
