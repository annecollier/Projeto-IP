import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 480
largura = 640


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Bob Esponja')

class Sponge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/bob1.png'))
        self.sprites.append(pygame.image.load('sprites/bob2.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.x_bob = 100
        self.y_bob = 100
        self.rect.topleft = self.x_bob,self.y_bob
        self.animar = False

    def andar(self):
        self.animar = True

    def posicao(self):
        if pygame.key.get_pressed()[K_a]: 
            self.x_bob -= 10 
            if self.x_bob <= 0:
                self.x_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_d]:
            self.x_bob += 10
            if self.x_bob >= 580:
                self.x_bob = 580
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_w]:
            self.y_bob -= 10
            if self.y_bob <= 0:
                self.y_bob = 0
            self.rect.topleft = self.x_bob,self.y_bob
        if pygame.key.get_pressed()[K_s]:
            self.y_bob += 10
            if self.y_bob >= 400:
                self.y_bob = 400
            self.rect.topleft = self.x_bob,self.y_bob

    def update(self):
        if self.animar == True:
            self.atual += 0.25
            if self.atual >= len(self.sprites):
                self.atual = 0 
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (50, 50))


todas_sprites = pygame.sprite.Group()
bob = Sponge()
todas_sprites.add(bob)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,110,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_s]:  
            bob.andar()
            bob.posicao()

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()
