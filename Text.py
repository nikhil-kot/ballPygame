import pygame
from Drawable import Drawable

pygame.font.init()
class Text(Drawable):
    def __init__(self,x,y):
        super().__init__(x,y)
    def draw(self, score):
        font = pygame.font.Font("freesansbold.ttf", 14)
        return font.render('Score: ' + str(score), True, (0,0,0))
    
    def getRect(self):
        pass