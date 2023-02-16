import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 720))
game_icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake")
time.sleep(5)

pygame.quit()
quit()