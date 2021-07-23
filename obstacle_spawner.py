# imports
from random import randint
from obstacle import Obstacle


# unused function that just has all of the calculations for obstacle values in it
def create_obstacle_values(screen):
    # init obstacles:

    # the top obstacle's height, random value from 50-400
    oTopHeight = randint(50, 400)
    # top obstacle's width, always going to be 70
    topWidth = 70
    # set the height (this could be avoided, but it was here so it was more convenient
    # to set the value than change a variable's name)
    topHeight = oTopHeight
    # the top left corner of the top obstacle
    topYVal = 0

    # the bottom obstacle's width, always going to be 70
    bottomWidth = 70
    # the bottom obstacle's height, formula goes:
    # ((Screen's Height) - (Top Obstacle's Height) - (Gap) - (Floor Height))
    bottomHeight = screen.get_height() - oTopHeight - 200 - 65
    # bottom obstacle's top left corner, equal to the top obstacle's height + the gap
    bottomYVal = oTopHeight + 200

    # return all of the values, unused but nice for more advanced/cleaner implementation later
    return topWidth, topHeight, topYVal, bottomWidth, bottomHeight, bottomYVal


# ObstacleSpawner class, handles all obstacle spawning so the main game doesn't need to (organization, yay)
class ObstacleSpawner:

    # this class only needs the screen (for calculations) and a color (for obstacle color)
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.starter_speed = -4
        self.gap = 250
        self.respawn_x = -500

    # function for creating obstacles
    def create_obstacle(self, screen):
        # init obstacles
        oTopHeight = randint(75, 375)
        oColor = self.color

        # create obstacles
        oTop = Obstacle(70, oTopHeight, oColor, self.starter_speed, 0, True)
        bObstacleHeightCalc = screen.get_height() - oTopHeight - self.gap - 63
        oBottom = Obstacle(70, bObstacleHeightCalc, oColor, self.starter_speed, oTopHeight + self.gap, False)

        # return obstacles
        return oTop, oBottom

    def update(self):
        if self.gap > 100:
            self.gap -= 1 / 6000
        if self.respawn_x < -80:
            self.respawn_x += 1 / 6000
        if self.starter_speed > -10:
            self.starter_speed -= 1 / 6000
