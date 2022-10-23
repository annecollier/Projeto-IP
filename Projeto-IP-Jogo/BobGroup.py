import SpongeSprite
import SpriteGroups
import PlanctonSprite

def personagens():
    bob = SpongeSprite.Sponge()
    plancton = PlanctonSprite.Plancton()
    SpriteGroups.todas_sprites.add(bob)
    SpriteGroups.todas_sprites.add(plancton)
    SpriteGroups.bob.add(bob)
    return bob,plancton

bob,plancton = personagens()
