import sys
import numpy as np
from collections import Counter

datastream = str(np.loadtxt('Inputs/Day 6.txt', dtype='str'))   # Loads the Datastream into a string

MarkerLength = input('Length of the marker:')   # Routine to get the desired marker length as user input
try:
    int(MarkerLength)   # checks whether the input is an integer
except ValueError:
    print("This is not a valid integer")    # ends the process if the input is not an integer
    sys.exit()

i = int(MarkerLength)
while i < len(datastream):  # iterates over the input string
    duplicates = False  # initiates the variable that is logging duplicates
    chunk = Counter(datastream[i - int(MarkerLength):i])    # creates a library of how often each character is used in the string
    for char, count in chunk.items():
        if count > 1:   # checks whether there are any duplicate characters in the library
            duplicates = True
    if not duplicates:  # if there are no duplicates then the current location is printed and the loop ends
        print(i)
        break
    i += 1
