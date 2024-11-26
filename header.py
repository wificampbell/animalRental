from graphics import *
from globalVariables import *
from button import *

class Header:
    def __init__(self, x1, y1, x2, y2):
        self.header = Rectangle(Point(x1, y1), Point(x2, y2))
        self.header.setFill("#B16E4B")
        self.header.setOutline("#B16E4B")
        self.header.draw(win)