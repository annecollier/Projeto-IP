import pygame
from random import randint
import BobGroup
import PontuacaoContagem

class Plancton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/plancton.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (40.3, 71.5))
        self.rect = self.image.get_rect()
        self.x_planc = randint(40,600)
        self.y_planc = randint(40,420)
        self.change_position = 1
        self.rect.topleft = self.x_planc,self.y_planc
        self.ida_horizontal = True
        self.ida_vertical = True

    def subindo(self):
        self.y_planc += self.change_position
        if self.y_planc == 480:
            self.ida_vertical = False
        return self
    def descendo(self):
        self.y_planc -= self.change_position
        if self.y_planc == 0:
            self.ida_vertical = True
        return self
    def direita(self):
        self.x_planc += self.change_position
        if self.x_planc == 640:
            self.ida_horizontal = False
        return self
    def esquerda(self):
        self.x_planc -= self.change_position
        if self.x_planc == 0:
            self.ida_horizontal: True
        return self
    def posicao(self):
        if self.ida_horizontal:
            Plancton.direita()
        else:
            Plancton.esquerda()
        if self.ida_vertical:
            Plancton.subindo()
        else:
            Plancton.descendo()
        self.rect.topleft = self.x_planc, self.y_planc

    def update(self):
        if self.rect.colliderect(BobGroup.bob.rect):
            print('Vida perdida!')
            PontuacaoContagem.vidas -= 1

