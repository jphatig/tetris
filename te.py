# -*- coding: utf-8 -*-

from piece import Piece
from color import PURPLE

class Te(Piece):
    """Define L left piece: (*) primary_shape | (¤) secondary_shape
       UP       RIGHT  DOWN    LEFT
         *      ¤      ¤ ¤ ¤     ¤
       ¤ ¤ ¤    ¤ *      *     * ¤
                ¤                ¤
    """

    def __init__(self, surface, gameboard):
        super(Te, self).__init__(surface, gameboard, color=PURPLE)
        self.width = int(60)
        self.height = int(40)
        self.can_rotate = True

    def set_position(self, x, y):
        super(Te, self).set_position(x, y)
        height = self.height
        width = self.width

        if self.orientation == "up":
            self.primary_shape.x = x + (width / 3)
            self.primary_shape.y = y
            self.primary_shape.width = width / 3
            self.primary_shape.height = height / 2
            self.secondary_shape.x = x
            self.secondary_shape.y = y + (height / 2)
            self.secondary_shape.width = width
            self.secondary_shape.height = height / 2

        elif self.orientation == "right":
            self.primary_shape.x = x + (width / 2)
            self.primary_shape.y = y + (height / 3)
            self.primary_shape.width = width / 2
            self.primary_shape.height = height / 3
            self.secondary_shape.x = x
            self.secondary_shape.y = y
            self.secondary_shape.width = width / 2
            self.secondary_shape.height = height

        elif self.orientation == "down":
            self.primary_shape.x = x + (width / 3)
            self.primary_shape.y = y + (height / 2)
            self.primary_shape.width = width / 3
            self.primary_shape.height = height / 2
            self.secondary_shape.x = x
            self.secondary_shape.y = y
            self.secondary_shape.width = width
            self.secondary_shape.height = height / 2

        elif self.orientation == "left":
            self.primary_shape.x = x
            self.primary_shape.y = y + (height / 3)
            self.primary_shape.width = width / 2
            self.primary_shape.height = height / 3
            self.secondary_shape.x = x + (width / 2)
            self.secondary_shape.y = y
            self.secondary_shape.width = width / 2
            self.secondary_shape.height = height
