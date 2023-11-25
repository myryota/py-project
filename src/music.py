import random
import pygame

def Music():
    num = random.randint(1, 4)
    if num == 1:
        pygame.mixer.music.load('music/c418d65efad1826.mp3')
        pygame.mixer.music.play()
    elif num == 2:
        pygame.mixer.music.load('music/18e868cd5af33df.mp3')
        pygame.mixer.music.play()
    elif num == 3:
        pygame.mixer.music.load('music/c418d65efad1826.mp3')
        pygame.mixer.music.play()
    elif num == 4:
        pygame.mixer.music.load('music/edd75e572a44a07.mp3')
        pygame.mixer.music.play()

def Click():
    click = pygame.mixer.Sound("music/20af166b0a13e92.ogg")
    click.play()