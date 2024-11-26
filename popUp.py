from button import Button
from graphics import *

class popUp:
    def __init__(self, win,x1,y1,x2,y2, text):
        self.win = win
        self.box = Rectangle(Point(x1,y1),Point(x2,y2))
        self.box.setFill("#B16E4B")
        self.box.setOutline(None)
        self.heading = Text(Point((x2+x1)/2,360), text)
        self.heading.setFace("times roman")
        self.heading.setSize(30)
        self.heading.setTextColor("white")
        self.active = False

    def drawPopUp(self):
        self.box.draw(self.win)
        self.heading.draw(self.win)
        self.active = True

    def erasePopUp(self):
        self.box.undraw()
        self.heading.undraw()
        self.active = False
