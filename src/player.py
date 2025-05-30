from src.setting import PLAYER_SPTIRE


class Player:
    def __init__(self,map):
        self.map = map
        self.player = PLAYER_SPTIRE
        self.pos = map.tile_pos
    
    
    def move(self):
        pass
    
    def draw(self):
        pass