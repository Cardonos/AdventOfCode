import pandas as pd
import numpy as np

data = pd.read_csv('Inputs/Day 8.txt', header=None)
print(data)
# Parsing the Data into a grid
treeGrid = []   # creating the empty grid
j = 0
while j < len(data):
    newLine = []
    k = 0
    while k < len(str(data.iat[j, 0])): # populating the new line with Trees
        newLine.append(int(str(data.iat[j, 0])[k]))
        k += 1
    if len(treeGrid) > 0:   # adding the new line to the grid
        treeGrid = np.vstack((treeGrid, newLine))
    else:
        treeGrid = newLine
    j += 1

visibleGrid = np.zeros(treeGrid.shape)  # defining the grid to track visibility, 0 means covered, 1 means seen


def checkvisibility(direction, trees, visibility):
    if direction == 'left' or direction == 'right': # Checking fo which direction is being looked at
        lookingdir = 1
    elif direction == 'up' or direction == 'down':
        lookingdir = 0
    m = 0
    while m < trees.shape[abs(lookingdir-1)]:   # iterating over the Axis not being looked at
        currentHighestTree = -1 # variable to track the currently highest tree looked at
        n = 0
        if direction == 'left': # Routines for checking each direction
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[m, n]:    # if the tree is taller than the current highest
                    currentHighestTree = trees[m, n]    # new highest Tree
                    visibility[m, n] = 1    #tree is visible
                n += 1
        elif direction == 'right':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[m, trees.shape[lookingdir]-n-1]:
                    currentHighestTree = trees[m, trees.shape[lookingdir]-n-1]
                    visibility[m, trees.shape[lookingdir]-n-1] = 1
                n += 1
        elif direction == 'down':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[n, m]:
                    currentHighestTree = trees[n, m]
                    visibility[n, m] = 1
                n += 1
        elif direction == 'up':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[trees.shape[lookingdir]-n-1, m]:
                    currentHighestTree = trees[trees.shape[lookingdir]-n-1, m]
                    visibility[trees.shape[lookingdir]-n-1, m] = 1
                n += 1
        m += 1

checkvisibility('down', treeGrid, visibleGrid)
checkvisibility('up', treeGrid, visibleGrid)
checkvisibility('left', treeGrid, visibleGrid)
checkvisibility('right', treeGrid, visibleGrid) # checking every direction
print(visibleGrid)
print(np.count_nonzero(visibleGrid == 1))   # counting the number of visible trees

# Part 2