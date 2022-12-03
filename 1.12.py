import pandas as pd

input = pd.read_csv("Inputs/Day 1.txt", header=None, skip_blank_lines=False)

i = 0
output = 0
count = 0
while i < input.size:
    if pd.isna(input.at[i, 0]):
        if count > output:
            output = count
            count = 0
        else:
            count = 0
    else:
        count = count + input.at[i, 0]
    i = i + 1
print(output)
