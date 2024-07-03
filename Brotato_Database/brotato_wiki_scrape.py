#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

MOD_INDEX = 12

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
weapons_page = requests.get("https://brotato.wiki.spellsandguns.com/Weapons")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
weapons_soup = BeautifulSoup(weapons_page.text, 'html.parser')

weaponsPageTable = weapons_soup.findAll('table')
weaponsPage = weaponsPageTable[0].findAll('td')

items = {
    "Name": "", 
    "Class": [], 
    "Damage": [], 
    "Attack_Speed": [], 
    "Crit": [], 
    "Range": [], 
    "Knockback": [], 
    "Lifesteal": [], 
    "Special effects": ""
}

indexArray = []
nameFound = []

index = 0
for cell in weaponsPage:
    currIndex = index % MOD_INDEX
    if(cell != None):
        match currIndex:
            case 0: # Name
                if cell.div != None:
                    temp = cell.div.div.a['title']
                    if temp not in nameFound:
                        items["Name"] = temp
                        nameFound.append(temp)
                    else:
                        index = index + 11
            case 1: # Class
                if cell.a != None:
                    temp = cell.findAll('a')
                    for t in temp:
                        items["Class"].append(t['title'])
            case 2: # Damage
                if cell.p != None:
                    temp = cell.findAll('span')
                    for t in temp:
                        items["Damage"].append(t)
                pass
            case 3: # Attack Speed
                if cell.p != None:
                    temp = cell.findAll("span")
                    for t in temp:
                        items["Attack_Speed"].append(t.contents[0])
                pass
            case 5: # Crit Damage/Chance
                if cell.p != None:
                    temp = cell.p.span.contents[0]
                    items["Crit"] = temp
                pass
            case 6: # Range
                if cell.p != None:
                    temp = cell.p.span.contents
                    for t in temp:
                        if('0' < t < '9'):
                            t = int(t)
                        items["Range"] = t
                pass
            case 7: # Knockback
                if cell.p != None:
                    temp = cell.p.span.contents
                    for t in temp: 
                        if('0' < t < '9'):
                            t = int(t)
                        items["Knockback"] = t
                pass
            case 8: # Lifesteal
                if cell.p != None:
                    temp = cell.p.span.contents
                    items["Lifesteal"] = temp
                pass
            case 9: # Special Effects
                if cell.p != None:
                    temp = cell.p.contents
                    items["Special effects"] = temp
                indexArray.append(items.copy())
            case _:
                pass
    index = index + 1

for row in indexArray:
    print("\n")
    print(row)