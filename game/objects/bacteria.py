import pygame as pg
from .pixel import Pixel
from .dna import DNA
from random import random, choice


class Game:
    pass


class Bacteria(Pixel):
    def __init__(self, parent: DNA, game: Game, x: int, y: int):
        self.dna = DNA(parent)
        self.use_dna()
        super().__init__(x, y, self.width, self.height, groups=[game.rects])
    
    def use_dna(self):
        self.width = int(self.dna.size * 10) + 5
        self.height = int(self.dna.size * 10) + 5
    
    def _is_moving(self, chance: float = None):
        if chance is None:
            chance = random()
        if self.dna.speed >= chance:
            return True
        else:
            return False

    def _move_left(self):
        self.x -= self.width
    
    def _move_right(self):
        self.x += self.width
    
    def _move_up(self):
        self.y -= self.height
    
    def _move_down(self):
        self.y += self.height
    
    def _find_neighbours(self, rects: list):
        left_rect = pg.Rect(self.x - self.w, self.y, self.w, self.h)    #     __
        right_rect = pg.Rect(self.x + self.w, self.y, self.w, self.h)   #  __|__|__ 
        top_rect = pg.Rect(self.x, self.y - self.h, self.w, self.h)     # |__|__|__|
        bottom_rect = pg.Rect(self.x, self.y + self.h, self.w, self.h)  #    |__|
        neighbours = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        for rect in rects:
            if left_rect.colliderect(rect):
                neighbours['left'].append(rect)
            elif right_rect.colliderect(rect):
                neighbours['right'].append(rect)
            elif top_rect.colliderect(rect):
                neighbours['top'].append(rect)
            elif bottom_rect.colliderect(rect):
                neighbours['bottom'].append(rect)

        return neighbours
    
    def _where_to_go(self, neighbours: dict):
        directions = []
        if not neighbours['left']:
            directions.append(self._move_left)
        if not neighbours['right']:
            directions.append(self._move_right)
        if not neighbours['top']:
            directions.append(self._move_up)
        if not neighbours['bottom']:
            directions.append(self._move_down)
        
        return choice(directions)
            
    def move(self, rects: list):
        if self._is_moving():
            neighbours = self._find_neighbours(rects)
            go = self._where_to_go(neighbours)
            go()

    def update(self, game: Game, *args, **kwargs):
        # interact
        # breed
        # movement
        self.move(game.rects)
        return super().update(game.screen.screen, *args, **kwargs)
