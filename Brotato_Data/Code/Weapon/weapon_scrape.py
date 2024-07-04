from bs4 import BeautifulSoup
import requests
from weapon import WeaponClass

MOD_WEAPONS = 12
SCALING_TYPES = ["Level", "Melee Damage", "Ranged Damage", "Elemental Damage", "Max HP", "Armor", "Engineering", "Range", "Attack Speed", "Speed"]

# Request the Weapons page of the wiki
requestPage = requests.get("https://brotato.wiki.spellsandguns.com/Weapons")

# Parse the HTML Page
requestSoup = BeautifulSoup(requestPage.text, "html.parser")

# Obtain all TDs elements
allTables = requestSoup.findAll("table")
allTDs = allTables[0].findAll("td")
allTDs = allTDs + allTables[1].findAll("td")

# Obtain informations
weapon = None
allWeapons = []
for tdIndex, TD in enumerate(allTDs):
    relativePosition = tdIndex % MOD_WEAPONS
    values = allTDs[tdIndex].text
    
    match relativePosition:
        # N
        case 0:
            weapon = WeaponClass()
            weapon.setN(values)
            pass
        # C
        case 1:
            valuesSplit = values.split(", ")
            weapon.setC(valuesSplit)
            pass
        # BD, xSc
        case 2:
            valuesSplit = values.split("\n")
            valueSet = []
            weapon.clearSc()
            for i, item in enumerate(valuesSplit[1:5]):
                itemSplit = item.split("(")
                counter = 0
                if(item != "-" and item != " -"):
                    scalingSplit = itemSplit[1].split("%")
                    if("x" in itemSplit[0]):
                        itemSplitSpec = itemSplit[0].split("x")
                        itemSplit[0] = int(itemSplitSpec[0])*int(itemSplitSpec[1])
                    valueSet.append(int(itemSplit[0]))
                else:
                    valueSet.append(-1)
                for j, itemS in enumerate(SCALING_TYPES):
                    if(item != "-" and item != " -"):
                        if(itemS == "Level"):
                            allScaling = allTDs[tdIndex].find("img", attrs={"alt": itemS + ".png"})
                        else:
                            allScaling = allTDs[tdIndex].find("a", attrs={"title": itemS})
                        if(allScaling != None):
                            weapon.addSc(j, float(scalingSplit[counter])/100)
                            counter = counter + 1
                        else:
                            weapon.addSc(j, -1)
                    else:
                        weapon.addSc(j, -1)
            weapon.setBD(valueSet)
            pass
        # AS
        case 3:
            valueSplit = values.split("\n")
            valueSet = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
    	            valueSet.append(float(item.strip("s")))
                else:
                    valueSet.append(-1)
            weapon.setAS(valueSet)
            pass
        # CD, CC
        case 5:
            valueSplit = values.split("\n")
            valueSetCD = []
            valueSetCC = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
                    valueParSplit = item.split("(")
                    valueSetCD.append(float(valueParSplit[0].strip(" x")))
                    valueSetCC.append(float(valueParSplit[1].strip("%) ")))
                else:
                    valueSetCD.append(-1)
                    valueSetCC.append(-1)    
            weapon.setCD(valueSetCD)
            weapon.setCC(valueSetCC)
            pass
        # R
        case 6:
            valueSplit = values.split("\n")
            valueSet = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
    	            valueSet.append(int(item))
                else:
                    valueSet.append(-1)
            weapon.setR(valueSet)
            pass
        # K
        case 7:
            valueSplit = values.split("\n")
            valueSet = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
                    valueSet.append(int(item))
                else:
                    valueSet.append(-1)
            weapon.setK(valueSet)
            pass
        # L
        case 8:
            valueSplit = values.split("\n")
            valueSet = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
                    valueSet.append(float(item.strip("%"))/100)
                else:
                    valueSet.append(-1)
            weapon.setL(valueSet)
            pass
        # SE
        case 9:
            weapon.setSE(values)
            pass
        # BP
        case 10:
            valueSplit = values.split("\n")
            valueSet = []
            for i, item in enumerate(valueSplit[1:5]):
                if(item != "-" and item != " -"):
                    valueSet.append(int(item))
                else:
                    valueSet.append(-1)
            weapon.setBP(valueSet)
            allWeapons.append(weapon)
            pass
        # Not Important TDs
        case _:
            pass

for item in allWeapons:
    print(item)