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

        
    main.tela.fill(main.verde)

    pygame.draw.rect(main.tela, main.cinza, main.rua)

    pygame.draw.rect(main.tela, main.amar, main.borda_esquerda)
    pygame.draw.rect(main.tela, main.amar, main.borda_direita)

    marcador_faixa_y += vel
    if marcador_faixa_y >= main.marcador_altura * 2:
        marcador_faixa_y = 0

    for y in range(main.marcador_altura * -2, main.height, main.marcador_altura*2):
        pygame.draw.rect(main.tela, main.branco, (main.via_esq + 45, y + marcador_faixa_y, main.marcador_largura, main.marcador_altura))
        pygame.draw.rect(main.tela,main.branco, ((main.via_meio + 45, y + marcador_faixa_y, main.marcador_largura, main.marcador_altura)))
        pygame.draw.rect(main.tela,main.branco, ((main.via_dir + 45, y + marcador_faixa_y, main.marcador_largura, main.marcador_altura)))

    pygame.display.update()