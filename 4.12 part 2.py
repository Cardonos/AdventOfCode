import pandas as pd
data = pd.read_csv('Inputs/Day 4.txt', names=['a', 'b', 'c', 'd'], sep=',|-', engine='python')
i = 0; count = 0    # imports the input as 4 columns with , and - as separators
while i < len(data):
    if (data.at[i, 'c'] - data.at[i, 'a']) >= 0 and (data.at[i, 'b'] >= data.at[i, 'c']):
        count += 1  # if the first row overlaps the second row increase the count by one
    elif (data.at[i, 'a'] - data.at[i, 'c']) >= 0 and (data.at[i, 'd'] >= data.at[i, 'a']):
        count += 1  # if the second row overlaps the first row increase the count by one
    i += 1
print(count)    # output the number of overlapping rows
