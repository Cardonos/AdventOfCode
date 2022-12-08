import pandas as pd
import numpy as np

data = pd.read_csv('Inputs/Day 8.txt', header=None)
print(data)

indexing = []
i = 0
while i < len(str(data.iat[0, 0])):
    indexing.extend([str(i)])
    i += 1
treeGrid = []
j = 0
while j < len(data):
    newLine = []
    k = 0
    while k < len(str(data.iat[j, 0])):
        newLine.append(int(str(data.iat[j, 0])[k]))
        k += 1
    if len(treeGrid) > 0:
        treeGrid = np.vstack((treeGrid, newLine))
    else:
        treeGrid = newLine
    j += 1

visibleGrid = np.zeros(treeGrid.shape)


def checkvisibility(direction, trees, visibility):
    if direction == 'left' or direction == 'right':
        lookingdir = 1
    elif direction == 'up' or direction == 'down':
        lookingdir = 0
    m = 0
    while m < trees.shape[abs(lookingdir-1)]:
        currentHighestTree = -1
        n = 0
        if direction == 'left':
            while n < trees.shape[lookingdir]:
                if currentHighestTree < trees[m, n]:
                    currentHighestTree = trees[m, n]
                    visibility[m, n] = 1
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

print(treeGrid[0, 1])

checkvisibility('down', treeGrid, visibleGrid)
checkvisibility('up', treeGrid, visibleGrid)
checkvisibility('left', treeGrid, visibleGrid)
checkvisibility('right', treeGrid, visibleGrid)
print(visibleGrid)
print(np.count_nonzero(visibleGrid == 1))
