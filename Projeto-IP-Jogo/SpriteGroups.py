import pygame
from random import randint
import RefriSprite
import BurguerSprite
import FriesSprite


todas_sprites = pygame.sprite.Group()
for i in range(5):
    refri_i = RefriSprite.Refri(randint(40, 1000), randint(40, 600))
    todas_sprites.add(refri_i)
    burguer_i = BurguerSprite.Burguer(randint(40, 1000), randint(40, 600))
    todas_sprites.add(burguer_i)
    fries_i = FriesSprite.Fries(randint(40, 1000), randint(40, 600))
    todas_sprites.add(fries_i)