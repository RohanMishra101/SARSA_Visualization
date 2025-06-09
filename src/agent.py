import random
import pygame
import numpy as np
from collections import defaultdict
from src.setting import PLAYER_SPTIRE, TILE_TYPE

class Agent :
    def __init__(self,map,screen):
        self.map = map
        self.screen = screen
        self.agent_width = self.map.tile_size / 1.5
        self.agent_height = self.map.tile_size / 1.5
        self.agent = self.loadAgentImage()
        self.map_pos_data = map.tile_pos
        self.current_pos = self.getCurrentPos()
        self.starting_pos = None
        self.grid_index = None
        self.reached_goal = False
        # SARSA Implementation
        self.action = ["UP","RIGHT","DOWN","LEFT"]
        self.action_n = 4
        self.Q = defaultdict(lambda:np.zeros(self.action_n))
        self.alpha = 0.1 # Learnign rate
        self.gamma = 0.9 # Discount Factor
        self.epsilon_start = 1.0
        self.epsilon_end = 0.1
        self.epsilon_decay = 0.999
        self.epsilon = self.epsilon_start
        self.episode_num = 5000
        self.max_step = 100
        self.current_step = 0
        self.current_episode = 0
        #callback
        self.draw_callback = None
        
        #Analytics
        self.episode_count = ""
        

    
    def loadAgentImage(self):
        raw_image = pygame.image.load(PLAYER_SPTIRE)
        player_image = pygame.transform.scale(raw_image,(self.agent_width,self.agent_height))
        
        return player_image
    
    
    def e_greedy_policy(self,state):
        if random.uniform(0,1) < self.epsilon:
            return random.randint(0,self.action_n - 1)
        else:
            return np.argmax(self.Q[state])
    
    
    def sarsa_implementaion(self):
        while self.current_episode < self.episode_num:
            self.current_episode += 1
            print(self.current_episode)
            self.episode_count = f"Current Episode : {self.current_episode}"
            state = self.reset()
            action = self.e_greedy_policy(state)
            
            done = False
            while not done:
                next_state, reward, terminated, truncated, _ = self.step(action)
                done = terminated or truncated
                next_action = self.e_greedy_policy(next_state)
                
                # SARSA Update
                # print(self.Q[state][action])
                self.Q[state][action] += self.alpha * (reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action])
                
                state = next_state
                action = next_action
                
                if self.draw_callback:
                    self.draw_callback()
                    pygame.time.delay(10)
                    
                yield
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_end)
            yield

    
    def step(self, action):
        x, y = self.grid_index
        
        if action == 0:
            x -= 1
        elif action == 1:
            y += 1
        elif action == 2:
            x += 1
        elif action == 3:
            y -= 1
        
        new_index = (x, y)
        self.current_step += 1
        reward = 0
        terminated = False
        truncated = False
        for tile_types, tiles in self.map_pos_data.items():
            if new_index in tiles:
                walkable = TILE_TYPE[tile_types]['walkable']

                if not walkable:
                    reward -= 1
                    if tile_types == "L":
                        terminated = True
                    break
                
                if tile_types == "G":
                    reward = 1
                    terminated = True
                    self.reached_goal = True
                    
                self.grid_index = new_index
                self.current_pos = tiles[new_index]
                break
        else:
            reward -= 1
        
        truncated = self.current_step >= self.max_step
        # self.display_value_function()
        return self.grid_index, reward, terminated, truncated, {}
      
    
    def reset(self):
        self.getCurrentPos()
        self.current_step = 0
        self.reached_goal = False
        
        return self.grid_index

    
    def getCurrentPos(self):
        pos_data = self.map_pos_data['S']
        (x_indx, y_indx), (x, y) = next(iter(pos_data.items()))
        self.starting_pos = (x_indx, y_indx)
        self.grid_index = self.starting_pos
        self.current_pos = (x, y)
        return self.current_pos
    
    
    def display_value_function(self):
          for state in self.Q.keys():
              best_action = np.argmax(self.Q[state])
              value = np.max(self.Q[state])
            #   print(f"V({state}) = {value:.3f}, Best Action = {self.action[best_action]}")
    
    
    # def get_value_grid(self):
    #     # size = self.map.size  # Assuming square
    #     size = self.map.rows
    #     print("\nValue Grid:")
    #     for x in range(size):
    #         for y in range(size):
    #             state = (x, y)
    #             value = np.max(self.Q[state]) if state in self.Q else 0.0
    #             print(f"{value:5.2f}", end=" ")
    #         print()
    #     return value
        
    def get_value_grid(self):
        size = self.map.rows  # assuming square
        value_grid = np.zeros((size, size))
        print("\nValue Grid:")
        for x in range(size):
            for y in range(size):
                state = (x, y)
                value = np.max(self.Q[state]) if state in self.Q else 0.0
                value_grid[x, y] = value
                print(f"{value:5.2f}", end=" ")
            print()
        return value_grid

    
    
    def set_draw_callback(self, callback):
        self.draw_callback = callback

    
    def draw(self):
        x, y = self.current_pos
        
        pos_x = x - self.agent_width // 2
        pos_y = y - self.agent_height // 2
        self.screen.blit(self.agent,(pos_x,pos_y))