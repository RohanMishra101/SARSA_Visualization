import numpy as np
import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Analytic:
    def __init__(self, screen, agent):
        self.screen = screen
        self.agent = agent

        self.fig, self.ax = plt.subplots(figsize=(4, 3))
        self.canvas = FigureCanvasAgg(self.fig)


    def goal_visualize(self, top_left=(0, 0), size=(300, 300)):
        value_grid = self.agent.get_grid_value()

        if value_grid is None or isinstance(value_grid, float):  
            return

        # Only redraw if value grid has changed
        if not hasattr(self, 'last_value_grid') or not np.array_equal(self.last_value_grid, value_grid):
            self.last_value_grid = value_grid.copy()

            self.ax.clear()
            self.ax.imshow(value_grid, cmap='Blues', interpolation='nearest')
            self.ax.set_title("Value Grid (V = max Q)")
            self.ax.set_xticks([])
            self.ax.set_yticks([])

            for i in range(value_grid.shape[0]):
                for j in range(value_grid.shape[1]):
                    val = value_grid[i, j]
                    self.ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='black')

            self.fig.tight_layout()
            self.canvas.draw()

            raw_data = self.canvas.buffer_rgba()
            size_tuple = self.canvas.get_width_height()
            surf = pygame.image.frombuffer(raw_data, size_tuple, "RGBA")
            self.cached_surf = pygame.transform.scale(surf, size)

        # Draw cached surface
        self.screen.blit(self.cached_surf, top_left)


    def draw(self):
        self.goal_visualize(top_left=(1100, 200), size=(900, 700)) 
