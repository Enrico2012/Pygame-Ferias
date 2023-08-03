import pygame
from pygame.locals import *
import random
from pygame import mixer
pygame.mixer.init()
pygame.mixer.music.load('latina-noche-dance-latin-house-background-mexican-reggaeton-music-160302.mp3')
pygame.mixer.music.set_volume(10)
pygame.mixer.music.play(-1)

pygame.init()

# Criando a janela
largura = 900
altura = 600
tam_tela = (largura, altura)
tela = pygame.display.set_mode(tam_tela)
pygame.display.set_caption('Highway Rush!')

# Cores
cinza = (100, 100, 100)
verde = (76, 208, 56)
verm = (200, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 232, 0)
preto = (0, 0,0)

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
velocidade = 1
placar = 0

# Importa imagens
BackMenu = pygame.image.load('assets\Menu.png').convert_alpha()
BackMenu = pygame.transform.scale(BackMenu, (900, 600))
rulesmenu = pygame.image.load('assets\Regras.png').convert_alpha()
rule_smenu = pygame.transform.scale(rulesmenu, (900, 600))


def tela_de_inicio():
    # Loop para exibir a tela de início
    inicio = True
    botao_jogar = None
    botao_exit = None
    botao_rules = None
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi no botão "Jogar"
                if botao_jogar.collidepoint(event.pos):
                    return 'jogar'
                # Verifica se o clique foi no botão "como jogar"
                if botao_rules.collidepoint(event.pos):
                    return 'como jogar'
                if botao_exit.collidepoint(event.pos):
                    return 'sair'

        # Desenha o fundo na tela
        tela.fill((0, 0, 0))
        tela.blit(BackMenu, (0, 0))

        # Configurações do botão "Jogar"
        cor_botao_jogar = (0, 0, 0, 0)  # preto
        largura_botao = 200
        altura_botao = 50
        x_botao = 60
        y_botao = 320
        botao_jogar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        # Configurações do botão "Exit"
        cor_botao_exit = (255, 255, 255)  # branco
        largura_botao_exit = 150
        altura_botao_exit = 50
        x_botao_exit = 60
        y_botao_exit = 420
        botao_exit = pygame.Rect(x_botao_exit, y_botao_exit, largura_botao_exit, altura_botao_exit)

        # Configuração do botão "Rules"
        cor_botao_rules = (255, 255, 255)  # branco
        largura_botao_rules = 200
        altura_botao_rules = 50
        x_botao_rules = 60
        y_botao_rules = 520
        botao_rules = pygame.Rect(x_botao_rules, y_botao_rules, largura_botao_rules, altura_botao_rules)

        # Atualiza a tela
        pygame.display.flip()

def tela_rules():
    # Loop para exibir a tela de início
    inicio = True
    botao_return = None
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi no botão "Return"
                if botao_return.collidepoint(event.pos):
                    return 'menu'
                
        # Desenha o fundo na tela
        tela.fill((0, 0, 0))
        tela.blit(rule_smenu, (0, 0))  

        # Configuração do botão "Return"
        cor_botao = (255, 255, 255)  # branco
        largura_botao_return = 200
        altura_botao_return = 50
        x_botao_return = 60
        y_botao_return = 520
        botao_return = pygame.Rect(x_botao_return, y_botao_return, largura_botao_return, altura_botao_return)  

        # Atualiza a tela
        pygame.display.flip()

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
        image = pygame.image.load('assets/carro-principal.png').convert_alpha()
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
batida = pygame.image.load('assets/crash.png').convert_alpha()
batida_rect = batida.get_rect()



# Inicialização de variáveis
jogando = True
Menu = True
Tela = 'menu'  # Estado inicial do jogo

# Looping principal

while jogando:
        while Menu:
            if Tela == 'menu':
                Tela = tela_de_inicio()
                if Tela == 'como jogar':
                    Tela = tela_rules()
                
            elif Tela == 'como jogar':
                #Loop para exibir a tela de instruções
                while Tela == 'como jogar':
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    #Mostra novo frame
                    pygame.display.update()
            elif Tela == 'sair':
                jogando = False
                Menu = False
                pygame.quit()
                quit()
            else:
                space_pressed = True
                jogando = True
                while jogando:

                    for event in pygame.event.get():
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
                    mov_y += velocidade + 1
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
                                velocidade += 0.2
                    
                    # Desenhar os carros
                    grupo_carros.draw(tela)
                    
                    # Pontuação
                    font = pygame.font.Font(pygame.font.get_default_font(), 20)
                    text = font.render('placar: ' + str(placar), True, preto)
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
                        
                        pygame.draw.rect(tela, branco, (0, 50, largura, 100))
                        
                        font = pygame.font.Font(pygame.font.get_default_font(), 16)
                        text = font.render(f'Você morreu! PLACAR {placar}. Jogar denovo? (Tecle Y ou N)', True, preto)
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
                                jogando = False
                                
                            # Jogar denovo?
                            if event.type == KEYDOWN:
                                if event.key == K_y:
                                    # Reiniciar o jogo
                                    gameover = False
                                    velocidade = 1
                                    placar = 0
                                    grupo_carros.empty()
                                    jog.rect.center = [jog_x, jog_y]
                                elif event.key == K_n:
                                    # Sair dos loops
                                    gameover = False
                                    jogando = False

                pygame.quit()