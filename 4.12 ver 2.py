import numpy as np
import pandas as pd

data = pd.read_csv('Inputs/Day 4.txt', names=['a', 'b', 'c', 'd'], sep=',|-', engine='python')

i = 0
count = 0
while i < len(data):
    limLowA = data.at[i, 'a']
    limHiA = data.at[i, 'b']
    limLowB =data.at[i, 'c']
    limHiB = data.at[i, 'd']
    if (limLowB - limLowA) >= 0 and (limHiA - limHiB) >= 0:
        count = count + 1
    elif (limLowA - limLowB) >= 0 and (limHiB - limHiA) >= 0:
        count = count + 1
    i=i+1

print(count)
