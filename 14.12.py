import numpy as np


def drop_sand(location, y, x, end):  # method for how the sand behaves
    new_loc = location
    new_x = x
    new_y = y
    i = 0
    while True:
        if new_y >= end:    # if the sand would fall off the edge
            print('The sand falls off the edge after ' + str(i) + ' blocks')
            exit(0)
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
        new_y = y
        new_x = x
        i += 1


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
cave = np.full((max_y + 1, (max_x - min_x + 1)), '.', dtype=str)    # creating the cave dimensions from min to max value
k = 0
while k < len(draw):    # iterating over the list of move lists
    n = 0
    while n < len(draw[k]) - 1:  # iterating over the list of moves
        cave[draw[k][n][1], draw[k][n][0] - min_x] = '#'    # drawing the first wall
        dif_y = draw[k][n + 1][1] - draw[k][n][1]   # checking if wall goes in y
        dif_x = draw[k][n + 1][0] - draw[k][n][0]   # checking if wall goes in x
        if abs(dif_y) > 0:
            l = 0
            while l <= abs(dif_y):
                if dif_y <= 0:  # checking whether the wall goes up or down
                    cave[draw[k][n][1] - l, draw[k][n][0] - min_x] = '#'
                else:
                    cave[draw[k][n][1] + l, draw[k][n][0] - min_x] = '#'
                l += 1
        elif abs(dif_x) > 0:
            m = 0
            while m <= abs(dif_x):
                if dif_x <= 0:  # checking whether the wall goes left or right
                    cave[draw[k][n][1], draw[k][n][0] - m - min_x] = '#'
                else:
                    cave[draw[k][n][1], draw[k][n][0] + m - min_x] = '#'
                m += 1
        n += 1
    k += 1
print(drop_sand(cave, 0, 500 - min_x, max_y))   # dropping the sand from the given location