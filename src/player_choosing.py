import pygame
from intro import Intro
from music import Click
from intro_sec import Intro_sec

pygame.init()

screen = pygame.display.set_mode((1000, 640))

class Player():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# game loop
def Player_Choosing(back_ground_number):

    first_fighter_choosing = -1
    second_fighter_choosing = -1

    player_first_image = pygame.image.load(
        "images/icons/3.jpg").convert_alpha()
    player_second_image = pygame.image.load(
        "images/icons/1.jpg").convert_alpha()
    player_third_image = pygame.image.load(
        "images/icons/6.jpg").convert_alpha()
    player_fourth_image = pygame.image.load(
        "images/icons/2.jpg").convert_alpha()
    player_fifth_image = pygame.image.load(
        "images/icons/woman.jpg").convert_alpha()
    player_sixth_image = pygame.image.load(
        "images/icons/5.jpg").convert_alpha()

    back_ground = pygame.image.load("images/back/bg1.png").convert_alpha()
    back_ground = pygame.transform.scale(back_ground, (back_ground.get_width() // 6, back_ground.get_height() // 7))

    menu = pygame.image.load("images/menu/knight1.jpg").convert_alpha()
    menu = pygame.transform.scale(menu, (menu.get_width() * 1, menu.get_height() * 1.15))

    location_first = pygame.transform.scale(player_first_image,
                                            (player_first_image.get_width() // 7, player_first_image.get_height() // 7))
    location_first.set_colorkey((255, 255, 255))

    location_second = pygame.transform.scale(player_second_image, (player_second_image.get_width() // 7, player_second_image.get_height() // 7))
    location_second.set_colorkey((255, 255, 255))

    location_third = pygame.transform.scale(player_third_image, (
    player_third_image.get_width() // 7, player_third_image.get_height() // 7))
    location_second.set_colorkey((255, 255, 255))

    location_fourth = pygame.transform.scale(player_fourth_image, (
    player_fourth_image.get_width() // 7, player_fourth_image.get_height() // 7))
    location_fourth.set_colorkey((255, 255, 255))

    location_fifth = pygame.transform.scale(player_fifth_image,
                                            (player_fifth_image.get_width() // 7, player_fifth_image.get_height() // 7))
    location_fifth.set_colorkey((255, 255, 255))

    location_sixth = pygame.transform.scale(player_sixth_image, (
    player_sixth_image.get_width() // 7, player_sixth_image.get_height() // 7))
    location_sixth.set_colorkey((255, 255, 255))

    fighter1_choosing = pygame.image.load("images/icons/first.png").convert_alpha()
    fighter1_choosing = pygame.transform.scale(fighter1_choosing,
                                              (fighter1_choosing.get_width() // 7, fighter1_choosing.get_height() // 7))
    fighter2_choosing = pygame.image.load("images/icons/second.png").convert_alpha()
    fighter2_choosing = pygame.transform.scale(fighter2_choosing,
                                               (fighter2_choosing.get_width() // 7, fighter2_choosing.get_height() // 7))
    first_button = Player(65, 90, location_first)
    second_button = Player(290, 90, location_second)
    third_button = Player(515, 90, location_third)
    fourth_button = Player(65, 440, location_fourth)
    fifth_button = Player(290, 440, location_fifth)
    sixth_button = Player(515, 440, location_sixth)

    run = True

    while run:
        pygame.display.update()

        screen.blit(menu, (0, 0))

        if first_fighter_choosing == -1:
            screen.blit(fighter1_choosing, (250, 250))
        else:
            screen.blit(fighter2_choosing, (250, 250))

        screen.blit(back_ground, (40, 50))
        screen.blit(back_ground, (265, 50))
        screen.blit(back_ground, (490, 50))
        screen.blit(back_ground, (40, 400))
        screen.blit(back_ground, (265, 400))
        screen.blit(back_ground, (490, 400))

        if first_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 1
                Intro()
                continue
            second_fighter_choosing = 1
        elif second_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 2
                Intro()
                continue
            second_fighter_choosing = 2
        elif third_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 3
                Intro()
                continue
            second_fighter_choosing = 3
        elif fourth_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 4
                Intro()
                continue
            second_fighter_choosing = 4
        elif fifth_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 5
                Intro()
                continue
            second_fighter_choosing = 5
        elif sixth_button.draw():
            Click()
            if first_fighter_choosing == -1:
                first_fighter_choosing = 6
                Intro()
                continue
            second_fighter_choosing = 6

        if first_fighter_choosing != -1 and second_fighter_choosing != -1:
            Intro_sec(first_fighter_choosing, second_fighter_choosing, back_ground_number)
            return


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
