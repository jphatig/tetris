# -*- coding: utf-8 -*-

DEFAULT_COLOR = (0, 0, 0)

class Collision:
    """Check piece's collision based on moves"""

    def __init__(self, canvas, rect):
        self.canvas = canvas
        self.rect = rect
        self.top = DEFAULT_COLOR
        self.left = DEFAULT_COLOR
        self.right = DEFAULT_COLOR
        self.down = DEFAULT_COLOR

    def to_left(self):
        """Check collision on left move"""
        self._to_horizontal(x=self.rect.left - 1)

    def to_right(self):
        """Check collision on right move"""
        self._to_horizontal(x=self.rect.right + 1)

    def _to_horizontal(self, x):
        """Check collision on horizontal move"""
        self.top = self._compute_side(x, self.rect.top + 5)
        self.left = self._compute_side(x, self.rect.centery - 2)
        self.right = self._compute_side(x, self.rect.centery + 2)
        self.bottom = self._compute_side(x, self.rect.bottom)

    def to_down(self):
        """Check collision on down move"""
        self._to_vertical(y=self.rect.bottom + 1)

    def _to_vertical(self, y):
        """Check collision on vertical move"""
        self.top = self._compute_side(self.rect.left, y)
        self.left = self._compute_side(self.rect.centerx - 2, y)
        self.right = self._compute_side(self.rect.centerx + 2, y)
        self.bottom = self._compute_side(self.rect.right - 1, y)

    def _compute_side(self, x, y):
        """Return RGB in canvas based on x, y coords"""
        return tuple(map(lambda index: self.canvas.item(x, y, index), [0, 1, 2]))

    def get_sides(self):
        """Return a list with all collision types"""
        return [self.top, self.left, self.right, self.bottom]
