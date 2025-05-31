import pygame
from src.setting import PLAYER_SPTIRE

class Player:
    def __init__(self,map):
        self.map = map
        
        self.player_width = self.map.tile_size / 1.5
        self.player_height = self.map.tile_size / 1.5
        
        self.player = self.loadPlayerImage()
        
        self.map_pos_data = map.tile_pos
        self.current_pos = None
        self.grid_index = None
        self.move_speed = 1
        # print(self.map_pos_data)
    
    def loadPlayerImage(self):
        raw_image = pygame.image.load(PLAYER_SPTIRE)
        player_image = pygame.transform.scale(raw_image,(self.player_width,self.player_height))
        
        return player_image
      
    def move(self,x,y):
        
        new_index = (self.grid_index[0] + y, self.grid_index[1] + x)
        
        for tile_type, tiles in self.map_pos_data.items():
            print(tiles)
            if new_index in tiles:
                self.grid_index = new_index
                self.current_pos = tiles[new_index]
                return
                
        # print(self.grid_index)
        # for tile_type, tiles in self.map_pos_data.items():
        #     # print(f"Tile Type: {tile_type}")
        #     for grid_index, pixel_position in tiles.items():
        #         # print(f"  Grid Index: {grid_index}, Pixel Position: {pixel_position}")
                
        #         pos_x, pos_y = self.grid_index
        #         self.grid_index = (pos_x + x,pos_y + y)
                
        #         if grid_index == self.grid_index:
        #             print(pixel_position)
        #             self.current_pos = pixel_position
        
    def getCurrentPos(self):
        pos_data = self.map_pos_data['S']
        (x_indx,y_indx), (x,y) = next(iter(pos_data.items()))
        self.current_pos = (x,y)
        self.grid_index = (x_indx,y_indx)
        print(f"GRID INDEX : {self.grid_index}")
        
        return self.current_pos
            
    def draw(self,surface):
        if self.current_pos == None:
            self.current_pos = self.getCurrentPos()
            print(self.current_pos)
        else:
            x, y = self.current_pos
            
            pos_x = x - self.player_width // 2
            pos_y = y - self.player_height // 2
            
            surface.blit(self.player,(pos_x,pos_y))