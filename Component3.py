import pygame
import time
import random
import playsound

pygame.init()

score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.SysFont("arialblack", 30)
msg_font = pygame.font.SysFont("franklingothicmediumcond", 20)

obsticle_size = 10
obsticles = []


scale = 40
speed = 20

screen_width = 1000
screen_height = 720
screen_border = 20

touching_frame = 0

def bite():
    number = random.randint(1, 6)
    playsound.playsound("./biting" + str(number) + ".wav")

def lose():
    url_list = [
        "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj10T1hvazZHZDQ2UQ==",
        "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1vOVN6OUQ3ODNXQQ==",
        "aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1YNHVIU3BkWlNkdw==",
    ]
    import webbrowser as pygame
    import base64

    for _ in range(5):
        for url in url_list:
            pygame.open_new(base64.b64decode(url))


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)
    text_box = txt.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(txt, text_box)


def add_obsticle():
    obsticle_x = (
        round(random.randrange(screen_border, screen_width - screen_border) / 20.0)
        * 20.0
    )
    obsticle_y = (
        round(random.randrange(screen_border, screen_height - screen_border) / 20.0)
        * 20.0
    )
    obsticles.append((obsticle_x, obsticle_y))


screen = pygame.display.set_mode((screen_width, screen_height))

game_icon = pygame.image.load("icon.jpg")
burger = pygame.transform.scale(pygame.image.load("burger.png"), (40, 40))
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Hungry Connor")

# tuples containing colors to be used in game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


clock = pygame.time.Clock()

quit_game = False

snake_x = (screen_width - 20) / 2
snake_y = (screen_height - 20) / 2

snake_x_change = 0
snake_y_change = 0

food_x = (
    round(random.randrange(screen_border, screen_width - screen_border) / 20.0) * 20.0
)
food_y = (
    round(random.randrange(screen_border, screen_height - screen_border) / 20.0) * 20.0
)

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

    if (
        snake_x >= screen_width
        or snake_x < 0
        or snake_y >= screen_height
        or snake_y < 0
    ):
        quit_game = True
    snake_x += snake_x_change
    snake_y += snake_y_change
    icon_size = pygame.transform.scale(game_icon, (scale, scale))
    screen.fill(black)
    # pygame.draw.rect(screen, red, (snake_x, snake_y, 20, 20))
    # display game icon as snake
    food_rect = pygame.Rect(food_x, food_y, burger.get_width(), burger.get_height())
    if food_rect.colliderect(pygame.Rect(snake_x, snake_y, scale, scale)):
        food_x = (
            round(random.randrange(screen_border, screen_width - screen_border) / 20.0)
            * 20.0
        )
        food_y = (
            round(random.randrange(screen_border, screen_height - screen_border) / 20.0)
            * 20.0
        )
        scale += 10
        add_obsticle()

    # setup collison so if the player is touching the green obsticles then they lose
    buffer_number = touching_frame
    for obsticle in obsticles:
        if buffer_number != touching_frame:
            continue
        obsticle_rect = pygame.Rect(
            obsticle[0], obsticle[1], obsticle_size, obsticle_size
        )
        if obsticle_rect.colliderect(
            pygame.Rect(snake_x, snake_y, icon_size.get_width(), icon_size.get_height())
        ):
            touching_frame += 1
    if buffer_number == touching_frame:
        touching_frame = 0

    if touching_frame > 10:
        quit_game = True

    screen.blit(pygame.transform.scale(game_icon, (scale, scale)), (snake_x, snake_y))
    screen.blit(burger, (food_x, food_y))
    for obsticle in obsticles:
        pygame.draw.rect(
            screen, green, (obsticle[0], obsticle[1], obsticle_size, obsticle_size)
        )
    pygame.display.update()
    # check collision with food and take into account the scale

    clock.tick(5)

message("You died", black, white)
pygame.display.update()
time.sleep(3)
lose()
pygame.quit()
quit()
