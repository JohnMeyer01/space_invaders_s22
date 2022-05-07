""" 
Houses Game class, which manages the behavior and data needed to run a spece invaders game 
"""

import curses #what is this for? 
import datetime as dt 
import sys #what is this for? 

from datetime import datetime
from fleet import Fleet
from player import Player


class Game(object): # do we need to inherit from object? 

    def __init__(self, stdscr):
        self.stdscr = stdscr # gets the new game window
        self._initialize_colors()
        self.last_tick = datetime.now()
        self.window = self.stdscr.getmaxyx() # gets hieght and width (y, x) of the stdscrn window 
        self.fleet = Fleet(stdscr, self.window)
        self.player = Player(stdscr, self.window)

    def run(self):
        while True:
            self.tick() # why do it this way? why not call self.update() here? 

    def tick(self):
        self.update()

    def update(self):
        new_tick = dt.timedelta(milliseconds=10)
        self.last_tick += new_tick
        self.fleet.tick(self.last_tick)
        self.player.tick(self.last_tick)
        self.detect_collisions()

        if self.is_over():
            if self.won():
                self.end('You won!')
            else:
                self.end('Oh no, you lost!')

    def detect_collisions(self):
        for laser in self.player.lasers:
            for invader in self.fleet.invaders:
                if self._collision_found(laser, invader):
                    invader.block_color += 1

                    if invader.block_color == 7:
                        self.fleet.remaining_invaders -= 1

                    if invader.block_color > 8:
                        invader.block_color = 8

    def won(self):
        """
        Returns true if there are no more invaders 
        """
        return self.fleet.remaining_invaders == 0

    def lost(self):
        """ 
        Returns true if the inading fleet has reached the same vertical position as the player 
        """
        return self.fleet.y() >= self.player.y

    def is_over(self):
        """ 
        checks to see whether the player has won or lost 
        """
        return self.won() or self.lost()

    def end(self, message):
        """ 
        writes a message to the screen and ends the game 
        """
        sys.stdout.write(message)
        sys.exit(0)

    def _collision_found(self, laser, invader):
        """ 
        checks to see if a laser beam is to the left, right, above, or below an invader (ie: does not colide), and otherwise returns true (ie: a hit).
        """
        # Left
        if laser.x + laser.width < invader.x:
            return False
        # Right
        elif invader.x + invader.width < laser.x:
            return False
        # Above
        elif laser.y + 1 < invader.y:
            return False
        # Below
        elif invader.y + 8 < laser.y:
            return False

        return True

    def _initialize_colors(self):
        """ 
        Each call to init_pair() creates an indexed pair of colors that represent a foregropund/background pair of colors. these can be referenced later by index. 
        """
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED,     curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLUE,    curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_GREEN,   curses.COLOR_GREEN)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
        curses.init_pair(5, curses.COLOR_CYAN,    curses.COLOR_CYAN)
        curses.init_pair(6, curses.COLOR_YELLOW,  curses.COLOR_YELLOW)
        curses.init_pair(7, curses.COLOR_WHITE,   curses.COLOR_WHITE)
        curses.init_pair(8, curses.COLOR_BLACK,   curses.COLOR_BLACK)
        curses.init_pair(10, 10, 10)