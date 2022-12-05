import numpy as np
import pandas as pd

input = np.loadtxt("Inputs/Day 3.txt", dtype='str')


# loads the input file as strings
def checkCommonCharsInGroup(strIn):  # checks for common characters between groups of three
    output = []
    i = 0
    while i < len(strIn):
        output = np.append(output, list(set(strIn[i]) & set(strIn[i + 1]) & set(strIn[i + 2])))
        i = i + 3

    return output   # returns the common characters


comChar = checkCommonCharsInGroup(input)

print(comChar)


def createOut(inp):
    i = 0
    output = []
    while i < len(inp):
        if inp[i].isupper() == True:
            output = np.append(output, ord(inp[i]) - 38)
        elif inp[i].isupper() == False:
            output = np.append(output, ord(inp[i]) - 96)
        i = i + 1
    return output  # transforms the characters first to their ASCII value and then to their assigned value


print(createOut(comChar).sum())
