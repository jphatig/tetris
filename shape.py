# -*- coding: utf-8 -*-

import pygame

class Shape:
    """Define shapes for build pieces"""

    def __init__(self, surface, gameboard, color):
        """Define shape default params"""
        pygame.init()
        self.height = 0
        self.width = 0
        self.x = 0
        self.y = 0
        self.surface = surface
        self.gameboard = gameboard
        self.color = color

    def set_coords(self, x, y):
        """Set x and y position"""
        self.x = x
        self.y = y

    def set_dimension(self, width, height):
        """Set width and height"""
        self.width = width
        self.height = height

    def set_measure(self, x, y, width, height):
        """Set all Wmeasure for shape"""
        self.set_coords(x, y)
        self.set_dimension(width, height)

    def swap_dimension(self):
        """Swap height and width"""
        width = self.width
        height = self.height
        self.width = height
        self.height = width

    def draw(self):
        """Draw shape on screen"""
        measure = (self.x, self.y, self.width, self.height)
        self.rect = pygame.draw.rect(self.surface, self.color, measure)

    def save(self):
        """Save shape on screen canvas"""
        self.gameboard.draw_shape(self.x, self.y, self.width, self.height, self.color)
