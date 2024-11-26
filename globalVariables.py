from graphics import *
# width and height of screen
winWidth = 1300
winHeight = 750

# this is the p = win.getMouse()
p = Point(0,0)

# top headings clicked
page = 0
subpage = 0

win = GraphWin("Animal Rental",winWidth, winHeight)

def setPage(newPage):
    global page
    page = newPage

def setSubpage(newSubPage):
    global subpage
    subpage = newSubPage

def getPage():
    return page

def getSubpage():
    return subpage

themeColor = ""

def getThemeColor():
    return themeColor

def setThemeColor(newColor):
    global themeColor
    themeColor = newColor

claimedSpots = []

currentAnimal = 0

def setCurrentAnimal(newCurrentAnimal):
    global currentAnimal
    currentAnimal = newCurrentAnimal

def getCurrentAnimal():
    return currentAnimal

clickedOnAnimal = False

def setClickedOnAnimal(newAnimal):
    global clickedOnAnimal
    clickedOnAnimal = newAnimal

def getClickedOnAnimal():
    return clickedOnAnimal

adoptionPage = False

def getAdoptionPage():
    return adoptionPage

def setAdoptionPage(newPage):
    global adoptionPage
    adoptionPage = newPage

#checking to see if user still needs to sign in/sign up
username = ""

def getUsername():
    return username

def setUsername(newUser):
    global username
    username = newUser

stopSearch = False

def getStopSearch():
    return stopSearch

def setStopSearch(newStopSearch):
    global stopSearch
    stopSearch = newStopSearch


#for when the accessories buttons are clicked

selected = False

def getSelectedStatus():
    return selected

def setSelectedStatus(newStatus):
    global selected
    selected = newStatus

#to store wanted accessories

wantedAccessories = []

maxDay = ""

def getMaxDay():
    return maxDay

def setMaxDay(newMax):
    global maxDay
    maxDay = newMax

minDay = ""

def getMinDay():
    return minDay

def setMinDay(newMin):
    global minDay
    minDay = newMin

maxNum = ""

def getMaxNum():
    return str(int(maxNum)+1)

def setMaxNum(newMax):
    global maxNum
    maxNum = newMax

minNum = ""

def getMinNum():
    return str(int(minNum)+1)

def setMinNum(newMin):
    global minNum
    minNum = newMin


totalPrice = 0

def getTotalPrice():
    return totalPrice

def changeTotalPrice(newChange):
    global totalPrice
    totalPrice += newChange

def setTotalPrice(newPrice):
    global totalPrice
    totalPrice = newPrice
