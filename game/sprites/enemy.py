import random

import global_vars as g
import loader

from .__base import Base
from .bullets import Bullet
from .bullets import get_bullets_for_shooter


class Enemy(Base):
    def __init__(self, sprite_key, *args, **kwargs):
        sprite = loader.assets[sprite_key]
        super().__init__(sprite)

    def on_hit(self, other):
        self.alive = False


class Normal(Enemy):
    def __init__(self):
        super().__init__("normal_enemy", speed=(300))
        randx = random.randint(self.size[0], g.SCREEN_SIZE[0] - self.size[0])
        self.position = (randx, -self.size[1])
        self.shoot_cooldown = 1
        self.shoot_cooldown_timer = 0
        self.velocity = (0, 50)

    def shoot(self):
        if self.shoot_cooldown_timer >= self.shoot_cooldown:
            self.shoot_cooldown_timer = 0
            Bullet("e_bullet", self.position, (0, 300), shooter=g.ENEMY_SHOOTER_GROUP)

    def update(self, deltaT):
        self.shoot_cooldown_timer += deltaT
        self.shoot()
        super().update(deltaT)


class Controller:
    enemies = []

    def __init__(self):
        self.cooldown = {
            "normal": 3,
        }
        self.cooldown_timers = {
            "normal": 0,
        }
        self.enemy_types = {
            "normal": Normal,
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

        # Remove enemies that are dead or off screen
        indices_to_forget = [
            i
            for i, e in enumerate(self.enemies)
            if e.is_outside_screen() or not e.alive
        ]
        for i in indices_to_forget:
            self.enemies.pop(i)

        if len(indices_to_forget) >= 1:
            print(f"killed {len(indices_to_forget)} enemies")

        for b in get_bullets_for_shooter(g.PLAYER_SHOOTER_GROUP):
            for e in self.enemies:
                distance = b.distance_from(e)
                if distance <= e.hitbox_size:
                    e.on_hit(e)
                    b.on_hit()
        self.spawn_enemies()

    def draw_all_enemies(self):
        [e.draw() for e in self.enemies]
