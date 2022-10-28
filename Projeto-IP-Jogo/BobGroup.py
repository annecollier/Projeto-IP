import SpongeSprite
import SpriteGroups
import PlanctonSprite

import BobInstrucoes
import BobInstrucoes2
import BobInstrucoes3
import PlanctonInstrucoes

def personagens():
    bob = SpongeSprite.Sponge()
    plancton = PlanctonSprite.Plancton()
    SpriteGroups.todas_sprites.add(bob)
    SpriteGroups.todas_sprites.add(plancton)
    return bob,plancton

def personagens_menu():
    bob_menu = BobInstrucoes.BobMenu()
    SpriteGroups.bob_menu.add(bob_menu)
    return bob_menu

def personagens_menu2():
    bob_menu2 = BobInstrucoes2.BobMenu2()
    SpriteGroups.personagensmenu2.add(bob_menu2)
    return bob_menu2

def personagens_menu3():
    bob_menu3 = BobInstrucoes3.BobMenu3()
    plancton_menu = PlanctonInstrucoes.PlanctonMenu()
    SpriteGroups.personagensmenu3.add(bob_menu3)
    SpriteGroups.personagensmenu3.add(plancton_menu)
    return bob_menu3,plancton_menu

bob,plancton = personagens()
bob_menu = personagens_menu()
bob_menu2 = personagens_menu2()
bob_menu3,plancton_menu = personagens_menu3()
