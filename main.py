# imports
import pygame
import obstacle
from bird import Bird
from obstacle_spawner import ObstacleSpawner


# main game function
def main():
    # init:

    # init pygame
    pygame.init()
    pygame.mixer.init()

    # declare screen size
    size = (500, 700)

    # init screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy Pygame (Bird)")

    # init bg
    BACKGROUND_IMAGE = pygame.image.load("background.jpg")

    # init bird
    player = Bird(screen)
    player.rect.x = 50
    player.rect.y = screen.get_height() * 3 / 7

    # init obstacle spawner
    obstacleSpawner = ObstacleSpawner(screen, pygame.color.Color("#87ab3f"))

    # init sprites list
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)

    # init game exit var
    carry_on = True

    # clock init
    clock = pygame.time.Clock()

    # variable that tells the game to spawn new pipes or not
    spawnPipes = True

    # variable that tells the game whether the player is collided with a pipe or not
    gameOver = False

    # score
    score = 0

    # score debounce (used to see if player has gotten points from current pipes or not)
    scoreDB = False

    # sound init
    die = pygame.mixer.Sound("gameover.wav")
    point = pygame.mixer.Sound("point.wav")
    jump = pygame.mixer.Sound("jump.wav")
    restart = pygame.mixer.Sound("restart.wav")

    # main game loop:
    while carry_on:
        # delta time
        clock.tick(60)

        # events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False

        # init:

        # draw bg
        screen.blit(BACKGROUND_IMAGE, (0, 0))

        # check all sprites in the game
        for s in all_sprites_list:
            # check if the sprite we're looking at is an obstacle
            if type(s) == obstacle.Obstacle:
                # if an obstacle is off of the screen
                if s.rect.x <= obstacleSpawner.respawn_x:
                    # then remove it and spawn new pipes
                    all_sprites_list.remove(s)
                    spawnPipes = True

                # if a pipe is colliding with the player
                if pygame.sprite.collide_mask(s, player) and not gameOver:
                    # let the game know that it's game over and stop the player's movement
                    gameOver = True
                    player.gravity = False
                    player.y_change = 0
                    die.play()
                # check if player needs a point
                elif s.rect.x + s.width <= player.rect.x and not scoreDB:
                    score += 1
                    point.play()
                    scoreDB = True

                # if the game is over
                if gameOver:
                    # stop all pipes from moving
                    s.x_change = 0

        # spawn pipes?
        if spawnPipes:
            # get the top and bottom pipe and store it in a tuple (newObstacles)
            newObstacles = obstacleSpawner.create_obstacle(screen)
            # for each pipe in the newObject tuple
            for o in newObstacles:
                # add it to the sprite list
                all_sprites_list.add(o)
            # the pipes have been spawned, so we don't need to spawn more next frame (and we can reset scoreDB)
            spawnPipes = False
            scoreDB = False

        # check player y
        # check touching top/bottom
        if player.rect.y < 0:
            player.rect.y = 0
            player.y_change = 0
        elif player.rect.y > 575:
            player.rect.y = 575
            player.y_change = 0
            gameOver = True
            player.gravity = False
            die.play()

        # update sprites
        all_sprites_list.update()
        all_sprites_list.draw(screen)

        # update obstacle spawner
        obstacleSpawner.update()

        # gui rendering:

        # render score
        font = pygame.font.SysFont("Showcard Gothic", 128)
        scoreStr = str(score)
        # scoreStr = scoreStr.rstrip(scoreStr[-1])
        # scoreStr = scoreStr.rstrip(scoreStr[-1])
        scoreText = font.render(scoreStr, True, (255, 255, 255))
        scoreTextX = (screen.get_width() / 2) - (scoreText.get_width() / 2)
        scoreTextY = 10
        screen.blit(scoreText, (scoreTextX, scoreTextY))

        # check game over:
        if gameOver:
            # render game over text
            font = pygame.font.SysFont("Showcard Gothic", 80)
            gameOverText = font.render("Game Over", True, (255, 0, 0))
            gameOverTextX = (screen.get_width() / 2) - (gameOverText.get_width() / 2)
            gameOverTextY = (screen.get_height() / 2) - (gameOverText.get_height() / 2)
            screen.blit(gameOverText, (gameOverTextX, gameOverTextY))

            # render the restart text
            font2 = pygame.font.SysFont("Showcard Gothic", 48)
            restartText = font2.render("Press 'R' to restart", True, (255, 0, 0))
            restartTextX = (screen.get_width() / 2) - (restartText.get_width() / 2)
            restartTextY = (screen.get_height() / 2) - (restartText.get_height() / 2) \
                           + 45 #+ (gameOverTextY + gameOverText.get_height())
            screen.blit(restartText, (restartTextX, restartTextY))

        # key input:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and gameOver:
            restart.play()
            main()

        # player jump check
        if player.y_change == -5:
            jump.play()

        # render the finished display image:
        pygame.display.flip()

    # Code that runs when the user exits the game
    pygame.quit()


if __name__ == "__main__":
    main()
