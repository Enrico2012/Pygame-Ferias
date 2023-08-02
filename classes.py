import pygame
from pygame.locals import *
import random

from pygame.sprite import AbstractGroup
import main

class Veiculo(pygame.sprite.Sprite):

    def __init__(self, imagem, x, y):
        pygame.sprite.Sprite.__init__(self)

        escala_imagem = 45 / imagem.get_rect().width
        nova_largura = imagem.get_rect().width * escala_imagem
        nova_altura = imagem.get_rect().height * escala_imagem
        self.imagem = pygame.transform.scale(imagem, (nova_largura, nova_altura))


        self.rect = self.imagem.get_rect()
        self.rect.center = [x, y]

class veiculo_jogador(Veiculo):

    def __init__(self, x, y):
        imagem = pygame.image.load('assets/Captura de tela 2023-08-01 083829.png')
        super().__init__(imagem, x, y)
        