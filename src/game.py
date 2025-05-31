import pygame

# from player import Player
from src.player import Player
from src.setting import FPS, HEIGHT, WHITE, WIDTH
from src.map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.map = Map('map_8x8')
        self.player = Player(self.map)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("MOVE UP!!")
                    self.player.move(0,-self.player.move_speed)
                if event.key == pygame.K_DOWN:
                    print("MOVE DOWN!!")
                    self.player.move(0,self.player.move_speed)
                if event.key == pygame.K_LEFT:
                    print("MOVE LEFT!!")
                    self.player.move(-self.player.move_speed,0)
                if event.key == pygame.K_RIGHT:
                    print("MOVE RIGHT!!")
                    self.player.move(self.player.move_speed,0)
    
    def draw(self):
        self.screen.fill(WHITE)
        self.map.draw(self.screen)
        self.player.draw(self.screen)
        
        pygame.display.flip()