import pygame as pg


class Block(pg.sprite.Sprite):
    def __init__(self, color, width, height, coordinates, margine=2):
        super().__init__()

        self.image = pg.Surface([width - margine, height - margine])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinates
