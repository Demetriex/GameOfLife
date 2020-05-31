import pygame as pg

from config import DISPLAY
from .block import Block


class Board(pg.sprite.Group):
    def __init__(self, cells=10, color=(255, 255, 255)):
        super().__init__()
        self.cells = cells
        self.cell_size = min(DISPLAY) / self.cells
        self.color = color
        self._blocks = []

    def generate_blocks(self):
        for x in range(self.cells):
            for y in range(self.cells):
                b = Block(
                    self.color,
                    self.cell_size,
                    self.cell_size,
                    coordinates=(self.cell_size * x, self.cell_size * y),
                )
                self.add(b)

    @property
    def blocks(self):
        return self._blocks
