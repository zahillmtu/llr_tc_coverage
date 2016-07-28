""" Script to determine if all the LLRs that have been modified
are covered within a Test Case.
"""

__author__  = "Zachary Hill"
__email__   = "zachary.hill@psware.com"

import os # needed for the os.walk function
import re
import sys

from Tkinter import Tk
from tkFileDialog import askdirectory

def find_require_ln(fileName):
    """Method to find the line number of the location of 'REQUIREMENTS'
    in the text documents

    If no 'REQUIREMENTS' is found will return -1, otherwise returns line number
    """

    with open(fileName, 'r') as file:
        for num, line in enumerate(file, 1):
            if 'REQUIREMENTS' in line.upper():
                return num
    return -1 # if here no requirements found


def main():
    """Script designed to determine if all modified LLRs
    are covered within a test case.
    """

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    rootDir = askdirectory() # show an "Open" dialog box and return the path to the selected file
    print('Head of tree travesal selected %s' % rootDir)

    # Traverse the tree
    for dirName, subdirList, fileList in os.walk(rootDir):
        # Ignore hidden files and directories
        fileList = [f for f in fileList if not f[0] == '.']
        subdirList[:] = [d for d in subdirList if not d[0] == '.']

        print('Found directory: %s' % dirName)
        for file in fileList:
            if file.endswith('.txt') and file.startswith('TC'):
                # Do stuff here


if __name__ == '__main__':
    main()
