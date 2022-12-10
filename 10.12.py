import pandas as pd

data = pd.read_csv('Inputs/Day 10.txt', sep=' ', names=['op', 'val'], dtype={'op': str, 'val': 'Int64'})


def cycle(instructions, index, add_step):   # defining the processes that can happen during a cycle
    if instructions.at[index, 'op'] == 'noop':
        new_index = index + 1
        add = 0
        return new_index, add_step, add  # if 'noop' then only a new index gets returned
    elif add_step == 0:
        new_step = 1
        add = 0
        return index, new_step, add  # first half of the adding cycle, new step returned, same index
    else:
        new_step = 0
        new_index = index + 1
        add = instructions.at[index, 'val']
    return new_index, new_step, add  # second half of the adding cycle, new step returned, new index and the value


cycles = 1
output = 0
curr_index = 0
step = 0
x = 1
while curr_index < len(data):   # iterating over all the indexes, while counting cycles and incrementing x
    curr_cycle = cycle(data, curr_index, step)
    curr_index = curr_cycle[0]
    step = curr_cycle[1]
    x = x + curr_cycle[2]
    cycles += 1
    if cycles == 20:
        output += cycles * x
    if cycles == 60:
        output += cycles * x
    if cycles == 100:
        output += cycles * x
    if cycles == 140:
        output += cycles * x
    if cycles == 180:
        output += cycles * x
    if cycles == 220:
        output += cycles * x
print('The sum of the signal strength at the given values is ' + str(output))

# Part 2, building a printing routine
cycles = 1
curr_index = 0
step = 0
x = 1
newLine = ''    # the output line that the output characters get appended to
while curr_index < len(data):   # iterating over all the indexes, while counting cycles and incrementing x
    curr_cycle = cycle(data, curr_index, step)
    pointer = divmod(cycles, 40)[1]  # current segment of the screen that's being displayed
    if abs(x - (pointer-1)) <= 1:  # checking whether x is within a block of the to be shown pixel
        newLine += '#'
    else:
        newLine += '.'
    if pointer == 0:    # if the end of the line is reached it gets printed and reset
        print(newLine)
        newLine = ''
    curr_index = curr_cycle[0]
    step = curr_cycle[1]
    x = x + curr_cycle[2]
    cycles += 1
