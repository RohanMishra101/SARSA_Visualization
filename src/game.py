import pygame

# from player import Player
from src.agent import Agent
from src.setting import FPS, HEIGHT, WHITE, WIDTH
from src.map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.map = Map('map_4x4')
        self.agent = Agent(self.map,self.screen)
        pygame.display.set_caption("SARSA Visualization using Game")
        self.clock = pygame.time.Clock()
        
        self.agent.set_draw_callback(self.draw)
        
        self.running = True
        
    def run(self):
        self.agent.sarsa_implementaion()
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
        self.agent.draw()
        
        pygame.display.flip()
        pygame.event.pump()