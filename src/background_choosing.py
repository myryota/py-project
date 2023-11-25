import pygame
from player_choosing import Player_Choosing
from intro import Intro
from music import Click

pygame.init()

screen = pygame.display.set_mode((1000, 640))

class Back():
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
def Background_Choosing():
    location_first_image = pygame.image.load(
        "images/back/game_background_1.png").convert_alpha()
    location_second_image = pygame.image.load(
        "images/back/game_background_2.png").convert_alpha()
    location_third_image = pygame.image.load(
        "images/back/game_background_3.png").convert_alpha()
    location_fourth_image = pygame.image.load(
        "images/back/game_background_4.png").convert_alpha()

    icon_choosing = pygame.image.load("images/back/choose_icon.png").convert_alpha()
    icon_choosing = pygame.transform.scale(icon_choosing, (icon_choosing.get_width() // 6, icon_choosing.get_height() // 6))

    back_ground = pygame.image.load("images/back/bg.png").convert_alpha()
    back_ground = pygame.transform.scale(back_ground, (back_ground.get_width() // 4, back_ground.get_height() // 4))

    menu = pygame.image.load("images/menu/knight1.jpg").convert_alpha()
    menu = pygame.transform.scale(menu, (menu.get_width() * 1, menu.get_height() * 1.15))

    location_fourth = pygame.transform.scale(location_fourth_image, (location_fourth_image.get_width() // 15, location_fourth_image.get_height() // 15))
    location_fourth.set_colorkey((255, 255, 255))

    location_first = pygame.transform.scale(location_first_image, (location_first_image.get_width() // 15, location_first_image.get_height() // 15))
    location_first.set_colorkey((255, 255, 255))

    location_second = pygame.transform.scale(location_second_image, (location_second_image.get_width() // 15, location_second_image.get_height() // 15))
    location_second.set_colorkey((255, 255, 255))

    location_third = pygame.transform.scale(location_third_image, (location_third_image.get_width() // 15, location_third_image.get_height() // 15))
    location_third.set_colorkey((255, 255, 255))

    first_button = Back(60, 75, location_first)
    second_button = Back(400, 75, location_second)
    third_button = Back(60, 430, location_third)
    fourth_button = Back(400, 430, location_fourth)


    run = True

    while run:
        pygame.display.update()


        screen.blit(menu, (0, 0))
        screen.blit(icon_choosing, (250, 240))
        screen.blit(back_ground, (25, 25))
        screen.blit(back_ground, (365, 25))
        screen.blit(back_ground, (25, 380))
        screen.blit(back_ground, (365, 380))

        if first_button.draw():
            Click()
            Intro()
            Player_Choosing(1)
        if second_button.draw():
            Click()
            Intro()
            Player_Choosing(2)
        if third_button.draw():
            Click()
            Intro()
            Player_Choosing(3)
        if fourth_button.draw():
            Click()
            Intro()
            Player_Choosing(4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
