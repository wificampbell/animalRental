from graphics import *
from globalVariables import *
from testingClicks import *


##FOR MEETING 2 - making animal class
class Animal:
    def __init__(self, type=None, name=None, age=None, birthday=None):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.type = type
        self.maxAdopt = 0
        self.maxAdoptionDict = {
            "Dog": "5",
            "Cat": "5",
            "Lizard": "3",
            "Turtle": "3",
            "Pig": "4"
        }
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getBirthday(self):
        return self.birthday
    def getType(self):
        return self.type
    def displayInfo(self, x1, y1, color, size):
        infoDisplayed = Text(Point(x1, y1), self.getType() + " Name: " + self.getName()+ "\nAge: " + self.getAge() + "\n Birthday: " + self.getBirthday())
        infoDisplayed.setSize(size)
        infoDisplayed.setFill(color)
        infoDisplayed.setFace("times roman")
        infoDisplayed.draw(win)

    def maxAdoptionPeriod(self):
        return self.maxAdoptionDict.get(self.type,0)



##MMETING 2

#dogs
dogOne = Animal("Dog", "Scout", "7 months", "10/3")
dogTwo = Animal("Dog", "Max", "2 years", "5/2")
dogThree = Animal("Dog", "Baxter", "5 years", "4/24")
dogFour = Animal("Dog", "Pluto", "3 months", "2/2")
dogFive = Animal("Dog", "Milo", "7 years", "10/27")

listOfDogs = [dogOne, dogTwo, dogThree, dogFour, dogFive]

#cats
catOne = Animal("Cat", "Nimbus", "2 months", "3/12")
catTwo = Animal("Cat", "Whiskers", "1 week", "7/27")
catThree = Animal("Cat", "Luna", "7 months", "11/5")
catFour = Animal("Cat", "Pudding", "9 years", "1/15")
catFive = Animal("Cat", "Plagg", "9 months", "10/3")

listOfCats = [catOne, catTwo, catThree, catFour, catFive]


#lizards
lizardOne = Animal("Lizard", "Spike", "2 years", "9/4")
lizardTwo = Animal("Lizard", "Ziggy", "5 years", "3/14")
lizardThree = Animal("Lizard", "Basil", "8 years", "7/9")
lizardFour = Animal("Lizard", "Slinky", "1 year", "11/22")
lizardFive = Animal("Lizard", "Ember", "6 years", "5/30")

listOfLizards = [lizardOne, lizardTwo, lizardThree, lizardFour, lizardFive]

#turtles
turtleOne = Animal("Turtle", "Shelly", "7 years", "2/21")
turtleTwo = Animal("Turtle", "Leo", "15 years", "8/13")
turtleThree = Animal("Turtle", "Snappy", "4 years", "11/6")

listOfTurtle = [turtleOne, turtleTwo, turtleThree]

#pigs
pigOne = Animal("Pig", "Peppa", "9 months", "6/12")
pigTwo = Animal("Pig", "Truffle", "4 months", "11/21")
pigThree = Animal("Pig", "Chris P. Bacon", "7 months", "2/15")
pigFour = Animal("Pig", "Wilbur", "2 years", "8/4")
pigFive = Animal("Pig", "Hamlet", "11 months", "4/29")

listOfPigs = [pigOne, pigTwo, pigThree, pigFour, pigFive]

