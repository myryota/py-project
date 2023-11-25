import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 640))

clock = pygame.time.Clock()

def IntroFunction(flag_, counter_, picture_flag_):
    if flag_:
        if counter_ == 40:
            picture_flag_ = False

        if counter_ == 0:
            picture_flag_ = True

        if picture_flag_ == False:
            counter_ -= 1
        else:
            counter_ += 1

    return picture_flag_, counter_

def Intro():
    loading_image = pygame.image.load(
        "images/intro/load.png").convert_alpha()
    loading_image = pygame.transform.scale(loading_image, (loading_image.get_width() // 5, loading_image.get_height() // 5))
    loading_image.set_colorkey((255, 255, 255))

    running = True
    counter = 0
    picture_flag = True  #эти парметры для гифки
    intro_pictures = [
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z6.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z62.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z63.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z64.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z65.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z66.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z67.jpg'),
                               (1000, 640)),
        pygame.transform.scale(pygame.image.load('images/intro/cylon_knight_by_oliverink_ddfc1z68.jpg'),
                               (1000, 640)),
    ]
 
    while running:
        pygame.display.update()

        picture_flag, counter = IntroFunction(running, counter, picture_flag)

        screen.blit(intro_pictures[counter % 8], (0, 0))
        screen.blit(loading_image, (175, 35))

        if counter == 15:
            return

        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
