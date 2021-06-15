# -*- coding: utf-8 -*-

from piece import Piece
from color import BLUE

class Line(Piece):
    """Define line piece: It has only one shape (¤)
       UP/DOWN    RIGHT/LEFT
       ¤          ¤ ¤ ¤ ¤
       ¤
       ¤
       ¤
    """

    def __init__(self, surface, gameboard):
        super(Line, self).__init__(surface, gameboard, color=BLUE)
        self.width = int(20)
        self.height = int(80)
        self.can_rotate = True
        self.primary_shape.set_dimension(self.width, self.height)
        self.secondary_shape.set_dimension(self.width, self.height)

    def get_shapes(self):
        """Get piece's shapes"""
        return [self.primary_shape]
