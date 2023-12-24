import itertools

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
        return "PASS"
    else:
        return "FAIL"

def checkRuleII(inputList):
    
    if 

def checkRuleIII(inputList):

    if getShipPosition("Coho", inputList) == 4:
        return "PASS"
    else:
        return "FAIL"

def checkRuleIV(inputList):

def checkRuleV(inputList):

def checkRuleVI(inputList):

def checkRuleVII(inputList):

def checkRuleVIII(inputList):

    
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

for permCaptains in captains:
    #result will be list of Captains
    for captain in permCaptains:
        #result will be a Captain
        for permShips in ships:
            #result will be list of ships (Strings)
            for ship in permShips:
                captain.setShip(captain, ship)
    checkRules(permCaptains)