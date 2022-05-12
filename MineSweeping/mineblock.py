import random
from enum import Enum
from tkinter import Y

BLOCK_WIDTH = 30
BLOCK_HEIGHT = 16
SIZE = 90
MINE_COUNT = 99

class BlockStatus(Enum):
    normal = 1
    opened = 2
    mine = 3
    flag = 4
    ask = 5
    bomb = 6
    hint = 7
    double = 8


class Mine:
    def __init__(self, x, y, value=0) -> None:
        self._x = x
        self._y = y
        self._value = 0
        self._around_mine_count = -1
        sefl._status = BlockStatus.normal
        self.set_value(value)

    def __repr__(self) -> str:
        return str(self._value)

    def get_x(self):
        return sefl._x

    def set_x(self, x):
        self._x = x

    def set_y(self , y):
        self._y = y

    def get_y(sefl):
        return sefl._y

    y = property(fget=get_y, fset=set_y)

    