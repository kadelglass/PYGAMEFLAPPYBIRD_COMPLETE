# imports
import pygame


# Bird class, class of the player:
class Bird(pygame.sprite.Sprite):
    # init:
    def __init__(self, screen):
        # call base class init
        super().__init__()

        # set image
        self.image = pygame.image.load("bird1.png")
        # set the rect (the bounding box so to speak, contains x and y values) to the image's bounding rect
        self.rect = self.image.get_rect()

        # init vars
        self.screen = screen
        self.y_change = 0
        self.gravity = True

    # update:
    def update(self):
        # call base class update
        super().update()

        # movement:
        self.rect.y += self.y_change

        # gravity (we only do gravity if the gravity boolean is True, so we can set it to False at game over
        if self.gravity:
            # 1 / 5 is a nice ratio for gravity, snappy and feels good.
            # Bigger number instead of 5 means more floaty movement
            # Smaller number instead of 5 means more snappy movement
            # and only do the gravity change if not resting on the bottom
            if self.rect.y != 0:
                self.y_change += 1 / 5

        # input:
        self.check_input()

    # input handling:
    def check_input(self):
        # get all pressed keys
        keys = pygame.key.get_pressed()
        # if the space bar is being pressed and we are half-way done with a jump (small debounce so that
        # the input feels light and gravitatious instead of floaty or gravity-defying)
        if keys[pygame.K_SPACE] and self.y_change > -2.5:
            self.jump(5)

    # function for handling jumps
    def jump(self, amount):
        # if gravity boolean is True, jump (prevents jumping during game over)
        if self.gravity:
            self.y_change = -amount
