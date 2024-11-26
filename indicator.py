from graphics import *
from globalVariables import *

class Indicator:
    def __init__(self, win, color, x1, y1, x2, y2, x3, y3):
        self.win = win
        self.indicatorButton = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
        self.indicatorButton.setFill(color)
        self.indicatorButton.setOutline(None)
        self.active = False

    def drawIndicator(self):
        self.indicatorButton.draw(self.win)
        self.active = True

    def undrawIndicator(self):
        self.indicatorButton.undraw()
        self.active = False


currentAnimalIndicatorD1 = Indicator(win, "#C29B6C", 260, 170, 290, 170, 275, 190)
currentAnimalIndicatorD2 = Indicator(win, "#C29B6C", 760, 170, 790, 170, 775, 190)
currentAnimalIndicatorD3 = Indicator(win, "#C29B6C", 620, 375, 650, 375, 635, 395)
currentAnimalIndicatorD4 = Indicator(win, "#C29B6C", 970, 375, 1000, 375, 985, 395)
currentAnimalIndicatorD5 = Indicator(win, "#C29B6C", 970, 535, 1000, 535, 985, 545)

currentAnimalIndicatorC1 = Indicator(win, "#CECECD", 350, 375, 380, 375, 365, 395)
currentAnimalIndicatorC2 = Indicator(win, "#CECECD", 970, 535, 1000, 535, 985, 545)
currentAnimalIndicatorC3 = Indicator(win, "#CECECD", 725, 535, 755, 535, 740, 545)
currentAnimalIndicatorC4 = Indicator(win, "#CECECD", 350, 170, 380, 170, 365, 190)
currentAnimalIndicatorC5 = Indicator(win, "#CECECD", 840, 170, 870, 170, 855, 190)

currentAnimalIndicatorL1 = Indicator(win, "#B38B9D", 350, 375, 380, 375, 365, 395)
currentAnimalIndicatorL2 = Indicator(win, "#B38B9D", 850, 535, 880, 535, 865, 545)
currentAnimalIndicatorL3 = Indicator(win, "#B38B9D", 480, 170, 510, 170, 495, 190)
currentAnimalIndicatorL4 = Indicator(win, "#B38B9D", 225, 170, 255, 170, 240, 190)
currentAnimalIndicatorL5 = Indicator(win, "#B38B9D", 850, 170, 880, 170, 865, 190)

currentAnimalIndicatorT1 = Indicator(win, "#ADD0B3", 270, 170, 300, 170, 285, 190)
currentAnimalIndicatorT2 = Indicator(win, "#ADD0B3", 600, 170, 630, 170, 615, 190)
currentAnimalIndicatorT3 = Indicator(win, "#ADD0B3", 940, 170, 970, 170, 955, 190)

currentAnimalIndicatorP1 = Indicator(win, "#FB928E", 265, 445, 295, 445, 280, 455)
currentAnimalIndicatorP2 = Indicator(win, "#FB928E", 940, 445, 970, 445, 955, 455)
currentAnimalIndicatorP3 = Indicator(win, "#FB928E", 600, 300, 630, 300, 615, 320)
currentAnimalIndicatorP4 = Indicator(win, "#FB928E", 265, 180, 295, 180, 280, 200)
currentAnimalIndicatorP5 = Indicator(win, "#FB928E", 940, 180, 970, 180, 955, 200)
