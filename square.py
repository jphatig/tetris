# -*- coding: utf-8 -*-

from piece import Piece
from color import ORANGE

class Square(Piece):
    """Define square piece: It has only one shape
       UP/DOWN/RIGHT/LEFT
       ¤ ¤
       ¤ ¤
    """

    def __init__(self, surface, gameboard):
        super(Square, self).__init__(surface, gameboard, color=ORANGE)
        self.width = int(40)
        self.height = int(40)
        self.primary_shape.set_dimension(self.width, self.height)
        self.secondary_shape.set_dimension(self.width, self.height)

    def get_shapes(self):
        return [self.primary_shape]
