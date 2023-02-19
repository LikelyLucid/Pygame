import pygame
import time
import random
pygame.init()

score_font = pygame.font.SysFont('arialblack', 20)
exit_font = pygame.font.SysFont('arialblack', 30)
msg_font = pygame.font.SysFont('franklingothicmediumcond', 20)

def lose():
    url_list = ["aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj10T1hvazZHZDQ2UQ==", "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1vOVN6OUQ3ODNXQQ==", "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1YNHVIU3BkWlNkdw=="]
    import webbrowser as pygame
    import base64
    for _ in range(5):
        for url in url_list:
            pygame.open_new(base64.b64decode(url))

def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(txt, text_box)
scale = 40
speed = 20
screen_width = 1000
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

game_icon = pygame.image.load("icon.jpg")
burger = pygame.transform.scale(pygame.image.load("burger.png"), (40, 40))
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake")

# tuples containing colors to be used in game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


clock = pygame.time.Clock()

quit_game = False

snake_x = (screen_width-20) / 2
snake_y = (screen_height-20) / 2

snake_x_change = 0
snake_y_change = 0

food_x = round(random.randrange(20, screen_width-20) / 20.0) * 20.0
food_y = round(random.randrange(20, screen_height-20) / 20.0) * 20.0

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

    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        quit_game = True
    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(black)
    # pygame.draw.rect(screen, red, (snake_x, snake_y, 20, 20))
    # display game icon as snake
    screen.blit(pygame.transform.scale(game_icon, (scale, scale)), (snake_x, snake_y))
    screen.blit(burger, (food_x, food_y))
    pygame.display.update()
    #check collision with food and take into account the scale
    if snake_x < food_x < snake_x + scale and snake_y < food_y < snake_y + scale:
        food_x = round(random.randrange(20, screen_width-20) / 20.0) * 20.0
        food_y = round(random.randrange(20, screen_height-20) / 20.0) * 20.0
        score += 1
    clock.tick(5)

message("You died", black, white)
pygame.display.update()
time.sleep(3)
# lose()
pygame.quit()
quit()