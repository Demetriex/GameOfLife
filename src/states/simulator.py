import pygame as pg

from config import HEIGHT, WIDTH
from src.utils import State
from src.entities import Board


class Simulator(State):
    def on_start(self):
        self.board = Board()
        self.board.generate_blocks()

    def update(self):
        self.draw()

    def draw(self):
        screen = self.manager.game.screen
        screen.fill((128, 128, 128))
        self.board.draw(screen)
