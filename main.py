import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura = 480

x_blue = 0
y_blue = 0

x_red = 100  # randint(10, 600)
y_red = 100  # randint(10, 600)
vel = 1
n_vel = s_vel = l_vel = o_vel = vel
last_pressed = 0

txt = pygame.font.SysFont('arial', 12, bold=True, italic=False)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Testando')
relogio = pygame.time.Clock()
coletados = 0
colbibli = {"col0": True, "col1": True, "col2": True}
while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    msg = f'coletados: {coletados}'

    nao_sei = txt.render(msg, True, (0, 255, 0))

    # PAREDES RETANGULOS
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_blue, y_blue, 20, 20))
    ret_verm = pygame.draw.rect(tela, (255, 0, 0), (x_red, y_red, 20, 20))
    # cor            cords     tamanhos
    obs_1 = pygame.draw.rect(tela, (255, 255, 100), (100, 30, 200, 25))
    obs_2 = pygame.draw.rect(tela, (255, 255, 100), (350, 30, 200, 25))
    obs_3 = pygame.draw.rect(tela, (255, 255, 100), (100, 55, 25, 150))
    obs_4 = pygame.draw.rect(tela, (255, 255, 100), (525, 55, 25, 150))

    obs_5 = pygame.draw.rect(tela, (255, 255, 100), (100, 255, 25, 150))
    obs_6 = pygame.draw.rect(tela, (255, 255, 100), (100, 405, 200, 25))
    obs_7 = pygame.draw.rect(tela, (255, 255, 100), (350, 405, 200, 25))
    obs_8 = pygame.draw.rect(tela, (255, 255, 100), (525, 255, 25, 150))

    obs_9 = pygame.draw.rect(tela, (255, 255, 100), ((largura / 2) - 100, (altura / 2) - 100, 200, 200))
    if coletados < 300:  # Gambiarra
        if colbibli["col0"] == True:
            coletavel0 = pygame.draw.circle(tela, (255, 20, 20), (50, 400), 10)
        if colbibli["col1"] == True:
            coletavel1 = pygame.draw.circle(tela, (255, 20, 20), (200, 200), 10)
        if colbibli["col2"] == True:
            coletavel2 = pygame.draw.circle(tela, (255, 20, 20), (250, 350), 10)

    # lista coletaveis
    coletaveis_lista = [coletavel0, coletavel1, coletavel2]

    # lista de paredes
    colide_list = [obs_1, obs_2, obs_3, obs_4, obs_5, obs_6, obs_7, obs_8, obs_9]

    # condições
    for i in range(len(coletaveis_lista)):
        if ret_azul.colliderect(coletaveis_lista[i]):
            colbibli[f"col{i}"] = False
            coletados += 1

    if ret_azul.collidelist(colide_list) >= 0:

        if last_pressed == 1:
            o_vel = 0
            x_blue += o_vel
        else:
            o_vel = vel
        if last_pressed == 2:
            l_vel = 0
            x_blue -= o_vel
        else:
            l_vel = vel
        if last_pressed == 3:
            n_vel = 0
            y_blue += o_vel
        else:
            n_vel = vel
        if last_pressed == 4:
            s_vel = 0
            y_blue -= o_vel
        else:
            s_vel = vel


    if pygame.key.get_pressed()[K_a]:
        x_blue -= o_vel
        last_pressed = 1
    if pygame.key.get_pressed()[K_d]:
        x_blue += l_vel
        last_pressed = 2
    if pygame.key.get_pressed()[K_w]:
        y_blue -= n_vel
        last_pressed = 3
    if pygame.key.get_pressed()[K_s]:
        y_blue += s_vel
        last_pressed = 4

    if x_blue == 0:
        o_vel = 0
    if x_blue != 0:
        o_vel = vel

    if y_blue == 0:
        n_vel = 0
    if y_blue != 0:
        n_vel = vel

    if y_blue == 460:
        s_vel = 0
    if y_blue != 460:
        s_vel = vel
    if x_blue == 620:
        l_vel = 0
    if x_blue != 620:
        l_vel = vel
    tela.blit(nao_sei, (20, 20))

    pygame.display.update()




