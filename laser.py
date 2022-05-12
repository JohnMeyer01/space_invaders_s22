"""
Laser
"""
import curses


class Laser:

    def __init__(self, stdscr, x, y):
        self.stdscr = stdscr
        self.x = x
        self.y = y
        self.color = 7
        self.width = 1

    def tick(self, tick_number):
        if (self.y <= 0):
            self.color = 8
        else:
            self.y -= 1

        self.draw()

    def draw(self):
        self.stdscr.addstr(
            self.y,
            self.x,
            ' ' * self.width,
            curses.color_pair(self.color)
        )