
class panel_production():
    Owner = ''
    panelNumber = 0
    dimX = 0
    dimY = 0
    totalWatt= 0
    OC_V = 0
    SC_I = 0
    
    #define inputs
    def setOCV(self, OC_V):
        self.OC_V = OC_V
    
    def setSCI(self, SC_I):
        self.SC_I = SC_I
        
    def getOCV(self):
        return self.OC_V
    
    def getSCI(self):
        return self.SC_I
        
    def efficiency(self):
        currentPow = self.OC_V*self.SC_I
        return currentPow/self.totalWatt
    
    def getOwner(self):
        return self.Owner
    
    def __init__(self, name, dimX, dimY, totalWatt, panelNumber):
        self.Owner = name
        self.dimX = dimX
        self.dimY = dimY
        self.totalWatt = totalWatt
        self.panelNumber = panelNumber