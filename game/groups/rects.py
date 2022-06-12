import os
import pygame as pg

class RectGroup:
    def __init__(self, limit = None):
        self._rects = []
        self.limit = limit
    
    def update(self, *args, **kwargs):
        for rect in self._rects:
            rect.update(*args, **kwargs)

    def add(self, rect: pg.Rect):
        if len(self._rects) < self.limit:
            if rect not in self._rects:
                self._rects.append(rect)

    def remove(self, rect: pg.Rect):
        if rect in self._rects:
            self._rects.remove(rect)
    
    def index(self, rect: pg.Rect):
        return self._rects.index(rect)

    def __getitem__(self, key: int):
        return self._rects[key]
    
    def group_by(self):
        result = {}
        for rect in self._rects:
            name = str(rect)
            if name not in result:
                result[name] = 1
            else:
                result[name] += 1
        return result

    def prezent_in_console(self, groups: dict):
        # clear console
        os.system('cls' if os.name=='nt' else 'clear')
        for name, number in groups.items():
            print(name, number * '#')
