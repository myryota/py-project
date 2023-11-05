import pygame
from player import game

pygame.init()

screen = pygame.display.set_mode((1000, 640))

clock = pygame.time.Clock()

def IntroFunction(flag_, counter_, picture_flag_):
    if flag_:
        if counter_ == 45:
            picture_flag_ = False

        if counter_ == 0:
            picture_flag_ = True

        if picture_flag_ == False:
            counter_ -= 1
        else:
            counter_ += 1

    return picture_flag_, counter_

def Loading(digit):
    loading_image = pygame.image.load(
            "images/icons/3.jpg").convert_alpha()
    loading_image = pygame.transform.scale(loading_image, (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
    loading_image.set_colorkey((255, 255, 255))
    if digit == 2:
        loading_image = pygame.image.load(
            "images/icons/1.jpg").convert_alpha()
        loading_image = pygame.transform.scale(loading_image, (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
        loading_image.set_colorkey((255, 255, 255))
    elif digit == 3:
        loading_image = pygame.image.load(
            "images/icons/6.jpg").convert_alpha()
        loading_image = pygame.transform.scale(loading_image,
                                               (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
        loading_image.set_colorkey((255, 255, 255))
    elif digit == 4:
        loading_image = pygame.image.load(
            "images/icons/2.jpg").convert_alpha()
        loading_image = pygame.transform.scale(loading_image,
                                               (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
        loading_image.set_colorkey((255, 255, 255))
    elif digit == 5:
        loading_image = pygame.image.load(
            "images/icons/woman.jpg").convert_alpha()
        loading_image = pygame.transform.scale(loading_image,
                                               (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
        loading_image.set_colorkey((255, 255, 255))
    elif digit == 6:
        loading_image = pygame.image.load(
            "images/icons/5.jpg").convert_alpha()
        loading_image = pygame.transform.scale(loading_image,
                                               (loading_image.get_width() // 2.2, loading_image.get_height() // 2.2))
        loading_image.set_colorkey((255, 255, 255))
    return loading_image


def Intro_sec(first, second, back):

    pressing_button = pygame.image.load("images/player_choosing/old-photo-cardboard-with-corner-isolated-white-background-retro-style-paper-photo-frame_154730-1730.jpg-6-PhotoRoom.png-PhotoRoom.png")
    pressing_button = pygame.transform.scale(pressing_button, (pressing_button.get_width() // 6, pressing_button.get_height() // 6))
    pressing_button.set_colorkey((255, 255, 255))
    image1 = Loading(first)
    image2 = Loading(second)

    running = True
    counter = 0
    picture_flag = True  # эти парметры для гифки
    intro_pictures = [
        pygame.transform.scale(pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-0.png'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-1.png'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-2.png'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-3.png'),
                               (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-4.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-5.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-6.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-7.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-8.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-9.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-10.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-11.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-12.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-13.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-14.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-15.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-16.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-17.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-18.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-19.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-20.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-21.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-22.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-23.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-24.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-25.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-26.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-27.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-28.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-29.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-30.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-31.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-32.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-33.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-34.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-35.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-36.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-37.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-38.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-39.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-40.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-41.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-42.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-43.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-44.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-45.png'),
            (1000, 640)),
        pygame.transform.scale(
            pygame.image.load('images/player_choosing/91e0f84ad70b4736b3ed0bba5a8c5b6bdV95dl5uxJr8wEc8-46.png'),
            (1000, 640)),
    ]

    while running:
        pygame.display.update()

        picture_flag, counter = IntroFunction(running, counter, picture_flag)

        screen.blit(intro_pictures[counter % 46], (0, 0))
        screen.blit(pressing_button, (390, 5))
        screen.blit(image1, (5, 150))
        screen.blit(image2, (645, 150))

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game(back, first, second)
                    return





