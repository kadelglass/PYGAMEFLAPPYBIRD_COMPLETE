# imports
import pygame
from random import randint


# unused function that contains calculations for spawning obstacles
def create_obstacle_values(screen):
    # init obstacles
    oTopHeight = randint(50, 400)
    topWidth = 70
    topHeight = oTopHeight
    topYVal = 0
    bottomWidth = 70
    bottomHeight = screen.get_height() - oTopHeight - 200 - 65
    bottomYVal = oTopHeight + 200
    return topWidth, topHeight, topYVal, bottomWidth, bottomHeight, bottomYVal


class Obstacle(pygame.sprite.Sprite):
    # init:
    def __init__(self, width, height, color, x_change, yVal, topObstacle):
        # init:

        # call base class init
        super().__init__()

        # variable init
        self.width = width
        self.height = height
        self.color = color
        self.x_change = x_change
        self.topObstacle = topObstacle

        # draw init:

        # create the Surface (empty image container)
        self.image = pygame.Surface((self.width, self.height))
        # fill the background of it with black
        self.image.fill((0, 0, 0))
        # set the color key of it to black
        self.image.set_colorkey((0, 0, 0))
        # set the rect (contains x and y and other important values) to the image's bounding rect
        self.rect = self.image.get_rect()

        # draw
        if not self.topObstacle:
            # main body of the pipe
            pygame.draw.rect(self.image, color, (5, 25, self.width - 10, self.height - 25))
            # top part of the pipe
            pygame.draw.rect(self.image, color, (0, 0, self.width, 25))
        else:
            # main part of the pipe
            pygame.draw.rect(self.image, color, (5, 0, self.width - 10, self.height - 25))
            # top part of the pipe
            pygame.draw.rect(self.image, color, (0, self.height - 25, self.width, 25))

        # rect init
        self.rect.x = 500
        self.rect.y = yVal

    def update(self):
        # call base class update
        super().update()

        # movement:
        self.rect.x += self.x_change
