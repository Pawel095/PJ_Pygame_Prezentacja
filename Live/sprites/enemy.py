import pygame
import loader
from sprites.__base import Base
import sprites.bullet as bullets
import global_vars as g
from sprites.bullet import Bullet

class Enemy(Base):
    def __init__(self):
        self.sprite = loader.assets.get("enemy")
        self.size = self.sprite.get_rect()[2:]
        self.hitbox = self.size[0]

        self.speed=300
        self.position=(400,100)
        self.velocity=(0,50)
        self.acceleration=(0,0)
        
        self.shooting_timer = 0
        self.shooting_cooldown=2

        self.alive = True

    def on_hit(self):
        self.alive=False

    def think(self,deltaT):
        if self.shooting_timer>=self.shooting_cooldown:
            self.shooting_timer = 0
            Bullet(g.ENEMY_SHOOTER_GROUP,self.position,(0,100),(0,0))

    def update(self,deltaT):
        self.shooting_timer+=deltaT
        self.think(deltaT)
        super().update(deltaT)


class Controller:
    enemies = []
    def __init__(self):
        self.cooldown = {
            "normal":3
        }
        self.cooldown_timer = {
            "normal":3
        }
        self.enemy_types= {
            "normal":Enemy
        }
    
    def spawn_enemies(self):
        for k,i in self.cooldown.items():
            if self.cooldown_timer[k]>=self.cooldown[k]:
                self.cooldown_timer[k]=0
                e=self.enemy_types[k]()
                self.enemies.append(e)

    def update(self, deltaT):
        for e in self.enemies:
            e.update(deltaT)

        for k,i in self.cooldown_timer.items():
            self.cooldown_timer[k] += deltaT

        # Remove enemies that are dead or off screen
        indices_to_forget = [
            i
            for i, e in enumerate(self.enemies)
            if e.is_outside_screen() or not e.alive
        ]
        indices_to_forget.reverse()
        for i in indices_to_forget:
            self.enemies.pop(i)

        # Bullet hits
        for b in bullets.get_bullets_for_shooter(g.PLAYER_SHOOTER_GROUP):
            for e in self.enemies:
                dist= b.distance_from(e)
                if dist <= e.hitbox:
                    e.on_hit()
                    b.on_hit()


        self.spawn_enemies()

    def draw(self):
        [e.draw() for e in self.enemies]