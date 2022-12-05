import numpy as np

input = np.loadtxt("Inputs/Day 3.txt", dtype='str')
# loads the input file as strings

def checkCommonChars(strIn):    # splits the string into halves and checks for common characters between the two
    output = []
    i = 0
    while i < len(strIn):
        firstHalf = str(strIn[i])[0:int(len(strIn[i]) / 2)]
        secondHalf = str(strIn[i])[int(len(strIn[i]) / 2):len(strIn[i])]
        output = np.append(output, list(set(firstHalf) & set(secondHalf)))
        i = i + 1

    return output   # returns the common characters


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
    return output   # transforms the characters first to their ASCII value and then to their assigned value


print(createOut(comChar).sum())
