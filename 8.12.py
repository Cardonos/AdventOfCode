import pandas as pd
import numpy as np

data = pd.read_csv('Inputs/Day 8.txt', header=None)
# Parsing the Data into a grid
treeGrid = []  # creating the empty grid
j = 0
while j < len(data):
    newLine = []
    k = 0
    while k < len(str(data.iat[j, 0])):  # populating the new line with Trees
        newLine.append(int(str(data.iat[j, 0])[k]))
        k += 1
    if len(treeGrid) > 0:  # adding the new line to the grid
        treeGrid = np.vstack((treeGrid, newLine))
    else:
        treeGrid = newLine
    j += 1

visibleGrid = np.zeros(treeGrid.shape)  # defining the grid to track visibility, 0 means covered, 1 means seen


def checkvisibility(direction, trees, visibility):
    if direction == 'left' or direction == 'right':  # Checking fo which direction is being looked at
        lookingdir = 1
    elif direction == 'up' or direction == 'down':
        lookingdir = 0
    m = 0
    while m < trees.shape[abs(lookingdir - 1)]:  # iterating over the Axis not being looked at
        currentHighestTree = -1  # variable to track the currently highest tree looked at
        n = 0
        if direction == 'left':  # Routines for checking each direction
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[m, n]:  # if the tree is taller than the current highest
                    currentHighestTree = trees[m, n]  # new highest Tree
                    visibility[m, n] = 1  # tree is visible
                n += 1
        elif direction == 'right':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[m, trees.shape[lookingdir] - n - 1]:
                    currentHighestTree = trees[m, trees.shape[lookingdir] - n - 1]
                    visibility[m, trees.shape[lookingdir] - n - 1] = 1
                n += 1
        elif direction == 'down':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[n, m]:
                    currentHighestTree = trees[n, m]
                    visibility[n, m] = 1
                n += 1
        elif direction == 'up':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[trees.shape[lookingdir] - n - 1, m]:
                    currentHighestTree = trees[trees.shape[lookingdir] - n - 1, m]
                    visibility[trees.shape[lookingdir] - n - 1, m] = 1
                n += 1
        m += 1


checkvisibility('down', treeGrid, visibleGrid)
checkvisibility('up', treeGrid, visibleGrid)
checkvisibility('left', treeGrid, visibleGrid)
checkvisibility('right', treeGrid, visibleGrid)  # checking every direction
print('The number of visible trees is ' + str(np.count_nonzero(visibleGrid == 1)))  # counting the number of visible
# trees


# Part 2

def scenicvalue(trees, x, y):   # method to get the scenic value of any given tree
    currentTree = trees[x, y]
    scenvalleft = 0
    scenvalright = 0
    scenvalup = 0
    scenvaldown = 0
    # check left
    o = 1   # iterating towards the left, checking for taller trees, increasing value per tree thats shorter
    while o <= x:
        if trees[x - o, y] < currentTree:
            scenvalleft += 1
        elif trees[x - o, y] >= currentTree:
            scenvalleft += 1
            break
        o += 1
    # check right
    o = 1   # iterating towards the right, checking for taller trees, increasing value per tree thats shorter
    while o + x <= trees.shape[1] - 1:
        if trees[x + o, y] < currentTree:
            scenvalright += 1
        elif trees[x + o, y] >= currentTree:
            scenvalright += 1
            break
        o += 1
    # check up
    o = 1   # iterating upwards, checking for taller trees, increasing value per tree thats shorter
    while o <= y:
        if trees[x, y - o] < currentTree:
            scenvalup += 1
        elif trees[x, y - o] >= currentTree:
            scenvalup += 1
            break
        o += 1
    # check down
    o = 1   # iterating downwards, checking for taller trees, increasing value per tree thats shorter
    while o + y <= trees.shape[0] - 1:
        if trees[x, y + o] < currentTree:
            scenvaldown += 1
        elif trees[x, y + o] >= currentTree:
            scenvaldown += 1
            break
        o += 1
    scenicvalue = scenvaldown*scenvalleft*scenvalright*scenvalup # calculating the scenic value

    return scenicvalue


scenicValueGrid = np.zeros(treeGrid.shape)  # creating the output grid
p = 0
q = 0
while p < treeGrid.shape[0]:
    while q < treeGrid.shape[1]:
        scenicValueGrid[p, q] = scenicvalue(treeGrid, p, q) # calculating the scenic value for each tree on the grid
        q += 1
    q = 0
    p += 1

print('The tree with the highest scenic value has a value of ' + str(np.max(scenicValueGrid)))
