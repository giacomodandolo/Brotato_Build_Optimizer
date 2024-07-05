from bs4 import BeautifulSoup
import requests
import csv
from Weapons.weapon import *

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

weaponObj = None
allWeapons = []

# Obtain informations
def obtainWeapons():
    for tdIndex, TD in enumerate(allTDs):
        relativePosition = tdIndex % MOD_WEAPONS
        values = allTDs[tdIndex].text
        
        match relativePosition:
            # N
            case 0:
                weaponObj = WeaponClass()
                weaponObj.setN(values)
                pass
            # C
            case 1:
                valuesSplit = values.split(", ")
                weaponObj.setC(valuesSplit)
                pass
            # BD, xSc
            case 2:
                valuesSplit = values.split("\n")
                valueSet = []
                weaponObj.clearSc()
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
                                weaponObj.addSc(j, float(scalingSplit[counter])/100)
                                counter = counter + 1
                            else:
                                weaponObj.addSc(j, -1)
                        else:
                            weaponObj.addSc(j, -1)
                weaponObj.setBD(valueSet)
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
                weaponObj.setAS(valueSet)
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
                weaponObj.setCD(valueSetCD)
                weaponObj.setCC(valueSetCC)
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
                weaponObj.setR(valueSet)
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
                weaponObj.setK(valueSet)
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
                weaponObj.setL(valueSet)
                pass
            # SE
            case 9:
                weaponObj.setSE(values)
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
                weaponObj.setBP(valueSet)
                allWeapons.append(weaponObj)
                pass
            # Not Important TDs
            case _:
                pass

# Translate into CSV
def obtainCSV():
    csvFile = open('Brotato_Data\CSV\weapons.csv', 'w')
    csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
    
    for weaponObj in allWeapons:
        csvRow = weaponObj.obtainWeaponCSV()
        csvWriter.writerow(csvRow)

    csvFile.close()

# Translate into MD
def obtainMD():
    for item in allWeapons:
        item.obtainWeaponMD()

