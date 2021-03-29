"""
Author: Jamey Kirk
Date: 03/28/2021
Assignment: 6
Description: User creates txt file and inputs text
"""

import os
import re

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
    charsCheck = re.search('(\.\W|\_*)$', fileName)
    extCheck = re.search('(\.[a-z]*)$', fileName)
    if len(dotCheck) != 1:
        print("File name needs to have an extension.")
    elif len(charsCheck.group()) > 0:
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

# cwdPath = pathlib.Path.cwd()
# print(cwdPath)

# test = "test"
# print(enterLine(test))

## outer loop confirms whether user wants to create another file

newFile = True
while (newFile):
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
    # believe file must close to write before printing
    fHand.close()
    print("=============================")
    fHand = open(fileName)
    for line in fHand:
        print(line, end='')
    print("=============================")
    fHand.close()

    ## confirm if user wants to make a new file (outer loop test)
    anotherFile = input("Do you want to create another file? (Y/N) ")
    if anotherFile == 'n' or anotherFile == 'N':
            newFile = False

print("Thank you for playing!")
