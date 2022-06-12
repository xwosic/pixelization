import pygame as pg


class RectGroup:
    def __init__(self):
        self._rects = []
    
    def update(self, *args, **kwargs):
        for rect in self._rects:
            rect.update(*args, **kwargs)

    def add(self, rect: pg.Rect):
        if rect not in self._rects:
            self._rects.append(rect)

    def remove(self, rect: pg.Rect):
        if rect in self._rects:
            self._rects.remove(rect)
    
    def index(self, rect: pg.Rect):
        return self._rects.index(rect)

    def __getitem__(self, key: int):
        return self._rects[key]
