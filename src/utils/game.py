import sys
import pygame as pg

from config import DISPLAY


class Game(object):
    running = True
    manager = None

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(DISPLAY)

    def update(self):
        self.manager.update()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        self.manager.handle_event()

    def flip(self):
        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.flip()
