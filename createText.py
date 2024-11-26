from graphics import *

##---------Create Text------##
class textMaker:
    def __init__(self, win, location, text, size, color):
        self.text = Text(location, text)
        self.text.setSize(size)
        self.text.setTextColor(color)
        self.text.setFace("times roman")
        self.text.draw(win)
        self.win = win
        self.active = False

    def drawText(self):
        self.text.draw(self.win)
        self.active = True

    def undrawText(self):
        self.text.undraw()
        self.active = False

    def setText(self, text):
        self.text.setText(text)