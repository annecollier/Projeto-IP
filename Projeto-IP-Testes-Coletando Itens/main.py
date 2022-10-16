import pygame
from pygame.locals import *
from sys import exit
import BobGroup
import PontuacaoContagem
import SpriteGroups


pygame.init()


txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)


altura = 480
largura = 640
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Bob Esponja')


relogio = pygame.time.Clock()



while True:
    relogio.tick(100)
    tela.fill((0,110,100))
    msg1 = f'Carne: {PontuacaoContagem.carne}  Alface: {PontuacaoContagem.alface}   Pão:  {PontuacaoContagem.pao}'
    posicao = txt.render(msg1, True, (0, 255, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed():
        BobGroup.bob.posicao()
    SpriteGroups.todas_sprites.draw(tela)
    SpriteGroups.todas_sprites.update()
    tela.blit(posicao, (20, 20))
    pygame.display.flip()