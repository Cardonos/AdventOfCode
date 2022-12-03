import numpy as np
import pandas as pd

input = np.loadtxt("Inputs/Day 3.txt", dtype='str')

print(input)


# print(list(set(input[0]) & set(input[1])))

# print(str(input[1])[0:4], int(len(input[1])/2))

def checkCommonCharsInGroup(strIn):
    output = []
    i = 0
    while i < len(strIn):
        output = np.append(output, list(set(strIn[i]) & set(strIn[i+1]) & set(strIn[i+2])))
        i = i + 3

    return output


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
    return (output)


print(createOut(comChar).sum())
