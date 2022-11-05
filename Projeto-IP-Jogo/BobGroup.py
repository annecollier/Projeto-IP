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


class Personagens_menu():

    def __init__(self):

        self.bob_menu = Personagens_menu.personagens_menu(self)
        self.bob_menu2 = Personagens_menu.personagens_menu2(self)
        self.bob_menu3 = Personagens_menu.personagens_menu3(self)
        self.plancton_menu = Personagens_menu.personagens_menu3(self)


    def personagens_menu(self):
        self.bob_menu = BobInstrucoes.BobMenu()
        SpriteGroups.bob_menu.add(self.bob_menu)

    def personagens_menu2(self):
        self.bob_menu2 = BobInstrucoes2.BobMenu2()
        SpriteGroups.personagensmenu2.add(self.bob_menu2)

    def personagens_menu3(self):
        self.bob_menu3 = BobInstrucoes3.BobMenu3()
        self.plancton_menu = PlanctonInstrucoes.PlanctonMenu()
        SpriteGroups.personagensmenu3.add(self.bob_menu3)
        SpriteGroups.personagensmenu3.add(self.plancton_menu)

personagens = Personagens()
menus = Personagens_menu()






