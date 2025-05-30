WIDTH = 1920
HEIGHT = 1080
FPS = 60
WHITE = (255,255,255)

TILE_TYPE = {
    'S':{'name':'start','walkable':True,'image':'assets\\img\\start_tile.png'},
    'T':{'name':'rock','walkable':False,'image':'assets\\img\\rock_tile.png'},
    'L':{'name':'lake','walkable':False,'image':'assets\\img\\water_tile.png'},
    'G':{'name':'goal','walkable':True,'image':'assets\\img\\start_tile.png'},
    'E':{'name':'grass','walkable':True,'image':'assets\\img\\grass_tile.png'},
}
MAP_PATH = "map\\maps.json"

PLAYER_SPTIRE = "assets\\img\\Ghost.png"