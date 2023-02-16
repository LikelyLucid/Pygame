import pygame
import time
pygame.init()
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

quit_game = False
snake_x = (screen_width-20) / 2
snake_y = (screen_height-20) / 2

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    pygame.draw.rect(screen, red, (, snake_y, 20, 20))
    pygame.display.update()

pygame.quit()
quit()