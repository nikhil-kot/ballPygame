#Deeksha Reddy (dgr39)
#This program codes a simple game to throw a ball at stack of blocks.
import pygame
from Ball import ball
from Block import rectangle
from Text import Text

pygame.init()
width = 400
height = 400
surface = pygame.display.set_mode((width, height))

#given
dt = 0.1
g = -6.67
R = 0.7
eta = 0.5
ball = ball(20, 300, (0, 0, 0))  
blocks = []

blocks.append(rectangle((260), (260), 20, 20, (102, 0, 0)))
blocks.append(rectangle((280), (260), 20, 20, (153, 0, 0)))
blocks.append(rectangle((240), (260), 20, 20, (204, 0, 0)))
blocks.append(rectangle((260), (240), 20, 20, (0, 0, 102)))
blocks.append(rectangle((280), (240), 20, 20, (0, 0, 153)))
blocks.append(rectangle((240), (240), 20, 20, (0, 0, 204)))
blocks.append(rectangle((240), (280), 20, 20, (0, 102, 0)))
blocks.append(rectangle((260), (280), 20, 20, (0, 153, 0)))
blocks.append(rectangle((280), (280), 20, 20, (0, 204, 0)))


xv = 0
yv = 0
play = False
score = 0

#given
def intersect(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and \
            rect1.x + rect1.width > rect2.x and \
            rect1.y < rect2.y + rect2.height and \
            rect1.height + rect1.y > rect2.y:
        return True
    return False


Score = Text(0, 0)

while(True):
    pygame.draw.rect(surface, (255, 255, 255), (0, 0, 400, 400))
    pygame.draw.line(surface, (0, 0, 0), (0, 300), (500, 300))
    ball.draw(surface)
    surface.blit(Score.draw(score), (0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            first = pygame.mouse.get_pos()
        elif (event.type == pygame.MOUSEBUTTONUP):
            second = pygame.mouse.get_pos()
            xv = second[0]-first[0]
            yv = -(first[1]-second[1])
            play = True
    if play == True:
        if(ball.getY() > 300):
            yv = -R * yv
            xv = eta * xv
            temp = (int((ball.getX()+dt*xv)), int((ball.getY()+dt*yv)))
            ball.setLoc(temp)
        else:
            yv = yv-g*dt
            temp = (int(ball.getX()+(dt*xv)), int(ball.getY()+(dt*yv)))
            ball.setLoc(temp)

    for block in blocks:
        if block.getVisible():
            if (intersect(ball.getRect(), block.getRect())):
                block.setVisible(False)
                score += 1
            block.draw(surface)
    pygame.display.update()
