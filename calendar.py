from allAnimalsInfo import *
from graphics import *
from globalVariables import *
from button import *
from createText import *
from popUp import popUp

# Setting the Size of the calendar's dimensions
calendarWidth = 280
calendarHeight = 250
#size of each box
boxesSize = 70

class AdoptionCalendar:
    def __init__(self, win, numDaysInMonth, startWeekday, currentAnimal):
        self.win = win
        self.numDaysInMonth = numDaysInMonth
        self.startWeekday = startWeekday
        # X and Y positions of the calendar on the page
        self.xPosition = 730
        self.yPosition = 230
        self.currentA = currentAnimal
        self.confirmButton = Button(win, Point(1080, 620), 130, 40, "Confirm", getThemeColor())
        self.enterButton = Button(win, Point(900, 620), 130, 40, "Enter", getThemeColor())
        self.enterButton.activate()


        #stores each day's rectangle
        self.dayBoxes = {}
        #colors of each box
        self.dayColors = {}
        #reserved spots
        self.reservedDays = {}
        self.clickable = {}

        for i in range(numDaysInMonth):
            self.clickable[i + 1] = "clickable"

        #Calls the method to draw the calendar and the next button
        self.createCalendar()

    def createCalendar(self):
        numDaysInMonth = self.numDaysInMonth
        startWeekday = self.startWeekday

        # Draw the days of the week at the top
        dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        dayIndex = 0
        for eachDay in dayNames:
            #initial horizontal position + (current day box * size of each box) + half of the cell's width to put it in the center
            text = Text(Point(self.xPosition + (dayIndex * boxesSize) + (boxesSize / 2), 190), eachDay)
            text.setSize(20)
            text.setFace("times roman")
            #make into the theme color
            text.setTextColor(getThemeColor())
            text.draw(self.win)
            dayIndex += 1

        #first day of the month is 1
        dayNumber = 1
        #first row
        row = 0
        #starting column is the start weekday
        col = startWeekday

        #add the 1 to make sure it includes that last number
        for day in range(1, numDaysInMonth + 1):
            #based on the column position, it'll make the box start at the correct top left corner
            x1 = self.xPosition + col * boxesSize
            # based on the row position, it'll make the box start at the correct top left corner
            y1 = self.yPosition + row * boxesSize
            # add 1 to the col to essentially calculate the next boxes starting position so we know where the bottom
            # right corner of the rectangle should be
            x2 = self.xPosition + (col + 1) * boxesSize
            # same explanation with this code but for row instead of column
            y2 = self.yPosition + (row + 1) * boxesSize

            #create a rectangle for each day
            eachDayRectangle = Rectangle(Point(x1, y1), Point(x2, y2))
            eachDayRectangle.setOutline("black")
            eachDayRectangle.setWidth(1.25)
            eachDayRectangle.draw(self.win)
            self.takenSpots()

            specificReservedDays = list(self.reservedDays.keys())
            for i in specificReservedDays:
                if dayNumber == i:
                    eachDayRectangle.setFill(self.reservedDays[i])
                    self.clickable[dayNumber] = "not clickable"
                    break

            #write the day number in the center of the box
            eachDayRectangleText = Text(Point(x1 + (boxesSize / 2), y1 + (boxesSize / 2)), str(dayNumber))
            eachDayRectangleText.setSize(15)
            eachDayRectangleText.setTextColor("black")
            eachDayRectangleText.setFace("times roman")
            eachDayRectangleText.draw(self.win)

            #store the rectangle in the list
            self.dayBoxes[dayNumber] = eachDayRectangle

            # Update dayNumber and position (move to the next column)
            dayNumber += 1
            col += 1
            #move to next row when column hits 7
            if col == 7:
                col = 0
                row += 1

        #when user clicks
        #setMouseHandler is a method for when the user clicks

        setAdoptionPage(True)

        self.handleMouseClicks()

    def handleMouseClicks(self):
        while getAdoptionPage():
            p = self.win.getMouse()
            if self.isClickOnHeader(p):
                self.handleHeaderClick(p)
            elif self.isClickOnCalendar(p):
                self.dayBoxesClicked(p)
            elif self.isClickOnButton(p):
                self.handleCalendarButtonClick(p)

    def handleHeaderClick(self, p):
        from animalRentalScreens import (homeButton, homePage, adoptButton,
                                         adoptPage_Dogs, signupButton,
                                         signUpPageDesign)
        from testingClicks import clear
        if homeButton.buttonClicked(p):
            clear()
            setPage(0)
            setClickedOnAnimal(False)
            homePage()

        if adoptButton.buttonClicked(p):
            clear()
            setSubpage(2.1)
            setPage(2)
            setClickedOnAnimal(False)
            adoptPage_Dogs()

        if signupButton.buttonClicked(p):
            clear()
            setPage(3)
            setClickedOnAnimal(False)
            signUpPageDesign()

    def isClickOnHeader(self, p):
        headerTop = 0
        headerBottom = 75
        headerLeft = 0
        headerRight = winWidth

        return headerLeft <= p.getX() <= headerRight and headerTop <= p.getY() <= headerBottom

    def isClickOnCalendar(self, p):
        # Loop through all day boxes
        for day, rect in self.dayBoxes.items():
            if rect.getP1().getX() <= p.getX() <= rect.getP2().getX() and rect.getP1().getY() <= p.getY() <= rect.getP2().getY():
                return True
        return False

    def isClickOnButton(self, p):
        return self.enterButton.buttonClicked(p) or self.confirmButton.buttonClicked(p)

    def dayBoxesClicked(self, p):
        #check if user clicked inside any of the boxes
        #checks the day values of each boxes
        for day in self.dayBoxes:
            #get the corresponding rectangle from the current day
            rect = self.dayBoxes[day]
            if getUsername() == "":
                signInPlease = textMaker(win, (Point(winWidth/2,675)), "Please Sign In", 36, "#FF6961")
            else:
                if rect.getP1().getX() <= p.getX() <= rect.getP2().getX() and rect.getP1().getY() <= p.getY() <= rect.getP2().getY()\
                        and self.clickable[day] == "clickable":
                    #if the day is not in the dictionary of colored boxes, then add it
                    if day not in self.dayColors:
                        rect.setFill(getThemeColor())
                        #tracks it in the dictionary that that day is green
                        self.dayColors[day] = "selected"
                    else:
                        #resets color if clicked again and removes it from the colored boxes dictionary
                        rect.setFill("white")
                        del self.dayColors[day]
                    #prevents unnecessary checks for other days / quicker program time
                    break

    def handleCalendarButtonClick(self, p):
        if (p.getX() >= 835) and (p.getX() <= 965) and (p.getY() >= 599) and (p.getY() <= 641):
            self.adoptionLogic()
        elif (p.getX() >= 1015) and (p.getX() <= 1146) and (p.getY() >= 599) and (p.getY() <= 641):
            self.proceedWithAdoption()

    def adoptionLogic(self):
        if not hasattr(self, 'message'):
            self.message = Text(Point(1010, 690), "")
            self.message.setTextColor(getThemeColor())
            self.message.setFace("times roman")
            self.message.setSize(20)
            self.message.draw(win)
            good = False

        if len(self.dayColors) == 0:
            if getUsername() != "":
                self.message.setText("Please select dates.")
            good = False
        else:
            if self.consistencyCheck():
                suffixes = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                            '13th', '14th',
                            '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                            '26th', '27th',
                            '28th', '29th', '30th', '31st']
                self.message.setText("You have decided to adopt your animal from the "
                                     + (str(suffixes[min(list(self.dayColors))-1])) + " to the "
                                     + (str(suffixes[max(list(self.dayColors))-1])) + "." +
                                     "\n Please press 'Confirm' to lock in your decision.")
                setMinDay((str(suffixes[min(list(self.dayColors))-1])))
                setMaxDay((str(suffixes[max(list(self.dayColors))-1])))
                #to get the max number without the suffixes
                setMinNum(str(min(list(self.dayColors))-1))
                setMaxNum(str(max(list(self.dayColors))-1))
                if self.confirmButton.active == False:
                    self.confirmButton.activate()
                good = True

            else:
                self.message.setText("Please select consecutive dates and make"
                                     "\n sure you are adopting within the adoption period.")
                good = False
        return good

    def proceedWithAdoption(self):
        if self.adoptionLogic():
            self.popUpShow()
            self.message.setText("")
        else:
            self.message.setText("There's an error in your days. Check again")
            self.confirmButton.deactivate()

    def consistencyCheck(self):
        listOfSelectedDays = list(self.dayColors.keys())
        listOfSelectedDays.sort()
        isItInOrder = True
        for i in range(len(listOfSelectedDays)-1):
            currentNumber = listOfSelectedDays[i]
            if listOfSelectedDays[i+1] != currentNumber + 1:
                isItInOrder = False

        maxPeriod = ""
        reasonablePeriod = True
        if getSubpage() == 2.1:
            maxPeriod = listOfDogs[self.currentA].maxAdoptionPeriod()
        elif getSubpage() == 2.2:
            maxPeriod = listOfCats[self.currentA].maxAdoptionPeriod()
        elif getSubpage() == 2.3:
            maxPeriod = listOfLizards[self.currentA].maxAdoptionPeriod()
        elif getSubpage() == 2.4:
            maxPeriod = listOfTurtle[self.currentA].maxAdoptionPeriod()
        elif getSubpage() == 2.5:
            maxPeriod = listOfPigs[self.currentA].maxAdoptionPeriod()
        if len(self.dayColors) > int(maxPeriod) or len(self.dayColors) < 2:
            reasonablePeriod = False

        return isItInOrder & reasonablePeriod

    def takenSpots(self):
        fileRes = open("takenSpots.txt", "r")
        reservation = fileRes.readlines()
        for eachReservation in reservation:
            eachReservation = eachReservation.strip()
            eachReservation = eachReservation.split(",")
            usernameWhoTook = eachReservation[0]
            animalName = eachReservation[1]
            startReservation = int(eachReservation[2])
            endReservation = int(eachReservation[3])

            otherTakenColor = "#FF6961"
            yourTakenColor = "#F9DC5C"

            if getSubpage() == 2.1:
                if animalName == listOfDogs[getCurrentAnimal()].getName():
                    if usernameWhoTook == getUsername():
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = yourTakenColor
                    else:
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = otherTakenColor
            if getSubpage() == 2.2:
                if animalName == listOfCats[getCurrentAnimal()].getName():
                    if usernameWhoTook == getUsername():
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = yourTakenColor
                    else:
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = otherTakenColor
            if getSubpage() == 2.3:
                if animalName == listOfLizards[getCurrentAnimal()].getName():
                    if usernameWhoTook == getUsername():
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = yourTakenColor
                    else:
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = otherTakenColor
            if getSubpage() == 2.4:
                if animalName == listOfTurtle[getCurrentAnimal()].getName():
                    if usernameWhoTook == getUsername():
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = yourTakenColor
                    else:
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = otherTakenColor
            if getSubpage() == 2.5:
                if animalName == listOfPigs[getCurrentAnimal()].getName():
                    if usernameWhoTook == getUsername():
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = yourTakenColor
                    else:
                        for i in range(endReservation - startReservation + 1):
                            self.reservedDays[startReservation + i] = otherTakenColor

    def popUpShow(self):
        setAdoptionPage(False)
        from animalRentalScreens import choiceYes, choiceNo, buyMore
        buyMore.drawPopUp()
        choiceYes.activate()
        choiceNo.activate()