import pandas as pd

input = pd.read_csv("Inputs/Day 2.txt", names=['opp', 'me'], sep=' ')

print (input)


def winning (opp, me):
    signVal = 0
    outcome = 0
    if me == 'X':
        signVal = 1
        if opp == 'A':
            outcome = 3
        elif opp == 'C':
            outcome = 6
    if me == 'Y':
        signVal = 2
        if opp == 'B':
            outcome = 3
        elif opp == 'A':
            outcome = 6
    if me == 'Z':
        signVal = 3
        if opp == 'C':
            outcome = 3
        elif opp == 'B':
            outcome = 6

    return outcome+signVal


i = 0
output = 0
while i < len(input):
    output = output + winning(input.at[i, 'opp'], input.at[i, 'me'])
    i = i+1

print(output)
