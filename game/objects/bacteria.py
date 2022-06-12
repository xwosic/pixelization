import pygame as pg
from .pixel import Pixel
from .dna import DNA
from random import random, choice
from datetime import datetime, timedelta


class Game:
    pass


class Bacteria(Pixel):
    def __init__(self, parent: DNA, game: Game, x: int, y: int):
        self.dna = DNA(parent)
        self.game = game
        self.use_dna()
        super().__init__(x, y, self.width, self.height, groups=[game.rects])
        self._moves = {
            'left': self._move_left,
            'right': self._move_right,
            'top': self._move_up,
            'bottom': self._move_down
        }
        self._last_breed = datetime.now()
        self._birth_time = datetime.now()
        self._neighbours = {}
        self._child_num = 0
    
    def use_dna(self):
        size_constant = 5
        self.width = int(self.dna.size * 10) + size_constant
        self.height = int(self.dna.size * 10) + size_constant
        self.color = self.dna.color
        self.breed_period = timedelta(seconds=1 + self.dna.breed_period * 10)
        self.max_num_of_children = int(self.dna.max_num_of_children * 10)
        self.lifetime = timedelta(seconds=self.dna.lifetime * 60)
        
    def _is_moving(self):
        return self.dna.speed >= random()

    def _move_left(self):
        self.x -= self.width
    
    def _move_right(self):
        self.x += self.width
    
    def _move_up(self):
        self.y -= self.height
    
    def _move_down(self):
        self.y += self.height
    
    def _find_neighbours(self, rects: list):
        self._neighbours = {
            'left': [],
            'right': [],
            'top': [],
            'bottom': []
        }
        left_rect = pg.Rect(self.x - self.w, self.y, self.w, self.h)    #     __
        right_rect = pg.Rect(self.x + self.w, self.y, self.w, self.h)   #  __|__|__ 
        top_rect = pg.Rect(self.x, self.y - self.h, self.w, self.h)     # |__|__|__|
        bottom_rect = pg.Rect(self.x, self.y + self.h, self.w, self.h)  #    |__|
        for rect in rects:
            if left_rect.colliderect(rect):
                self._neighbours['left'].append(rect)
            elif right_rect.colliderect(rect):
                self._neighbours['right'].append(rect)
            elif top_rect.colliderect(rect):
                self._neighbours['top'].append(rect)
            elif bottom_rect.colliderect(rect):
                self._neighbours['bottom'].append(rect)
    
    def _choose_empty_direction(self):
        choises = []
        if not self._neighbours['left']:
            choises.append('left')
        if not self._neighbours['right']:
            choises.append('right')
        if not self._neighbours['top']:
            choises.append('top')
        if not self._neighbours['bottom']:
            choises.append('bottom')
        if choises:
            return choice(choises)

    def _choose_occupied_direction(self):
        choises = []
        if self._neighbours['left']:
            choises.append('left')
        if self._neighbours['right']:
            choises.append('right')
        if self._neighbours['top']:
            choises.append('top')
        if self._neighbours['bottom']:
            choises.append('bottom')
        if choises:
            return choice(choises)
    
    def _where_to_go(self, direction: str):  
        return self._moves[direction]
    
    def _breed_in_direction(self, direction: str):
        x = self.x
        y = self.y
        child = Bacteria(self.dna, self.game, x, y)
        if direction == 'left':
            child.x -= child.w
        elif direction == 'right':
            child.x += self.w
        elif direction == 'top':
            child.y -= child.h
        elif direction == 'bottom':
            child.y += self.h
        self._last_breed = datetime.now()
        self._neighbours[direction].append(child)
        self._child_num += 1
            
    def move(self, direction):
        if direction:
            if self._is_moving():
                go = self._where_to_go(direction)
                if go:
                    go()
    
    def _which_child(self):
        return self._child_num < self.max_num_of_children
    
    def _breed_period(self):
        return self.breed_period < datetime.now() - self._last_breed
    
    def breed(self, direction):
        if direction:
            if self._which_child():
                if self._breed_period():
                    self._breed_in_direction(direction)  
    
    def _time_to_die(self):
        return self.lifetime < datetime.now() - self._birth_time
    
    def dies(self):
        if self._time_to_die():
            self.kill()

    def update(self, game: Game, *args, **kwargs):
        self._find_neighbours(game.rects)
        empty_direction = self._choose_empty_direction()
        # interact (hunt, share)
        if empty_direction is not None:
            self.breed(empty_direction)
            empty_direction = self._choose_empty_direction()
            self.move(empty_direction)
        self.dies()
        return super().update(game.screen.screen, *args, **kwargs)
    
    def __str__(self):
        return self.dna.color
