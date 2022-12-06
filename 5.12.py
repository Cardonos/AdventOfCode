import pandas as pd
import numpy as np

data = pd.read_csv('Inputs/Day 5.txt', header=None, names=['a'], nrows=9)
commands = pd.read_csv('Inputs/Day 5.txt', header=None, names=['a', 'count', 'b', 'start', 'c', 'end'], sep=' ',
                       skiprows=9)
# Importing the two halves of the Data: the Box Stack and the list of Instructions
print(data)
i = 0
j = 0
stack = []
crates = []
while i < len(data):
    while j < len(data.at[1, 'a']):
        stack = np.append(stack, (data.at[i, 'a'][j:j + 3]))  # building the stack, three characters at a time
        j += 4  # skipping to the start of the next cell
    if len(crates) == 0:
        crates = stack  # when the output is empty the first value is the input
    else:
        crates = np.vstack((crates, stack))  # appending the new values in case the output isnt empty
    j = 0
    i += 1
    stack = []
crates[0, len(crates) - 1] = '   '  # manually adding a cell because for whatever reason the text input file
# automatically deletes it
print(crates)


def moveCrate(state, start, end):  # routine for moving a crate from a start position to an end position, returns
    # the new stack
    k = 0
    l = 0
    while k < len(state):  # iterates over the starting column
        if not state[k, start - 1] == '   ':  # Checks whether the currently looked at cell is filled
            moving = state[k, start - 1]
            state[k, start - 1] = '   '
            break  # copies the object to be moved and replaces it with an empty cell
        else:
            k += 1
    while l < len(state):  # iterates over the target column
        if not state[0, end - 1] == '   ':  # checks whether the top spot of the column is filled
            newline = np.zeros(len(state[0]), dtype=state.dtype)
            o = 0
            while o < len(newline):
                newline[o] = '   '
                o += 1
            newline[end - 1] = moving
            state = np.vstack((newline, state))  # creates a new row with the target cell filled and stacks it
            break
        elif not state[l, end - 1] == '   ':  # checks whether the target cell is filled
            state[l - 1, end - 1] = moving
            break  # places the copied object in the first free cell
        else:
            l += 1
    return state  # returns the new stack


m = 0
while m < len(commands):
    n = 0
    while n < commands.at[m, 'count']:
        crates = moveCrate(crates, commands.at[m, 'start'], commands.at[m, 'end'])
        n += 1  # Iterates over the commands to create the final state of the stack
    m += 1
print(crates)

output = []
p = 0
while p < len(crates[0]):
    q = 0
    while q < len(crates):
        if not crates[q, p] == '   ':
            output.append(crates[q, p])
            break  # iterates over the stack to create the final output
        else:
            q += 1
    p += 1

print(output)
