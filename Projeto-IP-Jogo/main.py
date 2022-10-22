import pygame
from pygame.locals import *
from sys import exit
from botoes import botao

import BobGroup
import PontuacaoContagem
import SpriteGroups


def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def game():
    pygame.init()

    txt = pygame.font.SysFont('arial', 25, bold=True, italic=False)

    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('music_bob.mp3')
    pygame.mixer.music.play(-1)

    altura = 640
    largura = 1024
    background = pygame.image.load(('fundomapa.jpg'))
    icon = pygame.image.load('sprites/bob_1.png')
    vidas = pygame.image.load('coletaveis/vidas.png')
    burguer = pygame.image.load('coletaveis/burguer1.png')
    burguer = pygame.transform.scale(burguer, (26, 26))
    vidas = pygame.transform.scale(vidas, (26, 26))
    fries = pygame.image.load('coletaveis/fries.png')
    fries = pygame.transform.scale(fries, (29, 32))
    soda = pygame.image.load('coletaveis/soda1.png')
    soda = pygame.transform.scale(soda, (22, 40))

    pygame.display.set_icon(icon)
    pygame.display.set_caption('Get the B(ob)urger!')
    relogio = pygame.time.Clock()
    status = "start"

    while True:
        if status == "game":
            tela = pygame.display.set_mode((largura, altura))
            relogio.tick(100)
            tela.blit(background,(0,0))
            tela.blit(vidas, (218,22))
            tela.blit(burguer, (15, 22))
            tela.blit(soda, (82, 13))
            tela.blit(fries, (145, 17))
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
                morte = pygame.mixer.Sound('morte.wav')
                pygame.mixer.Sound.set_volume(morte, 1)
                morte.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "gameover"

            if PontuacaoContagem.burguer == PontuacaoContagem.fries == PontuacaoContagem.refri == 5:
                venceu = pygame.mixer.Sound('venceu.wav')
                pygame.mixer.Sound.set_volume(venceu, 1)
                venceu.play()
                PontuacaoContagem.burguer = PontuacaoContagem.refri = PontuacaoContagem.fries = 0
                PontuacaoContagem.vidas = 3
                SpriteGroups.todas_sprites = SpriteGroups.desenhar()
                status = "win"
            SpriteGroups.todas_sprites.draw(tela)
            SpriteGroups.todas_sprites.update()
            tela.blit(posicao, (20, 20))
            pygame.display.flip()
            pygame.display.update()

        if status == "start":
            fundo = pygame.image.load("Fundos/Background.png")
            tela = pygame.display.set_mode((largura,altura))
            tela.blit(fundo, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(52).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
            MENU_RECT = MENU_TEXT.get_rect(center=(518, 100))

            PLAY_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 250),
                                text_input="INICIAR", font=get_font(70), base_color="#d7fcd4",
                                hovering_color="White")
            OPTIONS_BUTTON = botao(image=pygame.image.load("MenuAssets/Options Rect.png"), pos=(518, 400),
                                   text_input="OPÇÕES", font=get_font(70), base_color="#d7fcd4",
                                   hovering_color="White")
            QUIT_BUTTON = botao(image=pygame.image.load("MenuAssets/Quit Rect.png"), pos=(920, 590),
                                text_input="SAIR", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

            tela.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        status = "game"
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        exit()

            pygame.display.update()

        if status == "win":
            tela = pygame.display.set_mode((largura, altura))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            OPTIONS_TEXT = get_font(45).render("Você ganhou!!", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(518, 260))
            tela.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = botao(image=None, pos=(518, 460),
                                 text_input="Voltar", font=get_font(70), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(tela)

            for button in [OPTIONS_BACK]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        status = "start"
            pygame.display.update()

        if status == "gameover":
            tela = pygame.display.set_mode((largura, altura))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            tela.blit(fundo, (0, 0))

            texto_gameover = get_font(45).render("GAME OVER", True, "Black")
            OPTIONS_RECT = texto_gameover.get_rect(center=(518, 260))
            tela.blit(texto_gameover, OPTIONS_RECT)

            OPTIONS_BACK = botao(image=None, pos=(518, 460),
                                 text_input="Tente de novo", font=get_font(70), base_color="Black",
                                 hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(tela)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        status = "start"


            pygame.display.update()

        pygame.display.update()
if __name__ == '__main__':
    game()