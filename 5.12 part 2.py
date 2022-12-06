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


def moveCrate(state, start, end, number):
    r = 0
    moving = []
    space = True
    while r < number:  # iterating over the number of cells to be moved
        k = 0
        if not state[r, end - 1] == '   ':
            space = False  # checks whether the stack to be inserted is higher than the current maximum height
        while k < len(state):  # iterates over the starting stack
            if not state[k, start - 1] == '   ':  # looking for the first non-empty cell
                if len(moving) == 0:
                    moving = [state[k, start - 1]]  # creating the moving vector if it does not exist yet
                else:
                    moving = np.append(moving, state[k, start - 1])  # appending to the moving vector
                state[k, start - 1] = '   '  # replacing the copied cells with empty cells
                break
            else:
                k += 1

        r += 1
    r = 0
    while r < number:  # iterating over the number of cells to be moved
        l = 0
        if space:
            while l < len(state):
                if not state[l, end - 1] == '   ':
                    state[l - 1, end - 1] = moving[len(moving) - 1 - r]
                    break  # If there is enough space for the entire movement stack it just gets placed down
                else:
                    l += 1
        else:  # if there is not enough space for the entire movement stack
            while l < len(state):
                if not state[0, end - 1] == '   ':  # if the top cell is filled it creates a new line
                    newline = np.zeros(len(state[0]), dtype=state.dtype)
                    o = 0
                    while o < len(newline):
                        newline[o] = '   '
                        o += 1
                    newline[end - 1] = moving[len(moving) - 1 - r]
                    state = np.vstack((newline, state))  # the to be moved cell gets stacked together with the new row
                    break
                elif not state[l, end - 1] == '   ':  # checks for the first non-empty cell
                    state[l - 1, end - 1] = moving[len(moving) - 1 - r]  # places the object in the first empty cell
                    break
                else:
                    l += 1
        r += 1
    return state


m = 0
while m < len(commands):
    crates = moveCrate(crates, commands.at[m, 'start'], commands.at[m, 'end'], commands.at[m, 'count'])
    m += 1  # iterates over the list of commands to create the final stack
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
