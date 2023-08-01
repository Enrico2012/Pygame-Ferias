import pygame
from pygame.locals import *
import random
import main

acabou = False
vel = 2
pontuacao = 0

clock = pygame.time.Clock()
fps = 120
correndo = True
while correndo:

    clock.tick(fps)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            correndo = False

        
    tela.fill(verde)

    pygame.draw.rect(tela, cinza, rua)

    pygame.draw.rect(tela, amar, borda_esquerda)
    pygame.draw.rect(tela, amar, borda_direita)

    marcador_faixa_y += vel
    if marcador_faixa_y >= marcador_altura * 2:
        marcador_faixa_y = 0

    for y in range(marcador_altura * -2, height, marcador_altura*2):
        pygame.draw.rect(tela, branco, (via_esq + 45, y + marcador_faixa_y, marcador_largura, marcador_altura))
        pygame.draw.rect(tela,branco, ((via_meio + 45, y + marcador_faixa_y, marcador_largura, marcador_altura)))
        pygame.draw.rect(tela,branco, ((via_dir + 45, y + marcador_faixa_y, marcador_largura, marcador_altura)))

    pygame.display.update()