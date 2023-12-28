import itertools
from enum import Enum

"""class FailType(Enum):
    SHIPORDER = 0, 
    CAPTAINORDER = 1"""
class Captain:

    def __init__(self, name, medals, ship):
        self.name = name
        self.medals = medals
        self.ship = ship
    
    def __str__(self):
        return f"Captain: {self.name}, Ship: {self.ship}"

    def getMedals(self):
        return self.medals
    
    def getShip(self):
        return self.ship
    
    def getName(self):
        return self.name
    
    def setShip(self, ship):
        self.ship = ship


def getShipPosition(shipName, inputList):
    for i in range(len(inputList)):
        if inputList[i].getShip() == shipName:
            return i
    else:
        return -1
    
def getCaptainPosition(captainName, inputList):
    for i in range(len(inputList)):
        if inputList[i].getName() == captainName:
            return i
    else:
        return -1
    
def printCaptains(captains):
    for i in range(len(captains)):
        print(captains[i])

def checkRules(inputList):

    global testsPassing
    testsPassing = True

    checks = [checkRuleI, checkRuleII, checkRuleIII, checkRuleIV, checkRuleV, checkRuleVI, checkRuleVII]

    for check in checks:
        check(inputList)
        if testsPassing == False:
            break

    if testsPassing:
        return "SOLUTION FOUND"


def checkRuleI(inputList):

    global testsPassing

    if getShipPosition("Albacore", inputList) == (getCaptainPosition("S", inputList) + 2) and getCaptainPosition("S", inputList) != 0 and getCaptainPosition("S", inputList) != 4:
        return
    else:
        testsPassing = False

def checkRuleII(inputList):

    global testsPassing
    
    if inputList[getCaptainPosition("W", inputList)].getShip() == "Hammerhead" and getShipPosition("Hammerhead", inputList) == (getCaptainPosition("T", inputList) + 1) and  inputList[getCaptainPosition("T", inputList)].getShip() != "Bass":
        return
    else:
        testsPassing = False

def checkRuleIII(inputList):

    global testsPassing

    if getShipPosition("Coho", inputList) == 4:
        return
    else:
        testsPassing = False

def checkRuleIV(inputList):

    global testsPassing

    if getCaptainPosition("U", inputList) == (getCaptainPosition("V", inputList) + 1):
        return
    else:
        testsPassing = False

def checkRuleV(inputList):

    global testsPassing

    if getCaptainPosition("X", inputList) == (getShipPosition("Eel", inputList) - 1) and getCaptainPosition("X", inputList) == (getShipPosition("Dogfish", inputList) + 1):
        return 
    else:
        testsPassing = False

def checkRuleVI(inputList):

    global testsPassing

    if getCaptainPosition("Y", inputList) == 3:
        return 
    else:
        testsPassing = False

def checkRuleVII(inputList):

    global testsPassing

    if inputList[1].getMedals() < inputList[getShipPosition("Flounder", inputList)].getMedals() and getShipPosition("Flounder", inputList) != 0 and getShipPosition("Flounder", inputList) != 2:
        return
    else:
        testsPassing = False

def checkRuleVIII(inputList):

    global testsPassing

    if inputList[0].getMedals() > 4:
        return
    else:
        testsPassing = False

    
s = Captain("S", 6, "")
t = Captain("T", 4, "")
u = Captain("U", 5, "")
v = Captain("V", 5, "")
w = Captain("W", 4, "")
x = Captain("X", 5, "")
y = Captain("Y", 6, "")
z = Captain("Z", 6, "")

captains = list(itertools.permutations([s, t, u, v, w, x, y, z]))
ships = list(itertools.permutations(["Albacore", "Hammerhead", "Bass", "Coho", "Dogfish", "Eel", "Gar", "Flounder"]))

solutionFound = False
checkID = 0

for permCaptains in captains:
    #for every permutation of Captains... (result will be list of Captains)

    #knock out some permutations on the basis of incorrect captain positions
    if permCaptains[0].getMedals() < 5:
        continue
    elif permCaptains[3].getName() != "Y":
        continue
    elif permCaptains[0].getName() == "S" or permCaptains[4].getName() == "S":
        continue
    

    for permShips in ships:

        """#knock out some permutations on the basis of incorrect ship position
        if getShipPosition("Coho", permShips) != 4:
            continue
        elif getShipPosition("Flounder", permShips) == 0 or getShipPosition("Flounder", permShips) == 2:
            continue
        elif getCaptainPosition("W", permCaptains) != getShipPosition("Hammerhead", permShips):
            continue"""
        
        #for every permutation of Ships... (result will be list of ships (Strings))
        for i in range(len(permShips)):
            permCaptains[i].setShip(permShips[i])
            
        #print("Check ID: " + str(checkID))
        checkResult = checkRules(permCaptains)
        checkID += 1

        if checkResult == "SOLUTION FOUND":
            solutionFound = True
            print("SOLUTION FOUND")
            printCaptains(permCaptains)
            exit()

if not solutionFound:
    print("No solution was found.")