import pygame
from Drawable import Drawable

class ball(Drawable):
    def __init__(self, x, y, color):
        super().__init__(x,y)
        self.__color = color
def draw(self, surface):
        loc = super().getLoc()
        pygame.draw.circle(surface,self.__color,loc,8)
    def getRect(self):
        num = pygame.Rect(self.getX()-8,self.getY()-8, 16, 16)
        return num
