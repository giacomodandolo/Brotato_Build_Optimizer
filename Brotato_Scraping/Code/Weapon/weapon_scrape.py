from bs4 import BeautifulSoup
import requests
from weapon import WeaponClass

MOD_WEAPONS = 12

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

    match relativePosition:
        # N
        case 0:
            weapon = WeaponClass()
            values = allTDs[tdIndex].text
            weapon.setN(values)
            pass
        # C
        case 1:
            values = allTDs[tdIndex].text
            valuesSplit = values.split(", ")
            weapon.setC(valuesSplit)
            pass
        # BD, xSc
        case 2:

            pass
        # AS
        case 3:
            values = allTDs[tdIndex].text
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
            values = allTDs[tdIndex].text
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
            values = allTDs[tdIndex].text
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
            values = allTDs[tdIndex].text
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
            values = allTDs[tdIndex].text
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
            
            pass
        # BP
        case 10:
            values = allTDs[tdIndex].text
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
