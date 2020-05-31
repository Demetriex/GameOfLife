import pygame as pg

from config import HEIGHT, WIDTH
from src.utils import State


class Simulator(State):
    def on_start(self):
        pass

    def update(self):
        self.draw()

    def draw(self):
        self.manager.game.screen.fill((128, 128, 128))
