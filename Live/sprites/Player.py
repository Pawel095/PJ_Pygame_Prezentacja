import pygame
import loader
import events
from sprites.__base import Base
from sprites.bullet import Bullet
import sprites.bullet as bullets
import global_vars as g

class Player(Base):
    def __init__(self):
        self.sprite = loader.assets.get("player")
        self.size = self.sprite.get_rect()[2:]
        self.sprite = pygame.transform.rotozoom(self.sprite,180,0.5)
        self.hitbox = self.size[0]

        self.speed=300
        self.position=(100,100)
        self.velocity=(0,0)
        self.acceleration=(0,0)

        self.shooting_timer = 0
        self.shooting_cooldown=0.5

        self.alive = True
        self.hp=2

    def movement(self):
        vx, vy = self.velocity

        dx,dy = (0,0)
        if events.LEFT:
            dx+=-1
        if events.RIGHT:
            dx+= 1
        if events.UP:
            dy+=-1
        if events.DOWN:
            dy+= 1

        dx*=self.speed
        dy*=self.speed
        self.velocity = (dx,dy)

    def shooting(self):
        if events.SHOOT:
            if self.shooting_timer>=self.shooting_cooldown:
                self.shooting_timer = 0
                Bullet(g.PLAYER_SHOOTER_GROUP,self.position,(0,0),(0,-50))

    def on_hit(self):
        self.hp-=1
        if self.hp <= 0:
            self.alive = False

    def check_for_bullet_hits(self):
        # Bullet hits
        for b in bullets.get_bullets_for_shooter(g.ENEMY_SHOOTER_GROUP):
            dist= b.distance_from(self)
            if dist <= self.hitbox:
                self.on_hit()
                b.on_hit()

    def update(self,deltaT):
        self.shooting_timer+=deltaT
        self.movement()
        self.shooting()
        self.check_for_bullet_hits()
        super().update(deltaT)

    def draw(self):
        if self.alive:
            super().draw()