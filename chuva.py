import pygame
from sys import exit
from random import randint, choice 

def animacao_rochas():
    global movimento_rochas

    if fundo_rochas_voadoras_rect.y <= -20:
        movimento_rochas = 1
    elif fundo_rochas_voadoras_rect.y >= 20:
        movimento_rochas = -1
    
    fundo_rochas_voadoras_rect.y += movimento_rochas
 
    tela.blit(fundo_rochas_voadoras, fundo_rochas_voadoras_rect)

def animacao_estrelas():
    global index_estrelas
    index_estrelas = 0.222

    if (index_estrelas >= 4):
        index_estrelas = 0


    if (int(index_estrelas) == 0):
        tela.blit(fundo_estrelas, (0, 0))
    elif (int(index_estrelas) == 1):
        tela.blit(fundo_estrelas_2, (0, 0))
    else:
        tela.blit(fundo_estrelas_3, (0, 0))

def animacao_personagem():
    global jogador_index
    # Calcula o movimento do personagem
    jogador_retangulo.x += movimento_personagem
    # jogador_surface = null

    if movimento_personagem == 0: # Jogador está parado
        jogador_surfaces = jogador_parado_superficies
    else: # Jogador está se movimentando
        jogador_surfaces = jogador_voando_superficies

    # Avança para o proximo frame
    jogador_index += 0.11
    if jogador_index > len(jogador_surfaces) - 1:
        jogador_index = 0

    if direcao_personagem == 1:
        jogador = pygame.transform.flip(jogador_surfaces[int(jogador_index)], True, False)
    else:
        jogador = jogador_surfaces[int(jogador_index)]

    # Desenha o jogador na tela
    tela.blit(jogador, jogador_retangulo)


def adicionar_objeto():
    global chuva_objetos

    objetos_lista_aleatoria = ['Coracao'] * 10 + ['Moeda'] * 10 + ['Projetil'] * 80
    tipo_objeto = choice(objetos_lista_aleatoria)

    posicao = (randint(10, 950), randint(-100, 0))
    velocidade = randint(5, 10)



    if tipo_objeto == 'Projetil':
        objeto_rect = projetil_surfaces[0].get_rect(center=posicao)
        chuva_objetos.append({
            'tipo' : 'Projetil',
            'retangulo' : objeto_rect,
            'velocidade' : velocidade
        })

    if tipo_objeto == 'Coracao':
        objeto_rect = coracao_surfaces[0].get_rect(center=posicao)
        chuva_objetos.append({
            'tipo' : 'Coracao',
            'retangulo' : objeto_rect,
            'velocidade' : velocidade
        })

    if tipo_objeto == 'Moeda':    
        objeto_rect = moeda_surfaces[0].get_rect(center=posicao)
        chuva_objetos.append({
        'tipo' : 'Moeda',
        'retangulo' : objeto_rect,
        'velocidade' : velocidade
        })

def movimento_objetos_chuva():
    global chuva_objetos

    for objeto in chuva_objetos:
        
        objeto['retangulo'].y += objeto['velocidade']

        if objeto['tipo'] == 'Projetil':
            tela.blit(projetil_surfaces[projetil_index], objeto['retangulo'])
        elif objeto['tipo'] == 'Coracao':
            tela.blit(coracao_surfaces[coracao_index], objeto['retangulo'])
        elif objeto['tipo'] == 'Moeda':
            tela.blit(moeda_surfaces[projetil_index], objeto['retangulo'])  
              
# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("ChuvaMortal")

##
## Importa os arquivos necessários
##

# Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
fundo_estrelas = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
fundo_estrelas_2 = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
fundo_estrelas_3 = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
fundo_rochas = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
fundo_chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
fundo_rochas_voadoras = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()
fundo_lua = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
fundo_estrelas = pygame.transform.scale(fundo_estrelas, tamanho)
fundo_estrelas_2 = pygame.transform.scale(fundo_estrelas_2, tamanho)
fundo_estrelas_3 = pygame.transform.scale(fundo_estrelas_3, tamanho)
fundo_rochas = pygame.transform.scale(fundo_rochas, tamanho)
fundo_chao = pygame.transform.scale(fundo_chao, tamanho)
fundo_lua = pygame.transform.scale(fundo_lua, tamanho)
fundo_rochas_voadoras = pygame.transform.scale(fundo_rochas_voadoras, tamanho)
fundo_rochas_voadoras_rect = fundo_rochas_voadoras.get_rect(topleft = (0,0))
index_estrelas = 0
movimento_rochas = 1


# Carrega as imagens do personagem
jogador_index = 0
jogador_parado_superficies = []
jogador_voando_superficies = []



#carrega a imagens da chuva
coracao_surfaces = []
coracao_index = 0
for coracao in range(1,4):
    img_coracao = pygame.image.load(f'assets/objetos/coracao/Heart{coracao}.png').convert_alpha()
    img_coracao = pygame.transform.scale(img_coracao, (80,80))
    coracao_surfaces.append(img_coracao)

moeda_surfaces = []
moeda_index = 0
for moeda in range(1,5):
    img_moeda = pygame.image.load(f'assets/objetos/moeda/Coin-A{moeda}.png').convert_alpha()
    img_moeda = pygame.transform.scale(img_moeda, (80, 80))
    moeda_surfaces.append(img_moeda)

projetil_surfaces = []
projetil_index =0
for projetil in range(1,4):
    img_projetil = pygame.image.load(f'assets/objetos/projetil/Hero Bullet{projetil}.png').convert_alpha()
    projetil_surfaces.append(img_projetil) 

##guarda os objetos que vão cair do céu
chuva_objetos = []   


# Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()


# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0

#criar um evento para adicionar um objeto na tela
novo_objeto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_objeto_timer, 500)

# Carrega o jogador parado
for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_superficies.append(img)

# Carrega o jogador se movimentando
for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_superficies.append(img),



jogador_retangulo = jogador_parado_superficies[jogador_index].get_rect( center = (100, 430))


# Loop principal do jogo
while True:
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5
                direcao_personagem = 1

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5
                direcao_personagem = 0

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0

            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

        if evento.type == novo_objeto_timer:
            adicionar_objeto()

    # Desenha o fundo na tela
    tela.blit(plano_fundo, (0, 0))

    animacao_estrelas()

   

    animacao_rochas()

    tela.blit(fundo_rochas, (0, 0))
    tela.blit(fundo_chao, (0, 0))
    tela.blit(fundo_lua, (0, 0))
    
    


    # Faz a chamada da função animação do personagem
    animacao_personagem()

    movimento_objetos_chuva()

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)