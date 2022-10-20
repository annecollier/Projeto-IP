import pygame
from pygame.locals import *
from sys import exit
from gameovermenu import gameover
from winmenu import win


import BobGroup
import PontuacaoContagem
import SpriteGroups


def game():
    pygame.init()

    txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)

    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('music_bob.mp3')
    pygame.mixer.music.play(-1)

    altura = 480
    largura = 640
    tela = pygame.display.set_mode((largura, altura))
    background = pygame.image.load(('background2.jpg'))
    icon = pygame.image.load('sprites/bob_1.png')
    vidas = pygame.image.load('coletaveis/vidas.png')
    burguer = pygame.image.load('coletaveis/burguer1.png')
    vidas = pygame.transform.scale(vidas, (26, 26))
    fries = pygame.image.load('coletaveis/fries.png')
    fries = pygame.transform.scale(fries, (29, 32))
    soda = pygame.image.load('coletaveis/soda1.png')
    soda = pygame.transform.scale(soda, (22, 40))
    burguer = pygame.transform.scale(burguer, (26, 26))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Get the B(ob)urger!')
    relogio = pygame.time.Clock()


    while True:
        relogio.tick(100)
        tela.blit(background,(0,0))
        tela.blit(vidas, (255,22))
        tela.blit(burguer, (15, 22))
        tela.blit(soda, (96, 13))
        tela.blit(fries, (170, 17))
        msg1 = f'    : {PontuacaoContagem.burguer}       : {PontuacaoContagem.refri}       :  {PontuacaoContagem.fries}       :{PontuacaoContagem.vidas}'
        posicao = txt.render(msg1, True, (0, 110, 110))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        if pygame.key.get_pressed():
            BobGroup.bob.posicao()
            BobGroup.plancton.posicao()

        if PontuacaoContagem.vidas == 0:
            gameover()

        if PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5:
            win()

        SpriteGroups.todas_sprites.draw(tela)
        SpriteGroups.todas_sprites.update()
        tela.blit(posicao, (20, 20))
        pygame.display.flip()