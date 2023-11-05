import pygame
from music import Music
from intro import Intro
from menu import Menu_Function

pygame.init()
screen = pygame.display.set_mode((1000, 640))

Music()
Intro()
Menu_Function()

