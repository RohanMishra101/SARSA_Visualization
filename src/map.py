import json
import pygame
from src.setting import HEIGHT, MAP_PATH, TILE_TYPE, WIDTH


pygame.font.init()
font = pygame.font.SysFont('Arial', 36)

class Map:
    def __init__(self,map_name):
        self.grid = self.loadMap(MAP_PATH,map_name)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
        self.tile_width = WIDTH // self.cols
        self.tile_height = HEIGHT // self.rows
        self.tile_size = min(self.tile_width,self.tile_height)
        
        self.tile_images = self.loadTileImage()
        
        self.start_pos = self.find_tile('S')
        self.goal_pos = self.find_tile('G')
        
        self.tile_pos = self.get_tile_centers()

    
    
    def loadMap(self,path,map_name):
        with open(path, 'r') as f:
            data = json.load(f)
        
        for m in data['maps']:
            if m['name'] == map_name:
                grid =  [list(row) for row in m['grid']]
        
        print(grid)
        self.validateMap(grid)
        return grid
    
    def loadTileImage(self):
        image = {}
        for symbol, props in TILE_TYPE.items():
            raw_img = pygame.image.load(props['image'])
            scaled_img = pygame.transform.scale(raw_img,(self.tile_size,self.tile_size))
            image[symbol] = scaled_img
        
        return image
    
    def validateMap(self,grid):
        flat = [cell for row in grid for cell in row]
        if flat.count('S') != 1 or flat.count('G') != 1:
            raise ValueError("Map must have exactly one Start (S) and one Goal (E).")
        width = len(grid[0])
        for row in grid:
            if len(row) != width:
                raise ValueError("All rows in the map must have the same lenght.")
    
    def find_tile(self, symbol):
        for row_indx, row in enumerate(self.grid):
            for col_indx, cell in enumerate(row):
                if cell == symbol:
                    return (row_indx, col_indx)
        return None

    def get_tile_centers(self):
        tile_pos = {}
        for row in range(self.rows):
            for col in range(self.cols):
                tile = self.grid[row][col]  # Assuming each cell has one tile type, like 'S', 'E', etc.
                x = col * self.tile_size + self.tile_size // 2
                y = row * self.tile_size + self.tile_size // 2
                center = (x, y)
    
                if tile not in tile_pos:
                    tile_pos[tile] = {}
                tile_pos[tile][(row, col)] = center
        return tile_pos
    
    def draw(self, surface):
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                if cell not in self.tile_images:
                    print(f"Unknown tile symbol '{cell}' at ({row_idx}, {col_idx})")
                    continue  # Skip drawing
                x = col_idx * self.tile_size
                y = row_idx * self.tile_size
                
                surface.blit(self.tile_images[cell], (x, y))
                
                # Draw semi-transparent border
                self.draw_tile_border(surface, x, y, self.tile_size, color=(0, 0, 0), alpha=100, border_width=1)
                
    def draw_tile_border(self, surface, x, y, size, color=(0, 0, 0), alpha=100, border_width=1):
        border_surf = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.rect(border_surf, (*color, alpha), border_surf.get_rect(), border_width)
        surface.blit(border_surf, (x, y))
