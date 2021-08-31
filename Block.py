import pygame
from Drawable import Drawable

class rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color
    def draw(self, surface):
        loc = super().getLoc()
        pygame.draw.rect(surface,self.__color,(loc[0],loc[1],self.__width,self.__height))
        
    def getRect(self):
        num = pygame.Rect(self.getX(),self.getY(), self.__width, self.__height)
        return num

    