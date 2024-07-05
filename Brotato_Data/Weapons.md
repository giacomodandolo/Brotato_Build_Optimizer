#scraping 
# GENERAL NOTES
In this section we will list the general attributes about weapons.
Weapons are the primary damage dealers. They can be Melee or Ranged. 
## Rarity
Weapons come in 4 different tiers. Some weapons have a minimum tier that they can appear as. 
If you have two identical weapons of the same tier, you can combine them into one weapon of one higher tier.
The four tiers are:
- Tier 1 (Common);
- Tier 2 (Uncommon);
- Tier 3 (Rare);
- Tier 4 (Legendary).
## Damage Types
Each weapon scales with one or more of the stats shown in the table. Each stat is described by an Identifier (ID), which is abbreviated by a Short ID in the documentation.

| **ID**       | Melee Damage | Ranged Damage | Elemental Damage | Max HP | Armor | Engineering | Range | Attack Speed | Speed | Level |
| ------------ | :----------: | :-----------: | :--------------: | :----: | :---: | :---------: | :---: | :----------: | :---: | :---: |
| **SHORT ID** |      MD      |      RD       |        ED        |  MHP   |   A   |      E      |   R   |      AS      |   S   |   L   |

---
# DATA
In this section we will list the characteristics needed to memorize all weapons and the data structure.
## Necessary informations
Every scaling stat, attack speed, crit damage, crit chance, range, knockback, lifesteal and base price value are based on the 4 tiers of the weapon.
Each weapon is fully defined by the informations shown in the following table, in which x identifies each type of damage.

| **NAME**       | Name | Class | Base Damage | x Scaling | Attack Speed | Crit Damage | Crit Chance | Range | Knockback | Lifesteal | Special Effects | Base Price |
| -------------- | :--: | :---: | :---------: | :-------: | :----------: | :---------: | :---------: | :---: | :-------: | :-------: | :-------------: | :--------: |
| **SHORT NAME** |  N   |   C   |     BD      |    xSc    |      AS      |     CD      |     CC      |   R   |     K     |     L     |       SE        |     BP     |
## Data Structure
To define the needed data structure, we must first define the base class for each single weapon.
```python
class WeaponClass:
    N = ""          # String
    C = []          # String
    BD = []         # Integer
    MDSc = []       # Float
    RDSc = []       # Float
    EDSc = []       # Float
    MHPSc = []      # Float
    ASc = []        # Float
    ESc = []        # Float
    RSc = []        # Float
    ASSc = []       # Float
    SSc = []        # Float
    LSc = []        # Float
    AS = []         # Float
    CD = []         # Float
    CC = []         # Float
    R = []          # Integer
    K = []          # Integer
    L = []          # Float
    SE = ""         # String
    BP = []         # Integer
```
In this class we can create a print function, and for each attribute a set, clear and get functions. 
Let's see an example for the attribute N and the attribute C.
```python
# Print
def __str__(self):
        return f"Name: {self.N}\nClass: {self.C}\nBase Damage: {self.BD}\nMelee Damage Scaling: {self.MDSc}\nRanged Damage Scaling: {self.RDSc}\nElemental Damage Scaling: {self.EDSc}\nArmor Scaling: {self.ASc}\nEngineering Scaling: {self.ESc}\nRange Scaling: {self.RSc}\nAttack Speed Scaling: {self.ASSc}\nLevel Scaling: {self.LSc}\nAttack Speed: {self.AS}\nCrit Damage: {self.CD}\nCrit Chance: {self.CC}\nRange: {self.R}\nKnockback: {self.K}\nLevel: {self.L}\nSpecial Effects: {self.SE}\nBase Price: {self.BP}\n"

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
```
We can create an object using a python class constructor. Each object can be inserted into an array in which all the weapons will be contained.
Let's see an example.
```python
# Creation of the object
weapon = WeaponClass()

# Inserting weapon in the array
weapons.append(weapon)
```
---
# WEB SCRAPING
All data shall be extracted from the [Brotato Wiki page for Weapons](https://brotato.wiki.spellsandguns.com/Weapons).
You can observe that the data needed to get extracted is all in the tags `<td>`, in intervals of 12 per item, since there are 12 columns in the wiki. So, the first thing to do is to obtain all `<td>` elements.
```python
allTDs = requestSoup.findAll("td")
```
After this, we need to define how to obtain every information needed.
Since it is in intervals of 12 `<td>` per item, we can define a constant `MOD_WEAPONS = 12`, which shall be used to obtain the appropriate index. We shall define the relative position as the position of the td relative to the row, which can have position 0 to 11.
```python
relativePosition = tdIndex % MOD_WEAPONS
```
All of the following code is gonna be inside the function `obtainWeapons()`.
## Name
In relative position 0, we can obtain the name by using the following instruction:
```python
values = allTDs[tdIndex].text
```
## Class
In relative position 1, we can obtain the classes by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction can obtain a string with multiple classes, we need to split the string using the following instruction:
```python
valuesSplit = classes.split(", ")
```
## Base Damage and scalings
In relative position 2, we can obtain the base damage and the scalings using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple base damage and scaling values, we need to split the string accordingly.
```python
valueSplit = values.split("\n")
```
The first element are the values of the base damage. We need to cast each value into integers, considering values that are not numbers as -1. 
```python
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
```
The second element is the values of the various scalings. We need to differentiate each type of scaling and giving its appropriate value, cast into floats after stripping the "%" character, considering values that are not numbers as -1. This shall all happen inside the first for.
```python
	for j, itemS in enumerate(SCALING_TYPES):
		if(item != "-" and item != " -"):
            if(itemS == "Level"):
				allScaling = allTDs[tdIndex].find("img", attrs={"alt": itemS + ".png"})
			else:
				allScaling = allTDs[tdIndex].find("a", attrs={"title":itemS})
			if(allScaling != None):
				weapon.addSc(j, float(scalingSplit[counter])/100)
				counter = counter + 1
			else:
				weapon.addSc(j, -1)
		else:
			weapon.addSc(j, -1)
```
## Attack Speed
In relative position 3, we can obtain the attack speed values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple attack speed values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to cast each value into floats after stripping the "s" character, considering values that are not numbers as -1.
```python
valueSet = []
for i, item in enumerate(valueSplit[1:5]):
	if(item != "-" and item != " -"):
		valueSet.append(float(item.strip("s")))
	else:
		valueSet.append(-1)
```
## Crit Damage and Crit Chance
In relative position 5, we can obtain the crit damage and crit chance values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple crit damage and crit chance values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to divide the values into crit damage and crit chance, cast each value into floats after stripping the " x" character for crit damage strings and the "%) " character for crit chance, considering values that are not numbers as -1.
```python
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
```
## Range
In relative position 6, we can obtain the range values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple range values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to cast each value into integers, considering values that are not numbers as -1.
```python
valueSet = []
for i, item in enumerate(valueSplit[1:5]):
	if(item != "-" and item != " -"):
		valueSet.append(int(item))
	else:
		valueSet.append(-1)
```
## Knockback
In relative position 7, we can obtain the knockback values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple knockback values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to cast each value into integers, considering values that are not numbers as -1.
```python
valueSet = []
for i, item in enumerate(valueSplit[1:5]):
	if(item != "-" and item != " -"):
		valueSet.append(int(item))
	else:
		valueSet.append(-1)
```
## Lifesteal
In relative position 8, we can obtain the lifesteal values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple lifesteal values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to cast each value into floats after stripping the "%" character and then dividing by 100, considering values that are not numbers as -1.
```python
valueSet = []
for i, item in enumerate(valuesSplit[1:5]):
	if(item != "-" and item != " -"):
		valueSet.append(float(item.strip("%"))/100)
	else:
		valueSet.append(-1)
```
## Special Effects
In relative position 9, we can obtain the special effects value by using the following instruction:
```python
values = allTDs[tdIndex].text
```
## Base Price
In relative position 10, we can obtain the base price values by using the following instruction:
```python
values = allTDs[tdIndex].text
```
Since this instruction obtains a string with multiple base price values, we need to split the string.
```python
valueSplit = values.split("\n")
```
After this, we need to cast each value into integers, considering values that are not numbers as -1.
```python
valueSet = []
for i, item in enumerate(valuesSplit[1:5]):
	if(item != "-" and item != " -"):
		valueSet.append(float(item.strip("%"))/100)
	else:
		valueSet.append(-1)
```
---
# CSV FORMAT
To translate into CSV format, we must first notice how the Class is formed by an irregular quantity of elements. Because of this, we shall use `;` to separate these values in the CSV format.
We must first define a function to obtain a CSV format array for a single weapon.
```python
def obtainWeaponCSV(weapon):
	dictWeapon = weapon.__dict__
	returningArray = []

    for keyD, valueD in dictWeapon.items():
		string = ""
		if(type(valueD) is str):
			returningArray.append(valueD)
		else:
			for i, valueW in enumerate(valueD):
				if(type(valueW) is str):
					if(i == len(valueD) - 1):
						string = string + valueW
						returningArray.append(string)
					else:
						string = string + valueW + ";"
				else:
					returningArray.append(valueW)
	return returningArray
```
Using the defined function, we shall create another one to format all the weapons.
```python
def obtainCSV():
	csvFile = open('Brotato_Data\CSV\weapons.csv', 'w')
	csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC)
	for weapon in allWeapons:
		csvRow = obtainWeaponCSV(weapon)
		csvWriter.writerow(csvRow)
	csvFile.close()
```
---
# MD FORMAT
Each weapon shall have a dedicated page with all the informations associated with it.
To translate into MD format, we must define the structure of the whole page. 
At the beginning of each Weapon page, there are gonna be the Class and Special Effects properties. After this, there's gonna be the identifying hashtag #weapon. 
Ultimately, all the attributes will be put into a table, defining the name of the attribute and the values from tiers 1 to 4.
To define this structure, we must define a function to create it for a single weapon.
```python
def obtainWeaponMD(weapon):
	dictWeapons = weapon.__dict__
	counter = 1
	fileName = "Brotato_Data\MD\Weapons\\" + dictWeapons["N"] + ".md"
	mdFile = open(fileName, "w")
	
	mdFile.write("---\n" + ALL_ATTRIBUTES[counter] + ":\n")
	for item in dictWeapons["C"]:
		mdFile.write("- " + item + "\n")
	counter = counter + 1
	
	mdFile.write(ALL_ATTRIBUTES[counter] + ": " + dictWeapons["SE"] + "\n---\n#weapon\n\n")
	counter = counter + 1
	for tier in TIERS:
		mdFile.write("| " + tier)
	mdFile.write(" |\n")
	for tier in TIERS:
		mdFile.write("| :---: ")
	mdFile.write(" |\n")

	for key, item in dictWeapons.items():
		if(key != "N" and key != "C" and key != "SE"):
			mdFile.write("| " + ALL_ATTRIBUTES[counter])
			counter = counter + 1
			if(type(item) is str):
				mdFile.write(item)
			else:
				for i, itemS in enumerate(item):
					mdFile.write(" | " + str(itemS) + " ")
					if(i != len(item) - 1):
						mdFile.write(" ")
			mdFile.write(" |\n")
			
    mdFile.close()
```
Using the defined function, we shall create another one to format all the weapons.
```python
def obtainMD():
    for item in allWeapons:
        obtainWeaponMD(item)
```