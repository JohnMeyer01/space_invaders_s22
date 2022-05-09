"""
Fleet
"""
from datetime import datetime

from invader import Invader


class Fleet(object):

    def __init__(self, stdscr, window):
        self.stdscr = stdscr
        # This is actually the width of an invader
        self.width = 11
        self.window = window
        self.range = (0, self.window[1] - self.width - 1)
        self.invaders = [
            Invader(stdscr, window, (5, 2)),
            Invader(stdscr, window, (20, 2)),
            Invader(stdscr, window, (35, 2)),
            Invader(stdscr, window, (50, 2)),
        ]
        self.step = 5
        self.last_tick = datetime.now()
        self.move_threshold = 1
        self.number_of_invaders = len(self.invaders)
        self.remaining_invaders = self.number_of_invaders

    def tick(self, tick_number):
        [invader.tick(tick_number) for invader in self.invaders]

        if self.invaders[self.number_of_invaders - 1].x + self.width // 2 >= max(self.range):
            # This is the "brake" for things that should animate more slowly than the main game loop.
            if datetime.now().timestamp() - self.last_tick.timestamp() > self.move_threshold:
                self.stdscr.clear()
                for invader in self.invaders:
                    invader.direction = -1
                    invader.y += self.step
                    self.last_tick = datetime.now()
        elif self.invaders[0].x <= min(self.range):
            if datetime.now().timestamp() - self.last_tick.timestamp() > self.move_threshold:
                self.stdscr.clear()
                for invader in self.invaders:
                    invader.direction = 1
                    invader.y += self.step
                    self.last_tick = datetime.now()

    def y(self):
        return self.invaders[0].y + 8