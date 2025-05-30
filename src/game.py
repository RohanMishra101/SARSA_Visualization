import pygame

from src.setting import FPS, HEIGHT, WHITE, WIDTH
from src.map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.map = Map('map_4x4')
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("SARSA Visualization using Game")
        self.clock = pygame.time.Clock()
        
        self.running = True
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handleEvents()
            self.draw()
        
        pygame.quit()
    
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        
        
        pygame.display.flip()