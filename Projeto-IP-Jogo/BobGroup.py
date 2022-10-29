import SpongeSprite
import SpriteGroups
import PlanctonSprite
import inimigo_2

import BobInstrucoes

def personagens():
    bob = SpongeSprite.Sponge()
    plancton = PlanctonSprite.Plancton()
    plancton2 = inimigo_2.Plancton_2()
    SpriteGroups.todas_sprites.add(bob)
    SpriteGroups.todas_sprites.add(plancton)
    return bob, plancton, plancton2

def personagens_menu():
    bob_menu = BobInstrucoes.BobMenu()
    SpriteGroups.bob_menu.add(bob_menu)
    return bob_menu

bob, plancton, plancton2 = personagens()
bob_menu = personagens_menu()