import pygame
import time
pygame.init()
speed = 20
screen_width = 1000
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

game_icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake")

# tuples containing colors to be used in game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# score_font = pygame.font.Font('arialblack', 20)
# exit_font = pygame.font.Font('arialblack', 30)
clock = pygame.time.Clock()

quit_game = False

snake_x = (screen_width-20) / 2
snake_y = (screen_height-20) / 2

snake_x_change = 0
snake_y_change = 0

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x_change = speed
                snake_y_change = 0
            if event.key == pygame.K_LEFT:
                snake_x_change = -speed
                snake_y_change = 0
            if event.key == pygame.K_UP:
                snake_y_change = -speed
                snake_x_change = 0
            if event.key == pygame.K_DOWN:
                snake_y_change = speed
                snake_x_change = 0
    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(black)
    # pygame.draw.rect(screen, red, (snake_x, snake_y, 20, 20))
    # display game icon as snake
    screen.blit(pygame.transform.scale(game_icon, ()), (snake_x, snake_y))
    pygame.display.update()

    clock.tick(5)

pygame.quit()
quit()