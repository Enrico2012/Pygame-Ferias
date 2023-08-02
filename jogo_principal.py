import pygame
from pygame.locals import *
import random

pygame.init()

# Criando a janela
largura = 500
altura = 500
tam_tela = (largura, altura)
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption('Car Game')

# Cores
cinza = (100, 100, 100)
verde = (76, 208, 56)
verm = (200, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 232, 0)

# Marcação do caminho
largura_rua = 300
marcador_largura = 10
marcador_altura = 50

# Marcação das vias
rua_esq = 150
rua_meio = 250
rua_direita = 350
lanes = [rua_esq, rua_meio, rua_direita]

# Delimitando espaço da rua
rua = (100, 0, largura_rua, altura)
marc_esq = (95, 0, marcador_largura, altura)
marc_dir = (395, 0, marcador_largura, altura)

# Para animação da estrada
mov_y = 0

# Coordenadas iniciais jogaador
jog_x = 250
jog_y = 400

# Frames
clock = pygame.time.Clock()
fps = 120

# Configs
gameover = False
velocidade = 2
placar = 0

class Vehicle(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Escala da imagem
        escala_img = 45 / image.get_rect().width
        nova_larg = image.get_rect().width * escala_img
        nova_alt = image.get_rect().height * escala_img
        self.image = pygame.transform.scale(image, (nova_larg, nova_alt))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerVehicle(Vehicle):
    
    def __init__(self, x, y):
        image = pygame.image.load('assets/Captura de tela 2023-08-01 083829.png')
        super().__init__(image, x, y)
        
# Grupo de sprites
grupo_jogador = pygame.sprite.Group()
grupo_carros = pygame.sprite.Group()

# Criando jogador
jog = PlayerVehicle(jog_x, jog_y)
grupo_jogador.add(jog)

# Imagem dos carros
imagens = ['assets/car-top-view-vector-11835175.jpg', 'assets/depositphotos_116291144-stock-illustration-racing-car-vector-illustration.jpg']
veiculos = []
for image_filename in imagens:
    image = pygame.image.load(image_filename)
    veiculos.append(image)
    
# Batida
batida = pygame.image.load('assets/crash.png')
batida_rect = batida.get_rect()

# Looping principal
running = True
while running:
    
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        # Movimentação
        if event.type == KEYDOWN:
            
            if event.key == K_LEFT and jog.rect.center[0] > rua_esq:
                jog.rect.x -= 100
            elif event.key == K_RIGHT and jog.rect.center[0] < rua_direita:
                jog.rect.x += 100
                
            # Checar colisão
            for vehicle in grupo_carros:
                if pygame.sprite.collide_rect(jog, vehicle):
                    
                    gameover = True
                    
                    # Posição do carro do jogador e da imagem da batida
                    if event.key == K_LEFT:
                        jog.rect.left = vehicle.rect.right
                        batida_rect.center = [jog.rect.left, (jog.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        jog.rect.right = vehicle.rect.left
                        batida_rect.center = [jog.rect.right, (jog.rect.center[1] + vehicle.rect.center[1]) / 2]
            
            
    # Grama
    tela.fill(verde)
    
    # Rua
    pygame.draw.rect(tela, cinza, rua)
    
    # Marcadores da rua
    pygame.draw.rect(tela, amarelo, marc_esq)
    pygame.draw.rect(tela, amarelo, marc_dir)
    
    # Marcadores das vias
    mov_y += velocidade * 2
    if mov_y >= marcador_altura * 2:
        mov_y = 0
    for y in range(marcador_altura * -2, altura, marcador_altura * 2):
        pygame.draw.rect(tela, branco, (rua_esq + 45, y + mov_y, marcador_largura, marcador_altura))
        pygame.draw.rect(tela, branco, (rua_meio + 45, y + mov_y, marcador_largura, marcador_altura))
        
    # Carro jogador
    grupo_jogador.draw(tela)
    
    # Adicionar veículo
    if len(grupo_carros) < 2:
        
        # Espaçamento entre os carros
        add_vehicle = True
        for vehicle in grupo_carros:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                
        if add_vehicle:
            
            # Via aleatória
            lane = random.choice(lanes)
            
            # Carro aleatorio
            image = random.choice(veiculos)
            vehicle = Vehicle(image, lane, altura / -2)
            grupo_carros.add(vehicle)
    
    # Movimentação dos carros
    for vehicle in grupo_carros:
        vehicle.rect.y += velocidade
        
        # Remover carro se sair da tela
        if vehicle.rect.top >= altura:
            vehicle.kill()
            
            # Pontuação
            placar += 1
            
            # Aumentar vel a cada 5 carros
            if placar > 0 and placar % 5 == 0:
                velocidade += 1
    
    # Desenhar os carros
    grupo_carros.draw(tela)
    
    # Pontuação
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render('placar: ' + str(placar), True, branco)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    tela.blit(text, text_rect)
    
    # Checar se houve colisão
    if pygame.sprite.spritecollide(jog, grupo_carros, True):
        gameover = True
        batida_rect.center = [jog.rect.center[0], jog.rect.top]
            
    # Tela se bateu
    if gameover:
        tela.blit(batida, batida_rect)
        
        pygame.draw.rect(tela, verm, (0, 50, largura, 100))
        
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'Você morreu, placar: {placar}. Play again? (Enter Y or N)', True, branco)
        text_rect = text.get_rect()
        text_rect.center = (largura / 2, 100)
        tela.blit(text, text_rect)
            
    pygame.display.update()

    # Esperar resposta
    while gameover:
        
        clock.tick(fps)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                gameover = False
                running = False
                
            # Jogar denovo?
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # Reiniciar o jogo
                    gameover = False
                    velocidade = 2
                    placar = 0
                    grupo_carros.empty()
                    jog.rect.center = [jog_x, jog_y]
                elif event.key == K_n:
                    # Sair dos loops
                    gameover = False
                    running = False

pygame.quit()