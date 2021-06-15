# -*- coding: utf-8 -*-

import sys
import pygame
import random

from pygame.locals import *
from gameboard import GameBoard
from collision import Collision
from square import Square
from line import Line
from te import Te
from zleft import Zleft
from zright import Zright
from elleft import Elleft
from elright import Elright

DEFAULT_FONT = 'src/fonts/8bit.TTF'

WIDTH = 600
HEIGHT = 600

FPS_BASE = 10

X_INIT = 180
Y_INIT = -80
X_NEXT = 460
Y_NEXT = 80

class Game:
    """Define methos for tetris game"""

    # Configuration

    def __init__(self):
        self.define_pieces()
        self.pygame_init()
        self.configure()

    def define_pieces(self):
        """Define pieces available for tetris game"""
        # self.pieces = [Square, Line, Te, Zleft, Zright, Elleft, Elright]
        self.pieces = [Te]

    def pygame_init(self):
        """Init pygame resources"""
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("TETRIS")

    def configure(self):
        """Do game initial configuration"""
        self.set_surface()
        self.set_gameboard()
        self.set_gameover_label()
        self.set_score_title()
        self.set_score_label()
        self.draw_score_title()
        self.draw_score_label()

    def set_gameboard(self):
        """Set gameboard"""
        self.gameboard = GameBoard(WIDTH, HEIGHT, self.surface)

    def set_gameover_label(self):
        """Set Gameover label"""
        font = pygame.font.Font(DEFAULT_FONT, 50)
        self.gameover_label = font.render('GAME OVER', 0, (255, 0, 0))

    def set_score_title(self):
        """Set score title"""
        font = pygame.font.Font(DEFAULT_FONT, 20)
        self.score_title = font.render('SCORE', 0, (255, 255, 255))

    def set_score_label(self):
        """Set score label"""
        font = pygame.font.Font(DEFAULT_FONT, 20)
        score = str(self.get_score())
        self.score_label = font.render(score, 0, (255, 255, 255))

    def set_surface(self):
        """Set surface for screen game"""
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    # Draws

    def draw_score_title(self):
        """Draw score title"""
        self.surface.blit(self.score_title, (440, 260))

    def draw_score_label(self):
        """Draw score label"""
        self.surface.blit(self.score_label, (450, 300))

    def draw_gameover_label(self):
        """Draw gameover label"""
        self.surface.blit(self.gameover_label, (55, 200))

    # Helpful methods

    def get_score(self):
        """Get score points"""
        return self.gameboard.get_score()

    def random_piece(self):
        """Return a random teris piece"""
        index = random.randrange(len(self.pieces))
        piece = self.pieces[index]
        return piece(self.surface, self.gameboard)

    def check_collision(self, direction):
        """Check piece collision on movement"""
        canvas = self.gameboard.get_canvas()
        color = self.gameboard.get_color()
        step = True
        for shape in self.piece.get_shapes():
            collision = Collision(canvas, shape.rect)
            if not step:
                continue
            if direction == 'left':
                collision.to_left()
            if direction == 'right':
                collision.to_right()
            if direction == 'down':
                collision.to_down()
            sides = collision.get_sides()
            if sides.count(color) != len(sides):
                step = False
        return step

    def play_theme(self):
        """Start tetris music theme"""
        pygame.mixer.music.load('src/sound/tetrisA.ogg')
        pygame.mixer.music.play(-1)

    def play_gameover(self):
        """Start gameover music theme"""
        pygame.mixer.music.load("src/sound/gameover.ogg")
        pygame.mixer.music.play(-1)

    def gameover(self):
        """Show gameover screen"""
        self.draw_gameover_label()
        self.play_gameover()
        self.refresh()
        self.gameover_quit()

    def gameover_quit(self):
        """Wait for gameover quit"""
        while True:
            for event in pygame.event.get():
                self.key_press_quit(event)
            self.refresh()
            self.fps_clock.tick(self.fps)

    # Game actions

    def restart_position(self):
        """Restart coords to original position"""
        self.x = X_INIT
        self.y = -10

    def start(self):
        """Start game"""
        self.fps = FPS_BASE
        self.falling = True
        self.play_theme()
        self.fps_clock = pygame.time.Clock()
        self.piece = self.random_piece()
        self.generate_next_piece()
        self.restart_position()
        while True:
            self.gameboard.draw()
            self.piece.set_position(self.x, self.y)
            self.piece.draw()
            self.next_piece.draw()
            self.draw_score_title()
            self.draw_score_label()
            self.key_pressed()
            if not self.continue_falling():
                break
            self.key_press()
            self.refresh()
            self.fps_clock.tick(self.fps)

    def refresh(self):
        """Refresh screen"""
        pygame.display.flip()

    def generate_next_piece(self):
        """Generate next piece on waiting"""
        self.next_piece = self.random_piece()
        self.next_piece.set_position(X_NEXT, Y_NEXT)
        self.next_piece.draw()

    def key_pressed(self):
        """Do action on key pressed"""
        key_pressed = pygame.key.get_pressed()
        self.key_pressed_left(key_pressed)
        self.key_pressed_right(key_pressed)
        self.key_pressed_down(key_pressed)

    def key_pressed_left(self, key_pressed):
        """Move piece to left key pressed"""
        if key_pressed[K_LEFT]:
            if self.x != 0 and self.check_collision('left'):
                self.x -= 20

    def key_pressed_right(self, key_pressed):
        """Move piece to right key pressed"""
        if key_pressed[K_RIGHT]:
            collision = self.check_collision('right')
            if self.x + self.piece.width != self.gameboard.width and collision:
                self.x += 20

    def key_pressed_down(self, key_pressed):
        """Down action on key pressed"""
        if key_pressed[K_DOWN]:
            self.fps = 120

    def continue_falling(self):
        """Check piece cointinuos falling"""
        if self.falling:
            collision = self.check_collision('down')
            if self.y > (self.gameboard.height - self.piece.height - 1) or not collision:
                self.falling == False
                if self.y <= 0:
                    self.gameover()
                    return
                self.piece.save()
                self.piece = self.next_piece
                self.generate_next_piece()
                self.gameboard.clean_row()
                self.set_score_label()
                self.restart_position()
            else:
                self.y += 5
        return True

    def key_press(self):
        """Do action on key press"""
        for event in pygame.event.get():
            self.key_press_rotate(event)
            self.key_press_fps(event)
            self.key_press_quit(event)

    def key_press_rotate(self, event):
        """Rotate piece on up key press"""
        if event.type == KEYDOWN and event.key == K_UP:
            left = self.check_collision('left')
            right = self.check_collision('right')
            down = self.check_collision('down')
            if left and right and down:
                self.piece.rotate() # Rotate doesn't work on side collision

    def key_press_fps(self, event):
        """Restart fps on up key down press"""
        if event.type == KEYUP and event.key == K_DOWN:
            self.fps = FPS_BASE

    def key_press_quit(self, event):
        """Quit game on escape key press"""
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
