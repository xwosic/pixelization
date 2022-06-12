import pygame as pg
from typing import List, Optional
from game.groups.rects import RectGroup

class Pixel(pg.Rect):
    def __init__(self, *args, groups: Optional[List[RectGroup]], **kwargs):
        pg.Rect.__init__(self, *args, **kwargs)
        self.groups = groups
        self.add_to_groups(self.groups)
    
    def add_to_groups(self, groups: Optional[List[RectGroup]]):
        if groups:
            for group in groups:
                group.add(self)
    
    def remove_from_groups(self):
        if self.groups:
            for group in self.groups:
                group.remove(self)
    
    def kill(self):
        self.remove_from_groups()
    
    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self.color, self)

    def update(self, surface: pg.Surface, *args, **kwargs):
        self.draw(surface)
