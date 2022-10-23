import pygame
from sys import exit
from botoes import botao

statuss = "indefinido"

def get_font(size):
    return pygame.font.Font("MenuAssets/font.ttf", size)


def instrucoes1():
    altura = 640
    largura = 1024
    fundo = pygame.image.load("Fundos/Background.png")
    tela = pygame.display.set_mode((largura, altura))
    tela.blit(fundo, (0, 0))
    menu_instrucao_pos = pygame.mouse.get_pos()

    titulo = get_font(45).render("GET THE B(OB)URGUER!", True, "#EEE8AA")
    titulo_espaco = titulo.get_rect(center=(518, 100))
    tela.blit(titulo, titulo_espaco)
    historia = get_font(20).render("hitoriahistoriahistoriahistoriahitoriahistoria", True, "#EEE8AA")
    historia_espaco = titulo.get_rect(center=(510, 300))
    tela.blit(historia, historia_espaco)


    instrucoes = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(290, 530),
                        text_input="INSTRUÇÕES", font=get_font(30), base_color="#d7fcd4",
                        hovering_color="White")
    iniciar = botao(image=pygame.image.load("MenuAssets/Botao Instrucoes.png"), pos=(718, 530),
                           text_input="JOGAR", font=get_font(30), base_color="#d7fcd4",
                           hovering_color="White")

    for button in [instrucoes, iniciar]:
        button.changeColor(menu_instrucao_pos)
        button.update(tela)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if instrucoes.checkForInput(menu_instrucao_pos):
                status = "game"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if iniciar.checkForInput(menu_instrucao_pos):
                status = "game"



