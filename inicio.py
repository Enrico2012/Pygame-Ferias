import random 
import pygame
from pygame.locals import *



timer = pygame.time.Clock()

fps = 120

correr = True

while correr:
    timer.tick(fps)

    for evento in pygame.event.get():
        if evento.type == QUIT:

            correr == False

    pygame.display.update()
pygame.quit()