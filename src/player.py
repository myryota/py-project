import pygame
from pygame import *

from fighter import Fighter
from intro import Intro

mixer.init()
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGTH = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
COLOR1 = (255, 25, 152)
COLOR2 = (34, 155, 152)

def game(back, player1, player2):
    clock = pygame.time.Clock()
    fps = 60

    # define game variables
    intro_count = 3
    last_count_update = pygame.time.get_ticks()
    # load background image
    if back == 1:
        bg_image = pygame.image.load("images/back/game_background_1.png").convert_alpha()
    elif back == 2:
        bg_image = pygame.image.load("images/back/game_background_2.png").convert_alpha()
    elif back == 3:
        bg_image = pygame.image.load("images/back/game_background_3.png").convert_alpha()
    elif back == 4:
        bg_image = pygame.image.load("images/back/game_background_4.png").convert_alpha()

    if player1 == 1:
        # define fighter variables
        FIGHTER1_SIZE = 116
        FIGHTER1_SCALE = 3
        FIGHTER1_OFFSET = [45, 35]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter1/sprites/fighter1.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        # define number of steps in each animation
        FIGHTER1_ANIMATION_STEPS = [10, 8, 3, 7, 6, 3, 11]  #1 индеец
    elif player1 == 2:
        FIGHTER1_SCALE = 3
        FIGHTER1_SIZE = 150
        FIGHTER1_OFFSET = [60, 55]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter2/sprites/fighter2.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        FIGHTER1_ANIMATION_STEPS = [8, 8, 2, 5, 5, 3, 8]  #2 амазонка
    elif player1 == 3:
        FIGHTER1_SCALE = 3
        FIGHTER1_SIZE = 160
        FIGHTER1_OFFSET = [60, 55]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter3/sprites/fighter3.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        FIGHTER1_ANIMATION_STEPS = [8, 8, 2, 6, 6, 4, 6]  #3 самурай
    elif player1 == 4:
        FIGHTER1_SCALE = 3.5
        FIGHTER1_SIZE = 128
        FIGHTER1_OFFSET = [60, 45]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter4/sprites/fighter4.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        FIGHTER1_ANIMATION_STEPS = [10, 6, 2, 4, 5, 3, 8]  #4 рыцарь
    elif player1 == 5:
        FIGHTER1_SCALE = 3
        FIGHTER1_SIZE = 116
        FIGHTER1_OFFSET = [60, 35]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter5/sprites/fighter5.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        FIGHTER1_ANIMATION_STEPS = [11, 8, 3, 7, 7, 4, 11]  #5 рыцарь2
    elif player1 == 6:
        FIGHTER1_SCALE = 3.5
        FIGHTER1_SIZE = 160
        FIGHTER1_OFFSET = [60, 70]
        FIGHTER1_DATA = [FIGHTER1_SIZE, FIGHTER1_SCALE, FIGHTER1_OFFSET]
        fighter1_sheet = pygame.image.load("assets/images/fighter6/sprites/fighter6.png").convert_alpha()
        fighter1_sheet.set_colorkey((255, 255, 255))
        FIGHTER1_ANIMATION_STEPS = [8, 8, 2, 8, 8, 3, 7]  #6 маг

    if player2 == 1:
        # define fighter variables
        FIGHTER2_SIZE = 116
        FIGHTER2_SCALE = 3
        FIGHTER2_OFFSET = [45, 35]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter1/sprites/fighter1.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [10, 8, 3, 7, 6, 3, 11]  #1 индеец
    elif player2 == 2:
        FIGHTER2_SCALE = 3
        FIGHTER2_SIZE = 150
        FIGHTER2_OFFSET = [60, 55]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter2/sprites/fighter2.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [8, 8, 2, 5, 5, 3, 8]  #2 амазонка
    elif player2 == 3:
        FIGHTER2_SCALE = 3
        FIGHTER2_SIZE = 160
        FIGHTER2_OFFSET = [60, 55]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter3/sprites/fighter3.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [8, 8, 2, 6, 6, 4, 6]  #3 самурай
    elif player2 == 4:
        FIGHTER2_SCALE = 3.5
        FIGHTER2_SIZE = 128
        FIGHTER2_OFFSET = [60, 45]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter4/sprites/fighter4.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [10, 6, 2, 4, 5, 3, 8]  #4 рыцарь
    elif player2 == 5:
        FIGHTER2_SCALE = 3
        FIGHTER2_SIZE = 160
        FIGHTER2_OFFSET = [60, 55]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter5/sprites/fighter5.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [11, 8, 3, 7, 7, 4, 11]  #5 рыцарь2
    elif player2 == 6:
        FIGHTER2_SCALE = 3.5
        FIGHTER2_SIZE = 160
        FIGHTER2_OFFSET = [60, 70]
        FIGHTER2_DATA = [FIGHTER2_SIZE, FIGHTER2_SCALE, FIGHTER2_OFFSET]
        fighter2_sheet = pygame.image.load("assets/images/fighter6/sprites/fighter6.png").convert_alpha()
        fighter2_sheet.set_colorkey((255, 255, 255))
        FIGHTER2_ANIMATION_STEPS = [8, 8, 2, 8, 8, 3, 7]  #6 маг

    fighter_1 = Fighter(1, 200, 350, False, FIGHTER1_DATA, fighter1_sheet, FIGHTER1_ANIMATION_STEPS)
    fighter_2 = Fighter(2, 700, 350, True, FIGHTER2_DATA, fighter2_sheet, FIGHTER2_ANIMATION_STEPS)
    run = True
    timer_help = 0
    while run:
        clock.tick(fps)

        # draw background
        scaled_bg = transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGTH))
        screen.blit(scaled_bg, (0, 0))

        # show player health
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

        if not fighter_1.alive or not fighter_2.alive:
            timer_help += 1

        if timer_help == 15:
            Intro()
            return

        if intro_count <= 0:
            # move fighters
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGTH, screen, fighter_2)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGTH, screen, fighter_1)
        else:
            # update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()
                print(intro_count)

        # update fighters
        fighter_1.update()
        fighter_2.update()

        # draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # update display
        pygame.display.update()
        screen.fill((0, 0, 0))

        # pygame.display.flip()
    # exit pygame
    pygame.quit()



#function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, COLOR2, (x, y, 400, 30))
    pygame.draw.rect(screen, COLOR1, (x, y, 400 * ratio, 30))
