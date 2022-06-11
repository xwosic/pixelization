from turtle import width
import pygame as pg
from .pixel import Pixel
from .dna import DNA


class Game:
    pass


class Bacteria(Pixel):
    def __init__(self, parent: DNA, game: Game, x: int, y: int):
        self.dna = DNA(parent)
        super().__init__(x, y, 10, 10, groups=[game.rects])
