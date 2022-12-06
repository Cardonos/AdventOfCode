import sys
import numpy as np
from collections import Counter

datastream = str(np.loadtxt('Inputs/Day 6.txt', dtype='str'))

MarkerLength = input('Length of the marker:')
try:
    int(MarkerLength)
except ValueError:
    print("This is not a valid integer")
    sys.exit()

i = int(MarkerLength)
while i < len(datastream):
    duplicates = False
    chunk = Counter(datastream[i - int(MarkerLength):i])
    for char, count in chunk.items():
        if count > 1:
            duplicates = True
    if not duplicates:
        print(i)
        i=len(datastream)
    i += 1
