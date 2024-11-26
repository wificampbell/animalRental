from graphics import *
from animalRentalScreens import themeColor

class Pages:
    def __init__(self, win, image1, image2, image3, image4, image5, themeColor, h, text):
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.image5 = image5
        self.adoptHeadingText = Text(h, text)

        self.image1.setFill(themeColor)
        self.image2.setFill(themeColor)
        self.image3.setFill(themeColor)
        self.image4.setFill(themeColor)
        self.image5.setFill(themeColor)

        self.image1.setOutline(None)
        self.image2.setOutline(None)
        self.image3.setOutline(None)
        self.image4.setOutline(None)
        self.image5.setOutline(None)

        self.adoptHeadingText.setTextColor(themeColor)
        self.adoptHeadingText.setSize(36)
        self.adoptHeadingText.setFace("times roman")

        self.image1.draw(win)
        self.image2.draw(win)
        self.image3.draw(win)
        self.image4.draw(win)
        self.image5.draw(win)
        self.adoptHeadingText.draw(win)

    def image1Clicked(self, p):
        x1 = self.image1.getP1().getX()
        y1 = self.image1.getP1().getY()
        x2 = self.image1.getP2().getX()
        y2 = self.image1.getP2().getY()

        # Check if the mouse click (p) is within the rectangle bounds
        return x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2