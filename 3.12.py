import numpy as np
import pandas as pd

input = np.loadtxt("Inputs/Day 3.txt", dtype='str')

print(input)


# print(list(set(input[0]) & set(input[1])))

# print(str(input[1])[0:4], int(len(input[1])/2))

def checkCommonChars(strIn):
    output = []
    i = 0
    while i < len(strIn):
        firstHalf = str(strIn[i])[0:int(len(strIn[i]) / 2)]
        secondHalf = str(strIn[i])[int(len(strIn[i]) / 2):len(strIn[i])]
        output = np.append(output, list(set(firstHalf) & set(secondHalf)))
        i = i + 1

    return output


comChar = checkCommonChars(input)


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
