
#
# ABANDONED CAUSE IT WILL NOT WORK LIKE THIS
#

import numpy as np
import pandas as pd
import re

data = pd.read_csv('Inputs/Day 7.txt', names=['a', 'b', 'c'], header=None, sep=' ')

i = 0
check = False
arrayOut = []
content = []
while i < len(data):
    if re.search('[a-z]', str(data.at[i, 'c'])) and not pd.isna(data.at[i, 'c']):
        content = [str(data.at[i, 'c'])]
        j = i
        while j < len(data) - 2:
            if data.at[j + 2, 'a'] == '$':
                break
            elif str(data.at[j + 2, 'a']) == 'dir':
                content = np.hstack((content, str(data.at[j + 2, 'b'])))
            else:
                content = np.hstack((content, str(data.at[j + 2, 'a'])))
            j += 1
    if not len(arrayOut) > 0:
        arrayOut = content
    elif len(content) > 0 and len(arrayOut) > 0:
        padding = 0
        laenge = len(arrayOut[0])
        if laenge == 1:
            laenge = len(arrayOut)
        if laenge > len(content):
            padding = int(laenge - len(content))
            content = np.pad(content, (0, padding), 'constant')
        elif laenge < len(content):
            padding = int(len(content) - laenge)
            arrayOut = np.pad(arrayOut, (0, padding), 'constant')
        arrayOut = np.vstack((arrayOut, content))
    content = []
    i += 1


fileSystem = pd.DataFrame(data=arrayOut.T)
print(fileSystem.dtypes)
fileSystem.columns = fileSystem.iloc[0]
fileSystem.drop(index=fileSystem.index[0], axis=0, inplace=True)
print(len(fileSystem.columns))
nested = True
while nested:
    l = 0
    while l < fileSystem.shape[1]:
        m = 1
        searchColumn = 0
        while m < fileSystem.shape[0]:    # Loop bauen, der die erste occurrence des Namens nach der search column gibt
            if re.search('[a-z]', str(fileSystem.iat[m-1, searchColumn])):
                lastColumn = searchColumn
                a = fileSystem.iat[m-1, lastColumn]
                z = searchColumn+1
                while z < len(fileSystem.columns):
                    if fileSystem.columns[z] == str(fileSystem.iat[m-1, lastColumn]):
                        searchColumn = z
                        break
                    z += 1
                m = 0
            m += 1
        n = 0
        while n < fileSystem.shape[0]:
            if re.search('[a-z]', str(fileSystem.iat[n, lastColumn])):
                o = 0
                summe = 0
                while o < fileSystem.shape[0]-1:
                    b = int(fileSystem.iat[o, searchColumn])
                    summe = summe + int(fileSystem.iat[o, searchColumn])
                    o += 1
                c = fileSystem.iat[n, lastColumn]
                fileSystem.iat[n, int(lastColumn)] = summe
                break
            n += 1
        l += 1
    nested = False
    p = 0
    while p < fileSystem.shape[1]:
        q = 0
        while q < fileSystem.shape[0]:
            if re.search('[a-z]', str(fileSystem.iat[q, p])):
                nested = True
            q += 1
        p += 1
print(fileSystem)


