from graphics import *
from globalVariables import *
from button import *
from popUp import popUp
from allAnimalsInfo import *
from createText import *


def clear():
    for item in win.items[:]:
        item.undraw()
    clickedOnAnimal = False

def checkClicks():
    from animalRentalScreens import (adoptButton, signupButton, homeButton, adoptPage_Dogs, homePage,
                                     signUpPageDesign, signInLogic, signInProceed, signUpProceed,
                                     signUpLogic, logOutButton, logOut, profileInfoButton,
                                     buyAccessoriesDesign, accessory1Button,profileInformation,
                                     accessory2Button, accessory3Button, accessoryProceed, receiptPage,
                                     goBackButton, proceedPurchaseButton, clickedOnAnimal)
    from animalRentalScreens import (dogButton, catButton, lizardButton, turtleButton, pigButton,
                                     choiceYes, choiceNo)
    if not win.isClosed():
        p = win.getMouse()

    if homeButton.buttonClicked(p):
        print("Home button clicked")  # Debugging
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

    from animalRentalScreens import (adoptPage_Cats, adoptPages_Lizard, adoptPage_Turtles, adoptPage_Pigs)

    if dogButton.buttonClicked(p):
        clear()
        setPage(2)
        setSubpage(2.1)
        setClickedOnAnimal(False)
        adoptPage_Dogs()

    if catButton.buttonClicked(p):
        clear()
        setPage(2)
        setSubpage(2.2)
        setClickedOnAnimal(False)
        adoptPage_Cats()

    if lizardButton.buttonClicked(p):
        clear()
        setPage(2)
        setSubpage(2.3)
        setClickedOnAnimal(False)
        adoptPages_Lizard()

    if turtleButton.buttonClicked(p):
        clear()
        setPage(2)
        setSubpage(2.4)
        setClickedOnAnimal(False)
        adoptPage_Turtles()

    if pigButton.buttonClicked(p):
        clear()
        setPage(2)
        setSubpage(2.5)
        setClickedOnAnimal(False)
        adoptPage_Pigs()

    if getPage() == 2:
        if (p.getX() >= winWidth - 150) and (p.getX() <= winWidth - 20) and (p.getY() >= winHeight - 100) and (
                p.getY() <= 700) and (getClickedOnAnimal()):
            from animalRentalScreens import adoptionProcess
            setClickedOnAnimal(False)
            clear()
            setPage(4)
            adoptionProcess()

    #shows the dog information when clicked
        if getSubpage() == 2.1:
            # each dog method
            from animalRentalScreens import (handleDogOne, handleDogTwo, handleDogThree, handleDogFour, handleDogFive)
            if (p.getX() >= 120) and (p.getX() <= 420) and (p.getY() >= 200) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleDogOne()
            if (p.getX() >= 450) and (p.getX() <= 1100) and (p.getY() >= 200) and (p.getY() <= 370):
                setClickedOnAnimal(True)
                handleDogTwo()
            if (p.getX() >= 450) and (p.getX() <= 820) and (p.getY() >= 400) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleDogThree()
            if (p.getX() >= 850) and (p.getX() <= 1110) and (p.getY() >= 400) and (p.getY() <= 530):
                setClickedOnAnimal(True)
                handleDogFour()
            if (p.getX() >= 850) and (p.getX() <= 1100) and (p.getY() >= 550) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleDogFive()

    ##FOR MEETING TWO
    #shows the cat information when clicked
        if getSubpage() == 2.2:
            # each cat method
            from animalRentalScreens import (handleCatOne, handleCatTwo, handleCatThree, handleCatFour,handleCatFive)

            if (p.getX() >= 120) and (p.getX() <= 600) and (p.getY() >= 400) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleCatOne()
            if (p.getX() >= 870) and (p.getX() <= 1100) and (p.getY() >= 550) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleCatTwo()
            if (p.getX() >= 630) and (p.getX() <= 850) and (p.getY() >= 550) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleCatThree()
            if (p.getX() >= 120) and (p.getX() <= 600) and (p.getY() >= 200) and (p.getY() <= 370):
                setClickedOnAnimal(True)
                handleCatFour()
            if (p.getX() >= 630) and (p.getX() <= 1100) and (p.getY() >= 200) and (p.getY() <= 530):
                setClickedOnAnimal(True)
                handleCatFive()
    #shows the lizard information when clicked
        if getSubpage() == 2.3:
            # each lizard method
            from animalRentalScreens import (handleLizardOne, handleLizardTwo, handleLizardThree, handleLizardFour, handleLizardFive)

            if (p.getX() >= 120) and (p.getX() <= 600) and (p.getY() >= 400) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleLizardOne()
            if (p.getX() >= 630) and (p.getX() <= 1100) and (p.getY() >= 550) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleLizardTwo()
            if (p.getX() >= 380) and (p.getX() <= 600) and (p.getY() >= 200) and (p.getY() <= 370):
                setClickedOnAnimal(True)
                handleLizardThree()
            if (p.getX() >= 120) and (p.getX() <= 350) and (p.getY() >= 200) and (p.getY() <= 370):
                setClickedOnAnimal(True)
                handleLizardFour()
            if (p.getX() >= 630) and (p.getX() <= 1100) and (p.getY() >= 200) and (p.getY() <= 530):
                setClickedOnAnimal(True)
                handleLizardFive()
        if getSubpage() == 2.4:
            # each turtle method
            from animalRentalScreens import (handleTurtleOne, handleTurtleTwo, handleTurtleThree)

            if (p.getX() >= 120) and (p.getX() <= 420) and (p.getY() >= 200) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleTurtleOne()
            if (p.getX() >= 460) and (p.getX() <= 760) and (p.getY() >= 200) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleTurtleTwo()
            if (p.getX() >= 800) and (p.getX() <= 1100) and (p.getY() >= 200) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handleTurtleThree()
        if getSubpage() == 2.5:
            # each pig method
            from animalRentalScreens import (handlePigOne, handlePigTwo, handlePigThree, handlePigFour, handlePigFive)

            if (p.getX() >= 120) and (p.getX() <= 430) and (p.getY() >= 460) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handlePigOne()
            if (p.getX() >= 800) and (p.getX() <= 1100) and (p.getY() >= 460) and (p.getY() <= 700):
                setClickedOnAnimal(True)
                handlePigTwo()
            if (p.getX() >= 450) and (p.getX() <= 780) and (p.getY() >= 330) and (p.getY() <= 570):
                setClickedOnAnimal(True)
                handlePigThree()
            if (p.getX() >= 120) and (p.getX() <= 430) and (p.getY() >= 210) and (p.getY() <= 440):
                setClickedOnAnimal(True)
                handlePigFour()
            if (p.getX() >= 800) and (p.getX() <= 1100) and (p.getY() >= 210) and (p.getY() <= 440):
                setClickedOnAnimal(True)
                handlePigFive()
    if getPage() == 3:
        if signInProceed.buttonClicked(p):
            signInLogic()
        if signUpProceed.buttonClicked(p):
            signUpLogic()
        if logOutButton.buttonClicked(p):
            logOut()
        if profileInfoButton.buttonClicked(p) and getUsername() != "":
            clear()
            profileInformation()

    if getPage() == 4:
        if choiceYes.buttonClicked(p):
            clear()
            setPage(5)
            buyAccessoriesDesign()
        if choiceNo.buttonClicked(p):
            setAdoptionPage(True)
            clear()
            setPage(6)
            receiptPage()

    ##accesory page, subtracting prices, resetting prices, etc.
    if getPage() == 5:

        if accessory1Button.buttonClicked(p) and not accessory1Button.selected:
            accessory1Button.setText("Selected")
            accessory1Button.toggleSelected()
            wantedAccessories.append("Clothing ($10)")
            changeTotalPrice(10)

        elif accessory1Button.buttonClicked(p) and accessory1Button.selected:
            accessory1Button.toggleSelected()
            accessory1Button.setText("Pick")
            wantedAccessories.remove("Clothing ($10)")
            changeTotalPrice(-10)

        if accessory2Button.buttonClicked(p) and not accessory2Button.selected:
            accessory2Button.setText("Selected")
            accessory2Button.toggleSelected()
            wantedAccessories.append("Food ($5)")
            changeTotalPrice(5)

        elif accessory2Button.buttonClicked(p) and accessory2Button.selected:
            accessory2Button.toggleSelected()
            accessory2Button.setText("Pick")
            wantedAccessories.remove("Food ($5)")
            changeTotalPrice(-5)

        if accessory3Button.buttonClicked(p) and not accessory3Button.selected:
            accessory3Button.setText("Selected")
            accessory3Button.toggleSelected()
            wantedAccessories.append("Toys ($25)")
            changeTotalPrice(25)


        elif accessory3Button.buttonClicked(p) and accessory3Button.selected:
            accessory3Button.toggleSelected()
            accessory3Button.setText("Pick")
            wantedAccessories.remove("Toys ($25)")
            changeTotalPrice(-25)


        if accessoryProceed.buttonClicked(p):
            clear()
            setPage(6)
            receiptPage()

    if getPage() == 6:
        if goBackButton.buttonClicked(p):
            clear()
            setPage(2)
            setSubpage(2.1)
            adoptPage_Dogs()
        if proceedPurchaseButton.buttonClicked(p):
            confirmAdoption()

def confirmAdoption():
    fileRes = open("takenSpots.txt", "a")
    if getSubpage() == 2.1:
        fileRes.write("\n" + getUsername() + "," + listOfDogs[getCurrentAnimal()].getName() + "," + getMinNum()
                      + "," + getMaxNum())
    if getSubpage() == 2.2:
        fileRes.write("\n" + getUsername() + "," + listOfCats[getCurrentAnimal()].getName() + "," + getMinNum()
                      + "," + getMaxNum())
    if getSubpage() == 2.3:
        fileRes.write("\n" + getUsername() + "," + listOfLizards[getCurrentAnimal()].getName() + "," + getMinNum()
            + "," + getMaxNum())
    if getSubpage() == 2.4:
        fileRes.write("\n" + getUsername() + "," + listOfTurtle[getCurrentAnimal()].getName() + "," + getMinNum()
            + "," + getMaxNum())
    if getSubpage() == 2.5:
        fileRes.write("\n" + getUsername() + "," + listOfPigs[getCurrentAnimal()].getName() + "," + getMinNum()
                      + "," + getMaxNum())

    text = textMaker(win, Point(650,700), "Adoption Placed!", 25, getThemeColor())

def createProceed():
    #if clickedOnAnimal is true and not on the adoption process page, show the proceed button
    if getClickedOnAnimal() and page != 4:
        buttonColor = getThemeColor()

        proceedButton = Button(win, Point(1215, 675),130,50,"Proceed", buttonColor)
        proceedButton.activate()

while True:
    global page
    from animalRentalScreens import win

    checkClicks()
    createProceed()

