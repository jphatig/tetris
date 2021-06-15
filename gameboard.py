# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
import numpy as np

class GameBoard:
    """Define tetris game gameboard"""

    def __init__(self, width, height, surface):
        """Define gameboard default parameters"""
        self.canvas = np.zeros((height, width, 3), np.uint32)
        self.surface = surface
        self.width = width
        self.height = height
        self.score = 0
        self.base_points = 100
        self.score_rank = {1: 100, 2: 200, 3: 400, 4: 800}
        self.color = (0, 0, 0)
        self.border_color = (255, 255, 255)
        self.draw_canvas_border()

    def compute_points(self, rows, points, row=1):
        """Compute score points based on clenaed rows"""
        if row == rows:
            return points
        points *= 2
        return self.compute_points(rows, points, row + 1)

    def draw_canvas_border(self):
        """Draw gameboard borders and separators"""
        for i in range(0, self.width):
            for j in range(0, self.height):#                                580 generates -1 white color
                if (j >= 0 and j <= 19) or (j >= 380 and j <= 399) or (i >= 580 and i <= 600) or (i >= 200 and i <= 219 and j >= 399) or (i >= 0 and i <= 19 and j >= 399) or (j >= 580 and j <= 599):
                    for x in range(0, 3):
                        self.canvas.itemset((j, i, x), self.border_color[x])

    def draw_shape(self, x, y, width, height, color):
        """Draw shape on gameboard"""
        for i in range(int(x), int(x + width)):
            for j in range(int(y), int(y + height)):
                for x in range(0, 3):
                    self.canvas.itemset((i, j, x), color[x])

    def _is_row_complete(self, x, y):
        """Check is row in complete for cleaning"""
        same = lambda index: self.canvas.item(x, y, index) == self.color[index]
        return not same(0) or not same(1) or not same(2)

    def clean_row(self):
        """Do row cleaning and set points"""
        num_rows = 0
        for i in range(self.width - 21, 20, -20):
            erase = True
            row = False
            while not row:
                for j in range(20, 379):
                    if not self._is_row_complete(j, i):
                        erase = False
                        row = True
                if erase:
                    num_rows += 1
                    self.erase_row(i)
        if num_rows:
            self.set_score(num_rows)

    def erase_row(self, i):
        """Clean row"""
        for l in range(i, 20, -1):
            for j in range(0, 380):
                for index in range(0, 3):
                    self.canvas.itemset((j, l, index), self.canvas.item(j, l - 20, index))

    def set_score(self, rows):
        """Set game score"""
        self.score += self.compute_points(rows, self.base_points)

    def get_score(self):
        """Get game score"""
        return self.score

    def draw(self):
        """Draw canvas on surface gameboard"""
        pygame.surfarray.blit_array(self.surface, self.canvas)

    def get_canvas(self):
        """Get canvas gameboard"""
        return self.canvas

    def get_color(self):
        """Get gameboard color"""
        return self.color
