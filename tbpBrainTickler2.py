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
        if inputList[i].getShip(inputList[i]) == shipName:
            return i
    else:
        return -1
    
def getCaptainPosition(captainName, inputList):
    for i in range(len(inputList)):
        if inputList[i].getName(inputList[i]) == captainName:
            return i
    else:
        return -1
    

def checkRules(inputList):

    testsPassing = True

    checkRuleI(inputList)
    checkRuleII(inputList)
    checkRuleIII(inputList)
    checkRuleIV(inputList)
    checkRuleV(inputList)
    checkRuleVI(inputList)
    checkRuleVII(inputList)
    checkRuleVIII(inputList)

def checkRuleI(inputList):

    if getShipPosition("Albacore", inputList) == getCaptainPosition("S", inputList) and getCaptainPosition("S", inputList) != 0 and getCaptainPosition("S", inputList) != 4:
        
    else:
        testsPassing = False

def checkRuleII(inputList):
    
    if inputList[getCaptainPosition("W", inputList)].getShip == "Hammerhead" and (getShipPosition("Hammerhead", inputList) + 1) == getCaptainPosition("T", inputList) and  inputList[getCaptainPosition("T", inputList)].getShip != "Bass":
        return "PASS"
    else:
        testsPassing = False

def checkRuleIII(inputList):

    if getShipPosition("Coho", inputList) == 4:
        return "PASS"
    else:
        testsPassing = False

def checkRuleIV(inputList):

    if getCaptainPosition("U", inputList) == (getCaptainPosition("V", inputList) + 1):
        return "PASS"
    else:
        testsPassing = False

def checkRuleV(inputList):

    if getCaptainPosition("X", inputList) == (getShipPosition("Eel", inputList) - 1) and getCaptainPosition("X", inputList) == (getShipPosition("Dogfish", inputList) + 1):
        return "PASS"
    else:
        testsPassing = False

def checkRuleVI(inputList):

    if getCaptainPosition("Y", inputList) == 3:
        return "PASS"
    else:
        testsPassing = False

def checkRuleVII(inputList):

    if inputList[1].getMedals < inputList[getShipPosition("Flounder", inputList)].getMedals and getShipPosition("Flounder", inputList) != 0 and getShipPosition("Flounder", inputList) != 2:
        return "PASS"
    else:
        testsPassing = False

def checkRuleVIII(inputList):

    if inputList[0].getMedals(inputList[0]) > 4:
        return "PASS"
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

for permCaptains in captains:
    #result will be list of Captains
    for captain in permCaptains:
        #result will be a Captain
        for permShips in ships:
            #result will be list of ships (Strings)
            for ship in permShips:
                captain.setShip(captain, ship)
    checkRules(permCaptains)