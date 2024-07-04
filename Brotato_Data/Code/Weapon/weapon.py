class WeaponClass:
    N = ""          # String
    C = []          # String
    BD = []         # Integer
    MDSc = []       # Float
    RDSc = []       # Float
    EDSc = []       # Float
    MHPSc = []      # Float
    ASc = []        # Float
    ESc = []        # Float
    RSc = []        # Float
    ASSc = []       # Float
    SSc = []        # Float
    LSc = []        # Float
    AS = []         # Float
    CD = []         # Float
    CC = []         # Float
    R = []          # Integer
    K = []          # Integer
    L = []          # Float
    SE = []         # String
    BP = []         # Integer

    # Print
    def __str__(self):
	    return f"Name: {self.N}\nClass: {self.C}\nBase Damage: {self.BD}\nMelee Damage Scaling: {self.MDSc}\nRanged Damage Scaling: {self.RDSc}\nElemental Damage Scaling: {self.EDSc}\nMax HP Scaling: {self.MHPSc}\nArmor Scaling: {self.ASc}\nEngineering Scaling: {self.ESc}\nRange Scaling: {self.RSc}\nAttack Speed Scaling: {self.ASSc}\nSpeed Scaling: {self.SSc}\nLevel Scaling: {self.LSc}\nAttack Speed: {self.AS}\nCrit Damage: {self.CD}\nCrit Chance: {self.CC}\nRange: {self.R}\nKnockback: {self.K}\nLifesteal: {self.L}\nSpecial Effects: {self.SE}\nBase Price: {self.BP}\n"

    # N
    def setN(cls, newN):
        cls.N = newN
    def clearN(cls):
        cls.N = ""
    def getN(cls):
        return cls.N
    
    # C
    def setC(cls, newC):
        cls.C = newC

    def clearC(cls):
        cls.C = []
    
    def getC(cls):
	    return cls.C
    
    # BD
    def setBD(cls, newBD):
        cls.BD = newBD

    def clearBD(cls):
        cls.BD = []
    
    def getBD(cls):
	    return cls.BD
    
    # MDSc
    def setMDSc(cls, newMDSc):
        cls.MDSc = newMDSc

    def clearMDSc(cls):
        cls.MDSc = []
    
    def getMDSc(cls):
	    return cls.MDSc
    
    # RDSc
    def setRDSc(cls, newRDSc):
        cls.RDSc = newRDSc

    def clearRDSc(cls):
        cls.RDSc = []
    
    def getRDSc(cls):
	    return cls.RDSc
    
    # EDSc
    def setEDSc(cls, newEDSc):
        cls.EDSc = newEDSc

    def clearEDSc(cls):
        cls.EDSc = []
    
    def getEDSc(cls):
	    return cls.EDSc
    
    # MHPSc
    def setMHPSc(cls, newMHPSc):
        cls.MHPSc = newMHPSc

    def clearMHPSc(cls):
        cls.MHPSc = []
    
    def getMHPSc(cls):
	    return cls.MHPSc

    # ASc
    def setASc(cls, newASc):
        cls.ASc = newASc

    def clearASc(cls):
        cls.ASc = []
    
    def getASc(cls):
	    return cls.ASc
    
    # ESc
    def setESc(cls, newESc):
        cls.ESc = newESc

    def clearESc(cls):
        cls.ESc = []
    
    def getESc(cls):
	    return cls.ESc
    
    # RSc
    def setRSc(cls, newRSc):
        cls.RSc = newRSc

    def clearRSc(cls):
        cls.RSc = []
    
    def getRSc(cls):
	    return cls.RSc
    
    # ASSc
    def setASSc(cls, newASSc):
        cls.ASSc = newASSc

    def clearASSc(cls):
        cls.ASSc = []
    
    def getASSc(cls):
	    return cls.ASSc
    
    # SSc
    def setSSc(cls, newSSc):
        cls.SSc = newSSc

    def clearSSc(cls):
        cls.SSc = []
    
    def getSSc(cls):
	    return cls.SSc

    # LSc
    def setLSc(cls, newLSc):
        cls.LSc = newLSc

    def clearLSc(cls):
        cls.LSc = []
    
    def getLSc(cls):
	    return cls.LSc
    
    # Set Scaling based on scType
    def addSc(cls, scType, newSc):
        match scType:
            case 0:
                cls.LSc.append(newSc)
                pass
            case 1:
                cls.MDSc.append(newSc)
                pass
            case 2:
                cls.RDSc.append(newSc)
                pass
            case 3:
                cls.EDSc.append(newSc)
                pass
            case 4:
                cls.MHPSc.append(newSc)
                pass
            case 5:
                cls.ASc.append(newSc)
                pass
            case 6:
                cls.ESc.append(newSc)
                pass
            case 7:
                cls.RSc.append(newSc)
                pass
            case 8:
                cls.ASSc.append(newSc)
                pass
            case 9:
                cls.SSc.append(newSc)
                pass
    
    # Clear all Scaling
    def clearSc(cls):
        cls.clearMDSc()
        cls.clearRDSc()
        cls.clearEDSc()
        cls.clearMHPSc()
        cls.clearASc()
        cls.clearESc()
        cls.clearRSc()
        cls.clearASSc()
        cls.clearSSc()
        cls.clearLSc()

    # AS
    def setAS(cls, newAS):
        cls.AS = newAS

    def clearAS(cls):
        cls.AS = []
    
    def getAS(cls):
	    return cls.AS
    
    # CD
    def setCD(cls, newCD):
        cls.CD = newCD

    def clearCD(cls):
        cls.CD = []
    
    def getCD(cls):
	    return cls.CD
    
    # CC
    def setCC(cls, newCC):
        cls.CC = newCC

    def clearCC(cls):
        cls.CC = []
    
    def getCC(cls):
	    return cls.CC
    
    # R
    def setR(cls, newR):
        cls.R = newR

    def clearR(cls):
        cls.R = []
    
    def getR(cls):
	    return cls.R
    
    # K
    def setK(cls, newK):
        cls.K = newK

    def clearK(cls):
        cls.K = []
    
    def getK(cls):
	    return cls.K
    
    # L
    def setL(cls, newL):
        cls.L = newL

    def clearL(cls):
        cls.L = []
    
    def getL(cls):
	    return cls.L
    
    # SE
    def setSE(cls, newSE):
        cls.SE = newSE

    def clearSE(cls):
        cls.SE = []
    
    def getSE(cls):
	    return cls.SE
    
    # BP
    def setBP(cls, newBP):
        cls.BP = newBP

    def clearBP(cls):
        cls.BP = []
    
    def getBP(cls):
	    return cls.BP
