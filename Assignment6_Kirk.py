"""
Author: Jamey Kirk
Date: 03/28/2021
Assignment: 6
Description: User creates txt file and inputs text
"""

import os
import re
import pathlib

def checkStart (fileName):
    """ 
    should begin with alphabetical or "_" characters
    """
    groupName = re.search('^([a-z]|[A-Z]|\_)', fileName)
    if groupName:
        return True
    else:
        print("The first character of the file name must be an alphabetical letter or '_'.")

def charCheck (fileName):
    """ 
    name consists of digits, or alphabetical or "_" characters
    """
    spaceCheck = re.sub('\s+', '', fileName)
    groupName = re.fullmatch('([a-z0-9A-Z_\.]*)', fileName)
    if len(spaceCheck) != len(fileName):
        print("Filename can contain only digits, letters, or '_'.")
    elif groupName:
        return True
    else:
        print("Filename can contain only digits, letters, or '_'.")

def hasExtension (fileName):
    """ 
    filename needs to have an extension (any extension)
    """
    dotCheck = re.findall('\.', fileName)
    extCheck = re.search('(\.[a-z]*)$', fileName)
    if len(dotCheck) != 1:
        print("File name needs to have an extension.")
    elif len(extCheck.group()) < 4 or len(extCheck.group()) > 5:
        print("File name needs to have an extension.")
    else:
        return True

def enterLine (strLine):
    """
    take input and append '\n'
    """
    return strLine + '\n'

cwdPath = pathlib.Path.cwd()
print(cwdPath)

test = "test"
print(enterLine(test))

## outer loop confirms whether user wants to create another file

## 1st inner loop evaluates file name and terminates if all conditions are true
fileName = input("Please enter a filename: ")
testFileName = True
while (testFileName):
    if checkStart(fileName) and charCheck(fileName) and hasExtension(fileName):
        testFileName = False
    else:
        fileName = input("Plese enter a proper filename: ")

## file is created with 1st inner loop file name
fHand = open(fileName, mode = 'w')
isWriting = True

## 2nd inner loop enters strings into file
while (isWriting):
    strLine = input("Please enter a sentence: ")
    fHand.write(enterLine(strLine))
    keepWriting = input("Do you want to add more lines? (Y/N) ")
    if keepWriting == 'n' or keepWriting == 'N':
        isWriting = False

print("This is what's entered into file ", fileName, ".", sep="")
fHand.close()
print("=============================")
fHand = open(fileName)
for line in fHand:
    print(line, end='')
print("=============================")
fHand.close()
