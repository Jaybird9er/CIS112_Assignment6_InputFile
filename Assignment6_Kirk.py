"""
Author: Jamey Kirk
Date: 03/28/2021
Assignment: 6
Description: User creates txt file and inputs text
"""

import re

def startABCorUS (fileName):
    """ 
    should begin with alphabetical or "_" characters
    """
    groupName = re.search('(^[a-z]|[A-Z]|\_)', fileName)
    if groupName:
        return True
    else:
        return "The first character of the file name must be an alphabetical letter or '_'."

def hasABCorDigitsorUS (fileName):
    """ 
    name consists of digits, or alphabetical or "_" characters
    """
    spaceCheck = re.sub('\s+', '', fileName)
    groupName = re.fullmatch('([a-z0-9A-Z_\.]*)', fileName)
    if len(spaceCheck) != len(fileName):
        return "Filename can contain only digits, letters, or '_'."
    elif groupName:
        return True
    else:
        return "Filename can contain only digits, letters, or '_'."

def noSpecialChar (fileName):
    """ 
    does not contain any special characters
    """
    pass

def hasExtension (fileName):
    """ 
    filename needs to have an extension (any extension)
    """
    dotCheck = re.findall('\.', fileName)
    #len(dotCheck) > 1
    pass

fileName = input("Please enter a filename: ")
#print(startABCorUS(fileName))
print(hasABCorDigitsorUS(fileName))
#dotCheck = re.findall('\.', fileName)
#print(len(dotCheck))