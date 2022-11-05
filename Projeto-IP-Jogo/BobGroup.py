#importacoes necessarias
import SpongeSprite
import SpriteGroups
import PlanctonSprite
import inimigo_2

import BobInstrucoes
import BobInstrucoes2
import BobInstrucoes3
import PlanctonInstrucoes
class Personagens():
    def __init__(self):
        self.bob = SpongeSprite.Sponge()
        self.plancton = PlanctonSprite.Plancton()
        self.plancton2 = inimigo_2.Plancton_2()
        SpriteGroups.todas_sprites.add(self.bob)
        SpriteGroups.todas_sprites.add(self.plancton)
        #return self.bob, self.plancton, self.plancton2


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

personagens = Personagens()
bob_menu = personagens_menu()
bob_menu2 = personagens_menu2()
bob_menu3,plancton_menu = personagens_menu3()