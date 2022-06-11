import pygame as pg


class Pixel(pg.Rect):
    def __init__(self, *args, **kwargs):
        pg.Rect.__init__(self, *args, **kwargs)
        self.color = 0xff0000
    
    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self.color, self)

    
    def update(self, surface: pg.Surface, *args, **kwargs):
        self.draw(surface)
