import pandas as pd
data = pd.read_csv('Inputs/Day 4.txt', names=['a', 'b', 'c', 'd'], sep=',|-', engine='python')
i = 0; count = 0
while i < len(data):
    if (data.at[i, 'c'] - data.at[i, 'a']) >= 0 and (data.at[i, 'b'] - data.at[i, 'd']) >= 0:
        count+=1
    elif (data.at[i, 'a'] - data.at[i, 'c']) >= 0 and (data.at[i, 'd'] - data.at[i, 'b']) >= 0:
        count+=1
    i+=1
print(count)
