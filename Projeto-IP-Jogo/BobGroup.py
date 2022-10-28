import SpongeSprite
import SpriteGroups
import PlanctonSprite

import bobintrucoes
import BobInstrucoes2

def personagens():
    bob = SpongeSprite.Sponge()
    plancton = PlanctonSprite.Plancton()
    SpriteGroups.todas_sprites.add(bob)
    SpriteGroups.todas_sprites.add(plancton)
    return bob,plancton

def personagens_menu():
    bob_menu = bobintrucoes.BobMenu()
    SpriteGroups.bob_menu.add(bob_menu)
    return bob_menu

def personagens_menu2():
    bob_menu2 = BobInstrucoes2.BobMenu2()
    SpriteGroups.personagensmenu2.add(bob_menu2)
    return bob_menu2

bob,plancton = personagens()
bob_menu = personagens_menu()
bob_menu2 = personagens_menu2()
