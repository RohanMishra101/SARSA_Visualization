import pygame

# from player import Player
from src.agent import Agent
from src.setting import FPS, HEIGHT, WHITE, WIDTH
from src.map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.map = Map('map_8x8')
        self.agent = Agent(self.map,self.screen)
        pygame.display.set_caption("SARSA Visualization using Game")
        self.clock = pygame.time.Clock()
        
        self.agent.set_draw_callback(self.draw)
        self.sarsa_gen = self.agent.sarsa_implementaion()
        self.running = True
        
        self.font_family = "arial"
        self.font_header = pygame.font.SysFont(self.font_family,44,  bold=True)
        self.font = pygame.font.SysFont(self.font_family,28,bold=True)
        
    def run(self):
        self.agent.sarsa_implementaion()
        while self.running:
            self.clock.tick(FPS)
            self.handleEvents()
            
            try:
                next(self.sarsa_gen)
            except StopIteration:
                pass
            
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
        
        self.screen.blit(self.font_header.render("SARSA IMPLEMENTATION",True,(0,0,0)), (1400,50))
        # self.screen.blit(self.font.render(self.agent.current_episode))
        
        pygame.display.flip()
        pygame.event.pump()