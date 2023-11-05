import pygame
from background_choosing import Background_Choosing
from intro import Intro
from music import Click

pygame.init()
screen = pygame.display.set_mode((1000, 640))

class Menu():
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


def Menu_Function():
    start_image = pygame.image.load(
        "images/menu/menu.png").convert_alpha()
    quit_image = pygame.image.load(
        "images/menu/quit.png").convert_alpha()


    menu = pygame.image.load("images/menu/knight1.jpg").convert_alpha()
    menu = pygame.transform.scale(menu, (menu.get_width() * 1, menu.get_height() * 1.15))

    quit_image = pygame.transform.scale(quit_image, (quit_image.get_width() // 3, quit_image.get_height() // 3))
    quit_image.set_colorkey((255, 255, 255))

    start_image = pygame.transform.scale(start_image, (start_image.get_width() // 3, start_image.get_height() // 3))
    start_image.set_colorkey((255, 255, 255))


    start_button = Menu(25, 25, start_image)
    quit_button = Menu(300, 300, quit_image)

    run = True

    while run:
        pygame.display.update()
        screen.blit(menu, (0, 0))

        if start_button.draw():
            Click()
            Intro()
            Background_Choosing()
        elif quit_button.draw():
            Click()
            quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
