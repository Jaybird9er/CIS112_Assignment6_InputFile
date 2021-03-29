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
        return groupName.group()
    else:
        return "The first character of the file name must be an alphabetical letter or '_'."

def hasABCorDigitsorUS (fileName):
    """ 
    name consists of digits, or alphabetical or "_" characters
    """
    pass

def noSpecialChar (fileName):
    """ 
    does not contain any special characters
    """
    pass

def hasExtension (fileName):
    """ 
    filename needs to have an extension (any extension)
    """
    pass

fileName = input("Please enter a filename: ")
#print(startABCorUS(fileName))

