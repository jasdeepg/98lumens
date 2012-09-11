
class stateReg():
    stateName = ''
    elecCost = 0
    waterCost = 0
    
    #outputs
    def geteCost(self):
        return self.elecCost

    def getwCost(self):
        return self.waterCost
    
    def __init__(self, stateName, elecCost, waterCost):
        self.stateName = stateName
        self.elecCost = elecCost
        self.waterCost = waterCost