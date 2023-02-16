import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 720))

game_icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake")

# tuples containing colors to be used in game
# Black, white, red, green
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True


pygame.quit()
quit()

pygame.quit()
quit()