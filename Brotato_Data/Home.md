#scraping 
In the following documents, we will explain the methodology for Web Scraping of each listed page of the relative [Brotato Wiki](https://brotato.wiki.spellsandguns.com/Brotato_Wiki|).
Specifically, we shall explain the following points:
- the necessary informations and the relative data structure;
- the Web Scraping strategy specific to the Wiki Page;
- how to translate the data structure in CSV file format to recover the data structure in future scripts;
- how to translate the data structure in Obsidian file format to graph and find the correlations.
# BeautifulSoup
For the Web Scraping we will use the BeautifulSoup python libraries, designed specifically for this purpose.
We will also use the requests python library, which will be used to receive the full page used for each instance.
Let's see some of the functions we will use in this project.
## Obtain the HTML code of the webpage
```python
# Imported libraries
from bs4 import BeautifulSoup 
import requests

# Request a webpage
requestedPage = requests.get("https://example.it")

# Use BeautifulSoup to parse the HTML
requestedSoup = BeautifulSoup(requestedPage.text, "html.parser")
```
## Obtain all HTML blocks defined by a tag
```python
# Obtain all blocks defined by a certain tag 
tag = "requestedTag"
allBlocks = requestedSoup.findAll(tag)

# If the specified tag needs a certain attribute
attributeName = "requestedAttributeName"
attributeValue = "requestedAttributeValue"
allBlocksAttr = requestedSoup.findAll(tag, attrs={attributeName: attributeValue})
```
## Obtain a tag inside another tag 
```python
# Obtain the contents of tag2 inside tag1
extractedElement = allBlocks.tag1.tag2
```
## Obtain the contents defined by a tag
The contents of a tag are defined as an array, where each element is defined by a tag.
```python
# Obtain the contents of an element 
extractedContent = extractedElement.contents

# Obtain the text contained in an element
extractedContent = extractedElement.text
```
## Obtain the value of an attribute defined by a tag
```python
# Obtain the value of a certain attribute of a tag
attribute = "requestedAttribute"
extractedAttributeValue = extractedElement[attribute]
```
# CONTENTS
	[[Weapons]]
	[[Items]]
	[[Characters]]
