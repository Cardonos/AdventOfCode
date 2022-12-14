import numpy as np
# Part 2, added floor and simulated until block rests at the top


def drop_sand(location, y, x, end):  # method for how the sand behaves
    new_loc = location
    new_x = x
    new_y = y
    i = 0
    while True:
        if new_loc[new_y + 1, new_x] == '.':    # if the sand can move down, it does
            new_y += 1
            continue
        if new_loc[new_y + 1, new_x - 1] == '.':    # if the sand can move down left, it does
            new_y += 1
            new_x = new_x - 1
            continue
        if new_loc[new_y + 1, new_x + 1] == '.':    # if the sand can move down right, it does
            new_y += 1
            new_x += 1
            continue
        new_loc[new_y, new_x] = 'o'  # when the sand can't move it gets set down
        i += 1
        if new_y == y and new_x == x:   # if the block placed is the one at the top
            print('The cave is full after ' + str(i) + ' blocks')
            exit(0)
        new_y = y
        new_x = x



draw = []
for data in open('Inputs/Day 14.txt'):  # parsing the data line by line
    newLine = []
    for line in data.strip().split(' -> '):  # splitting the moves per line
        scan = list((map(int, line.split(','))))    # splitting the xy coords
        if len(newLine) > 0:
            newLine.append(scan)
        else:
            newLine = [scan]
    if len(draw) > 0:
        draw.append(newLine)    # end result is a list containing the list of moves split in x and y
    else:
        draw = [newLine]
max_y = 0
min_x = draw[0][0][0]
max_x = 0
i = 0
while i < len(draw):
    j = 0
    while j < len(draw[i]):
        if draw[i][j][0] < min_x:
            min_x = draw[i][j][0]
        if draw[i][j][0] > max_x:
            max_x = draw[i][j][0]
        if draw[i][j][1] > max_y:
            max_y = draw[i][j][1]
        j += 1
    i += 1
cave = np.full((max_y + 3, max_x+500), '.', dtype=str)  # making the cave lower to the floor and much wider
o = 0
while o < cave.shape[1]:    # adding the cave floor
    cave[max_y + 2, o] = '#'
    o += 1
k = 0
while k < len(draw):    # iterating over the list of move lists
    n = 0
    while n < len(draw[k]) - 1:  # iterating over the list of moves
        cave[draw[k][n][1], draw[k][n][0]] = '#'    # drawing the first wall
        dif_y = draw[k][n + 1][1] - draw[k][n][1]   # checking if wall goes in y
        dif_x = draw[k][n + 1][0] - draw[k][n][0]   # checking if wall goes in x
        if abs(dif_y) > 0:
            l = 0
            while l <= abs(dif_y):
                if dif_y <= 0:  # checking whether the wall goes up or down
                    cave[draw[k][n][1] - l, draw[k][n][0]] = '#'
                else:
                    cave[draw[k][n][1] + l, draw[k][n][0]] = '#'
                l += 1
        elif abs(dif_x) > 0:
            m = 0
            while m <= abs(dif_x):
                if dif_x <= 0:  # checking whether the wall goes left or right
                    cave[draw[k][n][1], draw[k][n][0] - m] = '#'
                else:
                    cave[draw[k][n][1], draw[k][n][0] + m] = '#'
                m += 1
        n += 1
    k += 1
print(drop_sand(cave, 0, 500, max_y + 3))   # dropping sand from the given location
