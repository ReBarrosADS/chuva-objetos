import pygame
from sys import exit
import time

pygame.init()

#Cria a tela
tamanho =(960, 540)
tela = pygame.display.set_mode(tamanho)

##
##Importa os arquivos nescessários
##

#Carrega
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
estrelas_sete = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
estrelas_seis = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
estrelas_cinco = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
montanhas = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
terreno_rochoso = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
lua_flutuante = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
pedras_flutuante = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()





#Transforma o tamanho da imagen
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
estrelas_sete = pygame.transform.scale(estrelas_sete, tamanho)
estrelas_seis = pygame.transform.scale(estrelas_seis, tamanho)
estrelas_cinco = pygame.transform.scale(estrelas_cinco, tamanho)
montanhas = pygame.transform.scale(montanhas, tamanho)
terreno_rochoso = pygame.transform.scale(terreno_rochoso, tamanho)
lua_flutuante = pygame.transform.scale(lua_flutuante,tamanho)
pedras_flutuante = pygame.transform.scale(pedras_flutuante,tamanho)


#importar o personagem
jogador_parado_surf = pygame.image.load("assets/jogador/parado/Hero Boy Idle1.png").convert_alpha()
jogador_parado_rect = jogador_parado_surf.get_rect(midbottom=(100, 530))



#Defina o titulo da janela
pygame.display.set_caption("ChuvaMortal")

#Criar um relógio para controlar os FPS
relogio = pygame.time.Clock()
movimento_personagem = 0



#loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5
            
            if evento.type == pygame.K_LEFT:
                movimento_personagem =- 5


    
    tela.blit(plano_fundo, (0,0))
    tela.blit(estrelas_sete, (0,0))
    tela.blit(estrelas_seis, (0,0))
    tela.blit(estrelas_cinco, (0,0))
    tela.blit(montanhas, (0,0))
    tela.blit(terreno_rochoso,(0,0))
    tela.blit(lua_flutuante,(0,0))
    tela.blit(pedras_flutuante,(0,0))
    

    tela.blit(jogador_parado_surf, jogador_parado_rect)
    jogador_parado_rect.x += movimento_personagem
    #atualizar a tela com o conteudo
    pygame.display.update()
    #define a quantidade de frames por segundo
    relogio.tick(60)



