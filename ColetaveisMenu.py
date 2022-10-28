import pygame
import BobGroup


class FriesMenu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/fries.png'))
        self.sprites.append(pygame.image.load('coletaveis/fries2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (29,31))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (29, 31))
        if self.rect.colliderect(BobGroup.bob_menu2.rect):
            print('Batatinha Coletada!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()

class BurguerMenu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/burguer1.png'))
        self.sprites.append(pygame.image.load('coletaveis/burguer2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (28,28))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (28,28))
        if self.rect.colliderect(BobGroup.bob_menu2.rect):
            print('Burguer Coletado!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()

class RefriMenu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('coletaveis/soda1.png'))
        self.sprites.append(pygame.image.load('coletaveis/soda2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (25,40))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x,self.y

    # atualizando a sprite
    def update(self):
        self.atual += 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (25,40))
        # se o bob colidir com a soda, a sprite é eliminada
        if self.rect.colliderect(BobGroup.bob_menu2.rect):
            print('Refri Coletado!')
            coletou = pygame.mixer.Sound('sons/temacoletados.wav')
            pygame.mixer.Sound.set_volume(coletou, 0.2)
            coletou.play()
            self.kill()

