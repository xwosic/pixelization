from random import random


class fraction(float):
    """
    Fraction accepts real values from 0.0 to 1.0
    """
    def __new__(cls, value):
        if value > 1.0:
            value = 1.0
        elif value < 0.0:
            value = 0.0
        return float.__new__(cls, float(value))
    
    @classmethod
    def random(cls):
        """
        Returns random fraction.
        """
        return cls(random())
