# -*- coding: utf-8 -*-

from piece import Piece
from color import CYAN

class Zright(Piece):
    """Define Z right piece: (*) primary_shape | (¤) secondary_shape
       UP/DOWN    RIGHT/LEFT
         * *      ¤
       ¤ ¤        ¤ *
                    *
    """

    def __init__(self, surface, gameboard):
        super(Zright, self).__init__(surface, gameboard, color=CYAN)
        self.width = int(60)
        self.height = int(40)
        self.can_rotate = True

    def set_position(self, x, y):
        super(Zright, self).set_position(x, y)
        height = self.height
        width = self.width

        if self.orientation == "up" or self.orientation == "down":
            self.primary_shape.x = x + (width/3)
            self.primary_shape.y = y
            self.primary_shape.width = width - (width/3)
            self.primary_shape.height = height - (height/2)
            self.secondary_shape.x = x
            self.secondary_shape.y = y + (height/2)
            self.secondary_shape.width = width - (width/3)
            self.secondary_shape.height = height - (height/2)

        elif self.orientation == "right" or self.orientation == "left":
            self.primary_shape.x = x
            self.primary_shape.y = y
            self.primary_shape.width = width - (width/2)
            self.primary_shape.height = height - (height/3)
            self.secondary_shape.x = x + (width/2)
            self.secondary_shape.y = y + (height/3)
            self.secondary_shape.width = self.primary_shape.width
            self.secondary_shape.height = self.primary_shape.height
