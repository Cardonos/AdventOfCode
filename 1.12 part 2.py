import pandas as pd
import numpy as np

input = pd.read_csv("Inputs/Day 1.txt", header=None, skip_blank_lines=False)

i = 0
output = 0
count = 0
sums=np.array([], dtype=int)
print(sums)
while i < input.size:
    if pd.isna(input.at[i, 0]):
        sums = np.append(sums,count)
        count = 0
    else:
        count = count + input.at[i, 0]
    i = i + 1
sums = np.append(sums,count)
print(sums)
sums = np.sort(sums)

output=sums[len(sums)-1]+sums[len(sums)-2]+sums[len(sums)-3]
print(output)
