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


    altura = 480
    largura = 640
    tela = pygame.display.set_mode((largura, altura))
    background = pygame.image.load(('background2.jpg'))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('music_bob.mp3')
    pygame.mixer.music.play(-1)
    icon = pygame.image.load('sprites/bob_1.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Get the B(ob)urger!')


    relogio = pygame.time.Clock()


    while True:
        relogio.tick(100)
        tela.blit(background,(0,0))
        msg1 = f'Carne: {PontuacaoContagem.carne}  Alface: {PontuacaoContagem.alface}   Pão:  {PontuacaoContagem.pao}  Vidas:{PontuacaoContagem.vidas}'
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

        if PontuacaoContagem.carne == PontuacaoContagem.pao == PontuacaoContagem.alface == 5:
            win()

        SpriteGroups.todas_sprites.draw(tela)
        SpriteGroups.todas_sprites.update()
        tela.blit(posicao, (20, 20))
        pygame.display.flip()


