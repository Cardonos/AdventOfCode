import pandas as pd
import numpy as np

data = pd.read_csv('Inputs/Day 5.txt', header=None, names=['a'], nrows=9)
commands = pd.read_csv('Inputs/Day 5.txt', header=None, names=['a', 'count', 'b', 'start', 'c', 'end'], sep=' ',
                       skiprows=9)
print(data)
i = 0
j = 0
stack = []
crates = []
while i < len(data):
    while j < len(data.at[1, 'a']):
        stack = np.append(stack, (data.at[i, 'a'][j:j + 3]))
        j += 4
    if len(crates) == 0:
        crates = stack
    else:
        crates = np.vstack((crates, stack))
    j = 0
    i += 1
    stack = []
print(crates)
crates[0, len(crates)-1] = '   '

def moveCrate(state, start, end, number):
    r = 0
    moving = []
    space = True
    while r < number:
        k = 0
        if not state[r, end - 1] == '   ':
            space = False
        while k < len(state):
            if not state[k, start-1] == '   ':
                if len(moving) == 0:
                    moving = [state[k, start-1]]
                else:
                    moving = np.append(moving, state[k, start-1])
                state[k, start-1] = '   '
                k = len(state)
            else:
                k += 1

        r += 1
    r = 0
    while r < number:
        l = 0
        if space:
            while l < len(state):
                if not state[l, end - 1] == '   ':
                    state[l - 1, end - 1] = moving[len(moving) - 1 - r]
                    l = len(state)
                else:
                    l += 1
        else:
            while l < len(state):
                if not state[0, end - 1] == '   ':
                    newline = np.zeros(len(state[0]), dtype=state.dtype)
                    o = 0
                    while o < len(newline):
                        newline[o] = '   '
                        o += 1
                    newline[end - 1] = moving[len(moving) - 1 - r]
                    state = np.vstack((newline, state))
                    l = len(state)
                elif not state[l, end - 1] == '   ':
                    print(moving[len(moving) - 1 - r])
                    state[l - 1, end - 1] = moving[len(moving) - 1 - r]
                    l = len(state)
                else:
                    l += 1
        r += 1
    return state


m = 0
while m < len(commands):
    crates = moveCrate(crates, commands.at[m, 'start'], commands.at[m, 'end'], commands.at[m, 'count'])
    m += 1
print(crates)

output = []
p = 0
while p < len(crates[0]):
    q = 0
    while q < len(crates):
        if not crates[q, p] == '   ':
            output.append(crates[q, p])
            q = len(crates)
        else:
            q += 1
    p += 1

print(output)

