import pygame
import config as cf
import os
from random import randint
from random import randrange

pygame.mixer.init()

def musica_partida():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(cf.diretorio_sons, 'musica_partida.mp3'))
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

def inicio_partida():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(cf.diretorio_sons, 'inicio_partida.wav'))
    pygame.mixer.music.set_volume(0.35)
    pygame.mixer.music.play(1)

def musica_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(cf.diretorio_sons, 'musica_menu.mp3'))
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)


def moeda_contador():
    cf.contador + 1
    if cf.contador // 5 == 0:
        cf.VELOCIDADE =+ 3
    print(f'ta contando {cf.contador}')

#Essa função vai reiniciar os parâmetros do jogo
def reiniciar_jogo():
    cf.contador = 0
    cf.segundo = 0
    cf.minuto = 0
    cf.rua_numero = 0
    cf.morreu = False
    cf.carro_pos_x = 555
    cf.carro_pos_y = 556
    cf.car_pos_x = randrange(355, 755, 100)
    cf.car_pos_y = randint(- 350, - 200)
    cf.pedra_pos_x = randrange(360, 760, 100)
    cf.pedra_pos_y = randint(- 1100, - 950)
    cf.buraco_pos_x = randrange(355, 755, 100)
    cf.buraco_pos_y = randint(- 890, - 750)
    cf.tronco_pos_x = randrange(360, 760, 100)
    cf.tronco_pos_y = randint(- 600, - 470)
    cf.VELOCIDADE = 10
    cf.jogar = False
    cf.ganhou = False
    cf.morreu = False
    pygame.display.update()

def tempo():
    if cf.contador == 60:
        cf.segundo += 1
        cf.contador = 0
        if cf.segundo == 60:
            cf.segundo = 0
            cf.minuto += 1
    if (cf.segundo % 10) == 0:
        cf.VELOCIDADE = cf.VELOCIDADE + 0.05


def menu_skin():
    if cf.escolha_skin == 0:
        return cf.carro_amarelo_cortado
    elif cf.escolha_skin == 1:
        return cf.carro_preto_cortado
    elif cf.escolha_skin == 2:
        return cf.carro_azul_cortado
    elif cf.escolha_skin == 3:
        return cf.carro_rosa_cortado
    elif cf.escolha_skin == 4:
        return cf.carro_vermelho_cortado
    elif cf.escolha_skin == 5:
        return cf.carro_branco_cortado
