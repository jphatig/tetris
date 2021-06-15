# -*- coding: utf-8 -*-

from shape import Shape
from color import WHITE

class Piece:
    """Define piece for tetris game"""

    def __init__(self, surface, gameboard, color=WHITE):
        """Define default piece parameters"""
        self.can_rotate = False
        self.orientation = 'up'
        self.orientation_changes = {
            'up': 'right',
            'right': 'down',
            'down': 'left',
            'left': 'up',
        }
        self.primary_shape = Shape(surface, gameboard, color)
        self.secondary_shape = Shape(surface, gameboard, color)
        self.width = 10
        self.height = 10
        self.x = 0
        self.y = 0

    def set_position(self, x, y):
        """Set x and y position on screen"""
        self.x = x
        self.y = y
        self.primary_shape.set_coords(x, y)
        self.secondary_shape.set_coords(x, y)

    def draw(self):
        """Draw piece on screen"""
        self.primary_shape.draw()
        self.secondary_shape.draw()

    def change_dimension(self):
        """Swap dimension for piece and shapes"""
        if self.can_rotate:
            self.swap_dimension()
            self.primary_shape.swap_dimension()
            self.secondary_shape.swap_dimension()

    def swap_dimension(self):
        """Swap width and height"""
        width = self.width
        height = self.height
        self.width = height
        self.height = width

    def change_orientation(self):
        """Change piece orientarion"""
        self.orientation = self.orientation_changes.get(self.orientation)

    def rotate(self):
        """Rotate piece"""
        self.change_dimension()
        self.change_orientation()

    def get_shapes(self):
        """Return piece's shapes"""
        return [self.primary_shape, self.secondary_shape]

    def save(self):
        """Save piece shapes on screen canvas"""
        self.primary_shape.save()
        self.secondary_shape.save()
