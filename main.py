import pygame
from pygame.locals import *
import random

pygame.init()

width = 900
height = 600
tam_tela = (width, height)
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption('Highway Rush!')

cinza = (100, 100, 100)
verde = (76, 208, 56)
verm = (200, 0, 0)
branco = (255, 255, 255)
amar = (255, 232, 0)

marcador_largura = 10
marcador_altura = 50

rua = (100, 0, 300, height)
borda_esquerda = (95, 0, marcador_largura, height)
borda_direita = (395, 0, marcador_largura, height)

faixa_esq = 150
faixa_meio = 250
faixa_dir = 350

faixas = [faixa_esq, faixa_meio, faixa_dir]

marcador_faixa_y = 0
