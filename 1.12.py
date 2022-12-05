import pandas as pd

input = pd.read_csv("Inputs/Day 1.txt", header=None, skip_blank_lines=False)
# loads the input file including blank lines
i = 0
output = 0
count = 0
while i < input.size:  # iterates over the input file
    if pd.isna(input.at[i, 0]):  # checks whether the line is empty
        if count > output:
            output = count
            count = 0
        else:
            count = 0  # changes the output to the largest instance of the count variable
    else:
        count = count + input.at[i, 0]  # sums up all the inputs that are in a column without an empty line
    i = i + 1
print(output)   # prints the output
