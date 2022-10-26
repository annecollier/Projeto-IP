import pygame
from random import randint
import RefriSprite
import BurguerSprite
import FriesSprite

def desenhar():
    todas_sprites = pygame.sprite.Group()
    # posicionando 5 elementos de cada sprite em coordenadas pseudoaleatórias
    for i in range(5):
        refri_i = RefriSprite.Refri(randint(65, 980), randint(40, 580))
        todas_sprites.add(refri_i)
        burguer_i = BurguerSprite.Burguer(randint(65, 980), randint(40, 580))
        todas_sprites.add(burguer_i)
        fries_i = FriesSprite.Fries(randint(65, 980), randint(40, 580))
        todas_sprites.add(fries_i)
    return todas_sprites

# função que retorna a sprite do Bob
def bob_desenho():
    bob_menu = pygame.sprite.Group()
    return bob_menu

todas_sprites = desenhar()
bob_menu = bob_desenho()