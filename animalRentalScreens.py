import testingClicks
from globalVariables import *
from testingClicks import *
from allAnimalsInfo import *
from calendar import *
from button import *
from header import *
from eachPage import *
from createText import *
from indicator import *

#Page 1 = Home Page
#Page 2 = Rental Page
#Page 3 = Sign In Page
#Page 4 = Get Started on Adoption Page
#Page 5 = Accessory Page
#Page 6 = Receipt Page

choiceYes = Button(win, Point(450, 450), 150, 40, "Yes", "white")
choiceNo = Button(win, Point(850, 450), 150, 40, "No", "white")
choiceYes.changeTextColor("#B16E4B")
choiceNo.changeTextColor("#B16E4B")
buyMore = popUp(win, 300, 300, 1000, 500, "Would You Like To Buy Accessories?")

#-------------adoptSideBar--------------

dogButton = Button(win, Point(1215, 105), 130, 50, "Dogs", "#B16E4B")
catButton = Button(win, Point(1215, 175), 130, 50, "Cats", "#B16E4B")
lizardButton = Button(win, Point(1215, 245), 130, 50, "Lizards", "#B16E4B")
turtleButton = Button(win, Point(1215, 315), 130, 50, "Turtles", "#B16E4B")
pigButton = Button(win, Point(1215, 385), 130, 50, "Pigs", "#B16E4B")


def adoptSideBar():
    #Create clickable areas for each animal type
    dogButton.activate()
    catButton.activate()
    lizardButton.activate()
    turtleButton.activate()
    pigButton.activate()

#------------------draw paw------------#

def drawPaw(x1, y1):

    # Define the main pad (center circle)
    color = "#B16E4B"
    mainPaw = Circle(Point(x1, y1), 30)
    mainPaw.setFill(color)
    mainPaw.setOutline(None)
    mainPaw.draw(win)

    # Define the toe pads (smaller circles)
    toe1 = Circle(Point(x1-50, y1-40), 20)  # Toe 1 on the left
    toe2 = Circle(Point(x1+50, y1-40), 20)  # Toe 2 on the right
    toe3 = Circle(Point(x1-20, y1-80), 15)  # Toe 3 above left
    toe4 = Circle(Point(x1+20, y1-80), 15)  # Toe 4 above right

    # Set the fill color of the toe pads (optional)
    toe1.setFill(color)
    toe2.setFill(color)
    toe3.setFill(color)
    toe4.setFill(color)

    toe1.setOutline(None)
    toe2.setOutline(None)
    toe3.setOutline(None)
    toe4.setOutline(None)

    # Draw the toe pads
    toe1.draw(win)
    toe2.draw(win)
    toe3.draw(win)
    toe4.draw(win)

#-------------Home Page--------------
def homePage():
    global page
    setPage(0)
    headerDesign()
    menuHeading = textMaker(win, (Point(winWidth/2,winHeight/2-40)), "Animal Rental Center", 36, "#B16E4B")
    blurb = textMaker(win, (Point(winWidth/2,winHeight/2+70)), ("Welcome to Paws & Claws Pet Rentals — where finding your perfect companion has never been easier! "
                 "\n Whether you're looking for a furry friend for a weekend getaway or just a little extra joy in your life, "
                 "\nwe offer a wide variety of pets available for adoption on flexible terms. From playful puppies and kittens to gentle pigs,"
                 "\nexotic turtles, and even lizards, we have a pet for every lifestyle and need. At Paws & Claws, we believe that every person deserves the "
                 "\nlove and joy of a pet, without the long-term commitment. Our mission is to connect people with pets who can bring happiness, comfort, and "
                 "\ncompanionship, no matter how long or short the journey. Join us today and find your perfect pet match — adoption is just a click away!"), 20, "#B16E4B")
    win.setBackground("white")
    drawPaw(100,200)
    drawPaw(1200,700)

#-------------Adopt Page - Dog--------------
def adoptPage_Dogs():
    win.setBackground("white")
    headerDesign()
    setThemeColor("#C29B6C")
    setAdoptionPage(False)
    wantedAccessories.clear()
    setTotalPrice(0)

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(120,200), Point(420,700))
    image2 = Rectangle(Point(450,400), Point(820,700))
    image3 = Rectangle(Point(850, 550), Point(1100, 700))
    image4 = Rectangle(Point(450,200), Point(1100,370))
    image5 = Rectangle(Point(850, 400), Point(1100, 530))

    dogPages = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Our Lovely Dogs")

    adoptSideBar()
#------------------PLACEMENT-------------------------------------------------#

    #for i in range(10):
    #    p = win.getMouse()
    #    print(p.getX(), p.getY())


#------------- Each Dog  --------------
def handleDogOne():
    dogOne.displayInfo(270, 450, "white", 20)
    setCurrentAnimal(0)
    currentAnimalIndicatorD1.drawIndicator()

    #erase
    currentAnimalIndicatorD2.undrawIndicator()
    currentAnimalIndicatorD3.undrawIndicator()
    currentAnimalIndicatorD4.undrawIndicator()
    currentAnimalIndicatorD5.undrawIndicator()

def handleDogTwo():
    dogTwo.displayInfo(770, 285, "white", 20)
    setCurrentAnimal(1)
    currentAnimalIndicatorD2.drawIndicator()

    #erase
    currentAnimalIndicatorD1.undrawIndicator()
    currentAnimalIndicatorD3.undrawIndicator()
    currentAnimalIndicatorD4.undrawIndicator()
    currentAnimalIndicatorD5.undrawIndicator()

def handleDogThree():
    dogThree.displayInfo(640, 550, "white", 20)
    setCurrentAnimal(2)
    currentAnimalIndicatorD3.drawIndicator()

    #erase
    currentAnimalIndicatorD1.undrawIndicator()
    currentAnimalIndicatorD2.undrawIndicator()
    currentAnimalIndicatorD4.undrawIndicator()
    currentAnimalIndicatorD5.undrawIndicator()

def handleDogFour():
    dogFour.displayInfo(975, 465, "white", 20)
    setCurrentAnimal(3)
    currentAnimalIndicatorD4.drawIndicator()

    #erase
    currentAnimalIndicatorD1.undrawIndicator()
    currentAnimalIndicatorD2.undrawIndicator()
    currentAnimalIndicatorD3.undrawIndicator()
    currentAnimalIndicatorD5.undrawIndicator()

def handleDogFive():
    dogFive.displayInfo(975, 620, "white", 20)
    setCurrentAnimal(4)
    currentAnimalIndicatorD5.drawIndicator()

    #erase
    currentAnimalIndicatorD1.undrawIndicator()
    currentAnimalIndicatorD2.undrawIndicator()
    currentAnimalIndicatorD3.undrawIndicator()
    currentAnimalIndicatorD4.undrawIndicator()

#-------------Adopt Page - Cat--------------
def adoptPage_Cats():
    win.setBackground("white")
    headerDesign()
    adoptSideBar()
    setThemeColor("#9e9e9e")

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(120,400), Point(600,700))
    image2 = Rectangle(Point(870,550), Point(1100,700))
    image3 = Rectangle(Point(630, 550), Point(850, 700))
    image4 = Rectangle(Point(120,200), Point(600,370))
    image5 = Rectangle(Point(630, 200), Point(1100, 530))

    catPages = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Our Lovely Cats")
#------------- Each Cat  --------------
def handleCatOne():
    catOne.displayInfo(353, 551, "white", 20)
    setCurrentAnimal(0)
    currentAnimalIndicatorC1.drawIndicator()

    # erase
    currentAnimalIndicatorC2.undrawIndicator()
    currentAnimalIndicatorC3.undrawIndicator()
    currentAnimalIndicatorC4.undrawIndicator()
    currentAnimalIndicatorC5.undrawIndicator()

def handleCatTwo():
    catTwo.displayInfo(978, 627, "white", 20)
    setCurrentAnimal(1)
    currentAnimalIndicatorC2.drawIndicator()

    #erase
    currentAnimalIndicatorC1.undrawIndicator()
    currentAnimalIndicatorC3.undrawIndicator()
    currentAnimalIndicatorC4.undrawIndicator()
    currentAnimalIndicatorC5.undrawIndicator()

def handleCatThree():
    catThree.displayInfo(740, 627, "white", 20)
    setCurrentAnimal(2)
    currentAnimalIndicatorC3.drawIndicator()

    #erase
    currentAnimalIndicatorC1.undrawIndicator()
    currentAnimalIndicatorC2.undrawIndicator()
    currentAnimalIndicatorC4.undrawIndicator()
    currentAnimalIndicatorC5.undrawIndicator()

def handleCatFour():
    catFour.displayInfo(353, 278, "white", 20)
    setCurrentAnimal(3)
    currentAnimalIndicatorC4.drawIndicator()

    #erase
    currentAnimalIndicatorC1.undrawIndicator()
    currentAnimalIndicatorC2.undrawIndicator()
    currentAnimalIndicatorC3.undrawIndicator()
    currentAnimalIndicatorC5.undrawIndicator()

def handleCatFive():
    catFive.displayInfo(862, 356, "white", 20)
    setCurrentAnimal(4)
    currentAnimalIndicatorC5.drawIndicator()

    #erase
    currentAnimalIndicatorC1.undrawIndicator()
    currentAnimalIndicatorC2.undrawIndicator()
    currentAnimalIndicatorC3.undrawIndicator()
    currentAnimalIndicatorC4.undrawIndicator()

#-------------Adopt Page - Lizard--------------
def adoptPages_Lizard():

    win.setBackground("white")
    headerDesign()
    adoptSideBar()
    setThemeColor("#B38B9D")

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(120,400), Point(600,700))
    image2 = Rectangle(Point(630,550), Point(1100,700))
    image3 = Rectangle(Point(380, 200), Point(600, 370))
    image4 = Rectangle(Point(120,200), Point(350,370))
    image5 = Rectangle(Point(630, 200), Point(1100, 530))

    lizardPage = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Our Lovely Lizards")

# Each Lizard
def handleLizardOne():
    lizardOne.displayInfo(349.0, 557.0, "white", 20)
    setCurrentAnimal(0)
    currentAnimalIndicatorL1.drawIndicator()

    # erase
    currentAnimalIndicatorL2.undrawIndicator()
    currentAnimalIndicatorL3.undrawIndicator()
    currentAnimalIndicatorL4.undrawIndicator()
    currentAnimalIndicatorL5.undrawIndicator()

def handleLizardTwo():
    lizardTwo.displayInfo(855.0, 626.0, "white", 20)
    setCurrentAnimal(1)
    currentAnimalIndicatorL2.drawIndicator()

    # erase
    currentAnimalIndicatorL1.undrawIndicator()
    currentAnimalIndicatorL3.undrawIndicator()
    currentAnimalIndicatorL4.undrawIndicator()
    currentAnimalIndicatorL5.undrawIndicator()

def handleLizardThree():
    lizardThree.displayInfo(487.0, 286.0, "white", 20)
    setCurrentAnimal(2)
    currentAnimalIndicatorL3.drawIndicator()

    # erase
    currentAnimalIndicatorL1.undrawIndicator()
    currentAnimalIndicatorL2.undrawIndicator()
    currentAnimalIndicatorL4.undrawIndicator()
    currentAnimalIndicatorL5.undrawIndicator()

def handleLizardFour():
    lizardFour.displayInfo(235, 287, "white", 20)
    setCurrentAnimal(3)
    currentAnimalIndicatorL4.drawIndicator()

    # erase
    currentAnimalIndicatorL1.undrawIndicator()
    currentAnimalIndicatorL2.undrawIndicator()
    currentAnimalIndicatorL3.undrawIndicator()
    currentAnimalIndicatorL5.undrawIndicator()

def handleLizardFive():
    lizardFive.displayInfo(860.0, 357.0, "white", 20)
    setCurrentAnimal(4)
    currentAnimalIndicatorL5.drawIndicator()

    # erase
    currentAnimalIndicatorL1.undrawIndicator()
    currentAnimalIndicatorL2.undrawIndicator()
    currentAnimalIndicatorL3.undrawIndicator()
    currentAnimalIndicatorL4.undrawIndicator()

#-------------Adopt Page - Turtle --------------
def adoptPage_Turtles():

    win.setBackground("white")
    headerDesign()
    adoptSideBar()
    setThemeColor("#ADD0B3")

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(120, 200), Point(420, 700))
    image2 = Rectangle(Point(460, 200), Point(760, 700))
    image3 = Rectangle(Point(800, 200), Point(1100, 700))
    image4 = Rectangle(Point(0, 0), Point(0, 0))
    image5 = Rectangle(Point(0, 0), Point(0, 0))

    lizardPage = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Our Lovely Turtles")
# Each Turtle
def handleTurtleOne():
    turtleOne.displayInfo(270, 450, "white", 20)
    setCurrentAnimal(0)
    currentAnimalIndicatorT1.drawIndicator()

    # erase
    currentAnimalIndicatorT2.undrawIndicator()
    currentAnimalIndicatorT3.undrawIndicator()

def handleTurtleTwo():
    turtleTwo.displayInfo(610, 450, "white", 20)
    setCurrentAnimal(1)
    currentAnimalIndicatorT2.drawIndicator()

    # erase
    currentAnimalIndicatorT1.undrawIndicator()
    currentAnimalIndicatorT3.undrawIndicator()

def handleTurtleThree():
    turtleThree.displayInfo(945, 450, "white", 20)
    setCurrentAnimal(2)
    currentAnimalIndicatorT3.drawIndicator()

    # erase
    currentAnimalIndicatorT2.undrawIndicator()
    currentAnimalIndicatorT1.undrawIndicator()

#-------------Adopt Page - Pigs --------------
def adoptPage_Pigs():
    win.setBackground("white")
    headerDesign()
    adoptSideBar()
    setThemeColor("#FB928E")

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(120,460), Point(430,700))
    image2 = Rectangle(Point(800,460), Point(1100,700))
    image3 = Rectangle(Point(450, 330), Point(780, 570))
    image4 = Rectangle(Point(120,210), Point(430,440))
    image5 = Rectangle(Point(800,210), Point(1100,440))

    pigPage = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Our Lovely Pigs")

# Each pig
def handlePigOne():
    pigOne.displayInfo(270, 580, "white", 20)
    setCurrentAnimal(0)
    currentAnimalIndicatorP1.drawIndicator()

    # erase
    currentAnimalIndicatorP2.undrawIndicator()
    currentAnimalIndicatorP3.undrawIndicator()
    currentAnimalIndicatorP4.undrawIndicator()
    currentAnimalIndicatorP5.undrawIndicator()

def handlePigTwo():
    pigTwo.displayInfo(952, 580, "white", 20)
    setCurrentAnimal(1)
    currentAnimalIndicatorP2.drawIndicator()

    # erase
    currentAnimalIndicatorP1.undrawIndicator()
    currentAnimalIndicatorP3.undrawIndicator()
    currentAnimalIndicatorP4.undrawIndicator()
    currentAnimalIndicatorP5.undrawIndicator()

def handlePigThree():
    pigThree.displayInfo(612, 451, "white", 20)
    setCurrentAnimal(2)
    currentAnimalIndicatorP3.drawIndicator()

    # erase
    currentAnimalIndicatorP2.undrawIndicator()
    currentAnimalIndicatorP1.undrawIndicator()
    currentAnimalIndicatorP4.undrawIndicator()
    currentAnimalIndicatorP5.undrawIndicator()

def handlePigFour():
    pigFour.displayInfo(270, 332, "white", 20)
    setCurrentAnimal(3)
    currentAnimalIndicatorP4.drawIndicator()

    # erase
    currentAnimalIndicatorP2.undrawIndicator()
    currentAnimalIndicatorP3.undrawIndicator()
    currentAnimalIndicatorP1.undrawIndicator()
    currentAnimalIndicatorP5.undrawIndicator()

def handlePigFive():
    pigFive.displayInfo(952, 332, "white", 20)
    setCurrentAnimal(4)
    currentAnimalIndicatorP5.drawIndicator()

    # erase
    currentAnimalIndicatorP2.undrawIndicator()
    currentAnimalIndicatorP3.undrawIndicator()
    currentAnimalIndicatorP4.undrawIndicator()
    currentAnimalIndicatorP1.undrawIndicator()

#-------------Header Design for All Pages--------------

homeButton = Button(win, Point(200, 40), 100, 40, "Home", "#B16E4B")
adoptButton = Button(win, Point(winWidth / 2, 40), 100, 40, "Adopt", "#B16E4B")
signupButton = Button(win, Point(winWidth - 200, 40), 100, 40, "Sign Up", "#B16E4B")

def headerDesign():
    dropDownBackground = Header(0,0,winWidth,70)
    homeButton.activate()
    adoptButton.activate()
    signupButton.activate()

#-------------------- signUp Tab ----------------------#

signInUsername = entryInformation(win, (Point(325, 300)), 40, "white", 20, "Username")
signInPassword = entryInformation(win, (Point(325, 450)), 40, "white", 20, "Password")
signUpUsername = entryInformation(win, (Point(975, 300)), 40, "white", 20, "Desired Username")
signUpPassword = entryInformation(win, (Point(975, 450)), 40, "white", 20, "Desired Password")
signInProceed = Button(win, Point(325, 600), 130, 50, "Sign In", "#B16E4B")
signUpProceed = Button(win, Point(975, 600), 130, 50, "Sign Up", "#B16E4B")
logOutButton = Button(win, Point(winWidth-70, winHeight-30), 130, 50, "Log out", "#B16E4B")
profileInfoButton = Button(win, Point(winWidth-70, winHeight-100), 130, 50, "Profile", "#B16E4B")


signInMessage = textMaker(win, (Point(325, 675)), "", 30, "#B16E4B")
signUpMessage = textMaker(win, (Point(975, 675)), "", 30, "#B16E4B")
logOutMessage = textMaker(win, (Point(winWidth / 2, 675)), "", 30, "#B16E4B")


def signUpPageDesign():
    win.setBackground("white")
    headerDesign()
    setAdoptionPage(False)

    signInUsername.setText("Username")
    signInPassword.setText("Password")
    signUpUsername.setText("Desired Username")
    signUpPassword.setText("Desired Password")

    signInProceed.activate()
    signUpProceed.activate()
    logOutButton.activate()
    profileInfoButton.activate()

    heading = textMaker(win, (Point(winWidth/2-320, 150)), "Sign In", 36, "#B16E4B")
    heading2 = textMaker(win, (Point(winWidth/2+320, 150)), "Sign Up", 36, "#B16E4B")

    image1 = Rectangle(Point(100,200),Point(550,550))
    image2 = Rectangle(Point(750, 200), Point(1200, 550))
    image3 = Rectangle(Point(0, 0), Point(0, 0))
    image4 = Rectangle(Point(0, 0), Point(0, 0))
    image5 = Rectangle(Point(0, 0), Point(0, 0))
    signUpBackground = Pages(win, image1, image2, image3, image4, image5, "#B16E4B", Point(0,0), "")

    signInUsername.showEntry()
    signInPassword.showEntry()
    signUpUsername.showEntry()
    signUpPassword.showEntry()

signDict = {}

def readLogInInformation():
    global signDict
    fileRes = open("usersInformation.txt", "r")
    personsInformation = fileRes.readlines()
    for eachPerson in personsInformation:
        eachPerson = (eachPerson.strip()).split(",")
        username = eachPerson[0]
        password = eachPerson[1]
        signDict[username] = password

usernameFound = False

def signInLogic():
    if signInMessage.active:
        signInMessage.undrawText()
    if signUpMessage.active:
        signUpMessage.undrawText()
    logOutMessage.undrawText()

    signInMessage.drawText()
    signInMessage.setText("")

    readLogInInformation()
    listOfAllUsernames = list(signDict.keys())
    usernameFound = False
    text = ""

    if signInUsername.getText() == "Username" or signInPassword.getText() == "Password" or signInUsername.getText() == "" or signInPassword.getText() == "":
        text = "Please enter a username \nand/or password"
    else:
        for eachUser in listOfAllUsernames:
            if signInUsername.getText() == eachUser:
                usernameFound = True
                if signInPassword.getText() == signDict.get(eachUser):
                    text = "Sign In Complete!"
                    signupButton.setText(signInUsername.getText())
                    setUsername(signInUsername.getText())
                    break
                elif signInPassword.getText() != signDict.get(eachUser) and usernameFound:
                    text = "Password does not match username."
                    break
        if not usernameFound:
            text = "No username found."

    signInMessage.setText(text)

    signInUsername.setText("Username")
    signInPassword.setText("Password")


def signUpLogic():
    if signInMessage.active:
        signInMessage.undrawText()
    if signUpMessage.active:
        signUpMessage.undrawText()
    logOutMessage.undrawText()

    signUpMessage.drawText()
    signUpMessage.setText("")

    readLogInInformation()

    listOfAllUsernames = list(signDict.keys())
    usernameFound = False
    text = ""

    if signUpUsername.getText() == "Desired Username" or signUpPassword.getText() == "Desired Password" or signUpUsername.getText() == "" or signUpPassword.getText() == "":
        text = "Please enter a username \nand/or password"
    else:
        # Check if the username is already taken
        for eachUser in listOfAllUsernames:
            if signUpUsername.getText() == eachUser:
                text = "Username is taken. \nPlease choose another."
                usernameFound = True
                break  # Exit the loop if username is found

        # If username is not taken, proceed with sign-up
        if not usernameFound:
            text = "Sign Up Completed! \nPlease Sign In."
            usernameFound = False
            # Write the new user credentials to the file
            with open("usersInformation.txt", "a") as fileRes:
                fileRes.write("\n" + signUpUsername.getText() + "," + signUpPassword.getText())

    # Set the text message for the user (either success or error)
    signUpMessage.setText(text)

    # Reset the input fields
    signUpUsername.setText("Desired Username")
    signUpPassword.setText("Desired Password")


def logOut():
    signUpMessage.setText("")
    signInMessage.setText("")
    if getUsername() == "":
        text = "You Are Not Logged In."
    else:
        signupButton.setText("Sign Up")
        setUsername("")
        text = "Logged Out!"
    logOutMessage.setText(text)
    if not logOutMessage.active:
        logOutMessage.drawText()


def profileInformation():
    headerDesign()
    win.setBackground("white")
    setThemeColor("#b47578")
    fileRes = open("takenSpots.txt", "r")
    reservation = fileRes.readlines()
    count = 0

    suffixes = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                '13th', '14th',
                '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                '26th', '27th',
                '28th', '29th', '30th', '31st']

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(650, 250), Point(950, 700))
    image2 = Rectangle(Point(150, 250), Point(450, 300))
    image3 = Rectangle(Point(150, 305), Point(450, 355))
    image4 = Rectangle(Point(150, 360), Point(450, 410))
    image5 = Rectangle(Point(0, 0), Point(0, 0))

    profilePage = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading,
                           getUsername() + "'s Profile")
    yourAdoptionText = textMaker(win, Point(800,200), getUsername() + "'s Adoptions", 36, getThemeColor())
    yourInfoText = textMaker(win, Point(300,200), getUsername() + "'s Information", 36, getThemeColor())
    infoText =  textMaker(win, Point(300,330), "Registered User: Yes\n\nVerified: Yes\n\nTraining: Completed", 25, "white")


    for eachReservation in reservation:
        eachReservation = eachReservation.strip()
        eachReservation = eachReservation.split(",")
        usernameWhoTook = eachReservation[0]
        animalName = eachReservation[1]
        startReservation = int(eachReservation[2])
        endReservation = int(eachReservation[3])
        if usernameWhoTook == getUsername():
            yourAnimalText = ("Name: " + animalName +
                    "\nReservation: " + suffixes[startReservation-1] + " to " + suffixes[endReservation-1])
            text = textMaker(win, Point(800,(count*100)+320), yourAnimalText, 25, "white")
            count+=1


#------------------Buy Accessories------------------#
accessory1Button = Button(win, Point(255,700), 130, 40, "Pick", "#7fc2c4")
accessory2Button = Button(win, Point(645,700), 130, 40, "Pick", "#7fc2c4")
accessory3Button = Button(win, Point(1035,700), 130, 40, "Pick", "#7fc2c4")
accessoryProceed = Button(win, Point(1230,700), 130, 40, "Proceed", "#7fc2c4")

def buyAccessoriesDesign():
    headerDesign()
    win.setBackground("white")
    setThemeColor("#7fc2c4")
    setTotalPrice(0)
    accessory1Button.setSelected(False)
    accessory2Button.setSelected(False)
    accessory3Button.setSelected(False)
    accessory1Button.setText("Pick")
    accessory2Button.setText("Pick")
    accessory3Button.setText("Pick")
    wantedAccessories.clear()

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(150,220), Point(380,420))
    image2 = Rectangle(Point(540, 220), Point(770, 420))
    image3 = Rectangle(Point(920, 220), Point(1150, 420))
    image4 = Rectangle(Point(0,0), Point(0,0))
    image5 = Rectangle(Point(0, 0), Point(0, 0))

    buyAccessories = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading, "Buy Accessories")
    textPrices = textMaker(win, Point(winWidth/2,325), "$10                                       $5                                     $25", 36, "white")
    text1 = ("A stylish and functional clothing "
             "\naccessory for pets, designed to "
             "\nenhance their comfort and fashion. "
             "\nWhether it's a cozy sweater, a "
             "\ntrendy bandana, or a durable collar, "
             "\nthese accessories add personality while "
             "\nkeeping your furry friend looking great "
             "\nand feeling secure. Perfect for any "
             "\noccasion, from casual walks to special "
             "\nevents!")
    text2 = ("Nutrient-rich and delicious, our pet "
             "\nfood is specially crafted to meet the "
             "\nunique dietary needs of your furry "
             "\nfriend. Made with high-quality "
             "\ningredients, it offers a balanced mix of "
             "\nprotein, vitamins, and minerals to support "
             "\noverall health, energy, and vitality. "
             "\nWhether for dogs or pigs, it's a tasty and "
             "\nwholesome choice your pet will love!")
    text3 = ("A fun and engaging toy accessory for "
             "\npets, designed to stimulate their "
             "\nminds and keep them active. From "
             "\nchew toys that promote dental health "
             "\nto interactive puzzles and plush "
             "\nfavorites, these toys provide "
             "\nentertainment, exercise, and enrichment, "
             "\nmaking them a must-have for any playful "
             "\npet!")
    accessory1Heading = textMaker(win, Point(265,190), "Clothing", 30, getThemeColor())
    accessory2Heading = textMaker(win, Point(655,190), "Food", 30, getThemeColor())
    accessory3Heading = textMaker(win, Point(1035,190), "Toys", 30, getThemeColor())
    accessory1 = textMaker(win, Point(275,550), text1, 20, getThemeColor())
    accessory2 = textMaker(win, Point(665, 540), text2, 20, getThemeColor())
    accessory3 = textMaker(win, Point(1045, 540), text3, 20, getThemeColor())

    accessory1Button.activate()
    accessory2Button.activate()
    accessory3Button.activate()
    accessoryProceed.activate()


proceedPurchaseButton = Button(win, Point(900, 570), 170, 40, "Confirm", "#e2b571")
goBackButton = Button(win, Point(900, 630), 170, 40, "Back To Adopt", "#e2b571")

def receiptPage():
    headerDesign()
    win.setBackground("white")
    setThemeColor("#e2b571")

    adoptHeading = Point(winWidth / 2, 120)

    image1 = Rectangle(Point(500, 220), Point(800, 650))
    image2 = Rectangle(Point(0, 0), Point(0, 0))
    image3 = Rectangle(Point(0, 0), Point(0, 0))
    image4 = Rectangle(Point(0, 0), Point(0, 0))
    image5 = Rectangle(Point(0, 0), Point(0, 0))
    buyAccessories = Pages(win, image1, image2, image3, image4, image5, getThemeColor(), adoptHeading,
                           "Receipt")
    heading = textMaker(win, Point(650,260), getUsername(), 30, "white")

    line = Rectangle(Point(550, 290), Point(750, 291))
    line.setFill("white")
    line.setOutline(None)
    line.draw(win)

    if getSubpage() == 2.1:
        textType = textMaker(win, Point(650,320), ("Type                           " + listOfDogs[getCurrentAnimal()].getType()), 25, "white")
        textName = textMaker(win, Point(650,360), ("Name                         " + listOfDogs[getCurrentAnimal()].getName()), 25, "white")
        textAge = textMaker(win, Point(650,400), ("Age                        " + listOfDogs[getCurrentAnimal()].getAge()), 25, "white")
        textDates = textMaker(win, Point(648,440), ("Dates                 " + getMinDay() + " to " + getMaxDay()), 25, "white")

    if getSubpage() == 2.2:
        textType = textMaker(win, Point(650,320), ("Type                           " + listOfCats[getCurrentAnimal()].getType()), 25, "white")
        textName = textMaker(win, Point(650,360), ("Name                         " + listOfCats[getCurrentAnimal()].getName()), 25, "white")
        textAge = textMaker(win, Point(650,400), ("Age                        " + listOfCats[getCurrentAnimal()].getAge()), 25, "white")
        textDates = textMaker(win, Point(648,440), ("Dates                 " + getMinDay() + " to " + getMaxDay()), 25, "white")

    if getSubpage() == 2.3:
        textType = textMaker(win, Point(650,320), ("Type                           " + listOfLizards[getCurrentAnimal()].getType()), 25, "white")
        textName = textMaker(win, Point(650,360), ("Name                         " + listOfLizards[getCurrentAnimal()].getName()), 25, "white")
        textAge = textMaker(win, Point(650,400), ("Age                        " + listOfLizards[getCurrentAnimal()].getAge()), 25, "white")
        textDates = textMaker(win, Point(648,440), ("Dates                 " + getMinDay() + " to " + getMaxDay()), 25, "white")

    if getSubpage() == 2.4:
        textType = textMaker(win, Point(650,320), ("Type                           " + listOfTurtle[getCurrentAnimal()].getType()), 25, "white")
        textName = textMaker(win, Point(650,360), ("Name                         " + listOfTurtle[getCurrentAnimal()].getName()), 25, "white")
        textAge = textMaker(win, Point(650,400), ("Age                        " + listOfTurtle[getCurrentAnimal()].getAge()), 25, "white")
        textDates = textMaker(win, Point(648,440), ("Dates                 " + getMinDay() + " to " + getMaxDay()), 25, "white")

    if getSubpage() == 2.5:
        textType = textMaker(win, Point(650,320), ("Type                           " + listOfPigs[getCurrentAnimal()].getType()), 25, "white")
        textName = textMaker(win, Point(650,360), ("Name                  " + listOfPigs[getCurrentAnimal()].getName()), 25, "white")
        textAge = textMaker(win, Point(650,400), ("Age                        " + listOfPigs[getCurrentAnimal()].getAge()), 25, "white")
        textDates = textMaker(win, Point(648,440), ("Dates                 " + getMinDay() + " to " + getMaxDay()), 25, "white")

    text2 = "Accessories "
    text3 = "Total Price                    $" + str(getTotalPrice())
    count = 0
    for i in wantedAccessories:
        wordLength = 0
        if i[0] == "F":
            wordLength = 0
        elif i[0] == "T":
            wordLength = 3
        elif i[0] == "C":
            wordLength = 22
        text = textMaker(win, Point(740 - wordLength,(count*40)+480), i, 25, "white")
        count+=1
    accessoriesInfo = textMaker(win, Point(570,480), text2, 25, "white")
    totalPriceInfo = textMaker(win, Point(650,620), text3, 25, "white")

    proceedPurchaseButton.activate()
    goBackButton.activate()

#-------------------------adoption------------------------------#

def adoptionProcess():
    headerDesign()
    menuHeading = textMaker(win, (Point(winWidth / 2, 120)), "Get Started on Your Rental", 36, getThemeColor())

    if getSubpage() == 2.1:
        information = textMaker(win, (Point(winWidth/4+30,winHeight/2+30)), ("You have selected to adopt " + listOfDogs[getCurrentAnimal()].getName() +
                           " the " + listOfDogs[getCurrentAnimal()].getType() + ", who is \n" + listOfDogs[getCurrentAnimal()].getAge() +
                           " old. Their birthday is " + listOfDogs[getCurrentAnimal()].getBirthday() + ". Please select what days \nyou want to have "
                           + listOfDogs[getCurrentAnimal()].getName() +
                           ". Please be advised that the \nminimum adoption period is 2 days, and the maximum \nadoption period is "
                           + listOfDogs[getCurrentAnimal()].maxAdoptionPeriod() + " days.\n(Yellow: Your reservation\nRed: Others' Reservation)"), 25, getThemeColor())


    elif getSubpage() == 2.2:
        information = textMaker(win, (Point(winWidth/4+30,winHeight/2+30)), ("You have selected to adopt " + listOfCats[getCurrentAnimal()].getName() +
                           " the " + listOfCats[getCurrentAnimal()].getType() + ", who is \n" + listOfCats[getCurrentAnimal()].getAge() +
                           " old. Their birthday is " + listOfCats[getCurrentAnimal()].getBirthday() + ". Please select what days \nyou want to have "
                           + listOfCats[getCurrentAnimal()].getName() +
                           ". Please be advised that the \nminimum adoption period is 2 days, and the maximum \nadoption period is "
                           + listOfCats[getCurrentAnimal()].maxAdoptionPeriod() + " days.\n(Yellow: Your reservation\nRed: Others' Reservation)"), 25, getThemeColor())

    elif getSubpage() == 2.3:
        information = textMaker(win, (Point(winWidth/4+30,winHeight/2+30)), ("You have selected to adopt " + listOfLizards[getCurrentAnimal()].getName() +
                           " the " + listOfLizards[getCurrentAnimal()].getType() + ", who is \n" + listOfLizards[getCurrentAnimal()].getAge() +
                           " old. Their birthday is " + listOfLizards[getCurrentAnimal()].getBirthday() + ". Please select what days \nyou want to have "
                           + listOfLizards[getCurrentAnimal()].getName() +
                           ". Please be advised that the \nminimum adoption period is 2 days, and the maximum \nadoption period is "
                           + listOfLizards[getCurrentAnimal()].maxAdoptionPeriod() + " days.\n(Yellow: Your reservation\nRed: Others' Reservation)"), 25, getThemeColor())

    elif getSubpage() == 2.4:
        information = textMaker(win, (Point(winWidth/4+30,winHeight/2+30)), ("You have selected to adopt " + listOfTurtle[getCurrentAnimal()].getName() +
                           " the " + listOfTurtle[getCurrentAnimal()].getType() + ", who is \n" + listOfTurtle[getCurrentAnimal()].getAge() +
                           " old. Their birthday is " + listOfTurtle[getCurrentAnimal()].getBirthday() + ". Please select what days \nyou want to have "
                           + listOfTurtle[getCurrentAnimal()].getName() +
                           ". Please be advised that the \nminimum adoption period is 2 days, and the maximum \nadoption period is "
                           + listOfTurtle[getCurrentAnimal()].maxAdoptionPeriod() + " days.\n(Yellow: Your reservation\nRed: Others' Reservation)"), 25, getThemeColor())

    elif getSubpage() == 2.5:
        information = textMaker(win, (Point(winWidth/4+30,winHeight/2+30)), ( "You have selected to adopt " + listOfPigs[getCurrentAnimal()].getName() +
                           " the " + listOfPigs[getCurrentAnimal()].getType() + ", who is \n" + listOfPigs[getCurrentAnimal()].getAge() +
                           " old. Their birthday is " + listOfPigs[getCurrentAnimal()].getBirthday() + ". Please select what days \nyou want to have "
                           + listOfPigs[getCurrentAnimal()].getName() +
                           ". Please be advised that the \nminimum adoption period is 2 days, and the maximum \nadoption period is "
                           + listOfPigs[getCurrentAnimal()].maxAdoptionPeriod() + " days.\n(Yellow: Your reservation\nRed: Others' Reservation)"), 25, getThemeColor())

    adoptionCalendar = AdoptionCalendar(win, 31, 3, getCurrentAnimal())

homePage()
#p = win.getMouse()
