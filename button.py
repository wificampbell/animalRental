from graphics import  *

class Button:
    def __init__(self, win, center, width, height, label, color):
        #half width and half height to calculate the points to define the rectangle
        w = width/2
        h = height/2
        x = center.getX()
        y = center.getY()
        self.xMax = x+w
        self.xMin = x - w
        self.yMax = y + h
        self.yMin = y-h
        self.color = color
        #creating points that will helps define the rectangle
        p1 = Point(self.xMin, self.yMin)
        p2 = Point(self.xMax, self.yMax)

        self.rect = Rectangle(p1,p2)
        self.rect.setFill(self.color)
        self.rect.setOutline(self.color)
        self.label = Text(center, label)
        self.label.setSize(25)
        self.label.setFace("times roman")
        self.label.setTextColor("white")
        self.win = win
        self.active = False
        self.selected = False

    def deactivate(self):
        self.rect.undraw()
        self.label.undraw()
        self.active = False

    def activate(self):
        self.rect.draw(self.win)
        self.label.draw(self.win)
        self.active = True

    def buttonClicked(self, p):
        x1 = self.rect.getP1().getX()
        y1 = self.rect.getP1().getY()
        x2 = self.rect.getP2().getX()
        y2 = self.rect.getP2().getY()

        # Check if the mouse click (p) is within the rectangle bounds
        return x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2

    def setText(self, text):
        self.label.setText(text)

    def getText(self):
        return self.label.getText()

    def changeTextColor(self, newColor):
        self.label.setTextColor(newColor)

    def toggleSelected(self):
        self.selected = not self.selected

    def setSelected(self, newStatus):
        self.selected = newStatus

class entryInformation:
    def __init__(self, win, location, width, color, size, text):
        self.win = win
        self.entryBox = Entry(location, width)
        self.entryBox.setFill(color)
        self.entryBox.setFace("times roman")
        self.entryBox.setSize(size)
        self.entryBox.setText(text)

    def showEntry(self):
        self.entryBox.draw(self.win)

    def getText(self):
        return self.entryBox.getText()

    def setText(self, text):
        self.entryBox.setText(text)


