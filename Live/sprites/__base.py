import pygame
import global_vars as g

class Base:
    def __init__(self):
        self.speed=300
        self.position=(100,100)
        self.velocity=(0,0)
        self.acceleration=(0,0)

        self.alive = True

    def __linear_update(self,deltaT):
        px,py = self.position
        vx,vy = self.velocity
        ax,ay = self.acceleration

        self.velocity=(ax*deltaT + vx,ay*deltaT+vy)
        self.position=(px+ vx*deltaT +ax*deltaT**2,py+ vy*deltaT +ay*deltaT**2)

    def is_outside_screen(self):
        return (
            self.position[0] + self.size[0] <= 0
            or self.position[1] + self.size[1] <= 0
            or self.position[0] >= g.SCREEN_SIZE[0]
            or self.position[1] >= g.SCREEN_SIZE[1]
        )

    def update(self,deltaT):
        self.__linear_update(deltaT)

    def draw(self):
        center = (self.position[0] - self.size[0]/2,self.position[1] - self.size[1]/2)
        srf = pygame.display.get_surface()
        srf.blit(self.sprite,center)