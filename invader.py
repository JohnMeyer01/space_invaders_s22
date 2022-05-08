"""
Implements the invader class (an individual enemy ship) 
"""

import curses
from datetime import datetime


class Invader:

    def __init__(self, stdscr, window, position):
        """Creates a new invader and defines its properties"""
        self.stdscr = stdscr
        self.window = window
        self.width = 11
        self.speed = 5
        self.direction = 1
        self.range = (0, self.window[1] - self.width - 1)
        self.x = position[0]
        self.y = position[1]
        self.block_color = 1
        self.empty_color = 8
        self.block_width = 1
        self.last_tick = datetime.now()
        self.move_threshold = 0.5 # in seconds? (units of time)


    def __repr__(self):
        return [
            [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' '],
            [' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', ' '],
            [' ', 'O', 'O', ' ', 'O', 'O', 'O', ' ', 'O', 'O', ' '],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', ' ', 'O', 'O', 'O', 'O', 'O', 'O', 'O', ' ', 'O'],
            ['O', ' ', 'O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
            [' ', ' ', ' ', 'O', 'O', ' ', 'O', 'O', ' ', ' ', ' ']
        ]

    def draw(self):
        for y, row in enumerate(self.__repr__()):
            for x, char in enumerate(row):
                if char == ' ':
                    self._draw_block(x, y, self.empty_color)
                else:
                    self._draw_block(x, y, self.block_color)

    def _draw_block(self, x, y, color):
        self.stdscr.addstr(
            self.y + y,
            self.x + x,
            ' ' * self.block_width,
            curses.color_pair(color)
        )

    def _move(self):
    # def _move(self, tick_number):
        # This is a kind of "brake" to ensure that the invaders don't move for every single game tick
        # (since we want to animate the player's motion quickly, but the invaders should move more slowly).
        if datetime.now().timestamp() - self.last_tick.timestamp() > self.move_threshold:
            x = self.x + 1
            x = min(x, max(self.range))
            x = max(x, min(self.range))
            x = x - self.x
            self.x += x * self.speed * self.direction
            self.last_tick = datetime.now()

    def update(self):
        self._move()
        self.draw()

    def tick(self):
        self.update()

    #def update(self, tick_number):
    #    self._move(tick_number)
    #    self.draw()

    #def tick(self, tick_number):
    #    self.update(tick_number)


    