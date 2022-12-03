import pandas as pd

input = pd.read_csv("Inputs/Day 2.txt", names=['opp', 'oc'], sep=' ')

print (input)


def winning (opp, oc):
    signVal = 0
    outcome = 0
    if oc == 'X':
        outcome = 0
        if opp == 'A':
            signVal = 3
        elif opp == 'B':
            signVal = 1
        elif opp == 'C':
            signVal = 2
    if oc == 'Y':
        outcome = 3
        if opp == 'A':
            signVal = 1
        elif opp == 'B':
            signVal = 2
        elif opp == 'C':
            signVal = 3
    if oc == 'Z':
        outcome = 6
        if opp == 'A':
            signVal = 2
        elif opp == 'B':
            signVal = 3
        elif opp == 'C':
            signVal = 1

    return outcome+signVal


i = 0
output = 0
while i < len(input):
    output = output + winning(input.at[i, 'opp'], input.at[i, 'oc'])
    i = i+1

print(output)
