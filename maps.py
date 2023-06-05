import pygame, pytmx, pyscroll, mobs

class Map():
    def __init__(self, tilemapPath):
        self.tmx_data = pytmx.util_pygame.load_pygame("data/tilemaps/"+tilemapPath+".tmx")
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, (1280,720))

        self.collisions=[]
        for obj in self.tmx_data.get_layer_by_name("Collisions"):
            self.collisions.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.playerSpawnpoint = None
        self.hostileMobs=pygame.sprite.Group()
        self.hostileMobsItems=pygame.sprite.Group()

        for k in self.tmx_data.get_layer_by_name("Points"):
            if k.mobType == "player":
                self.playerSpawnpoint = k
            if k.mobType == "hostileMob":
                a=mobs.hostileMobs[k.mobName]
                a.setSpawnPoint((k.x, k.y))
                self.hostileMobs.add(a)
        
        for k in self.hostileMobs:
            self.hostileMobsItems.add(k.weapon)