import pygame
from .constants import ROWS,GREEN,WHITE , SQUARE_SIZE

class Board:
    def __int__(self):
        self.board = []
        self.selected_piece = None
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
    def draw_cubes(self,win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row %2,ROWS,2):
                pygame.draw.rect(win,GREEN,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    def create_board(self):
        pass