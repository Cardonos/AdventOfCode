def compare(a, b):
    if type(a) == int:
        if type(b) == int:  # if both elements are integers
            return a - b    # return their difference to see whether the second is larger than the first
        else:
            return compare([a], b)  # if only a is an int, turn it into a list and call this recursively
    elif type(b) == int:
        return compare(a, [b])  # if only b is an int, turn it into a list and call this recursively
    for x, y in zip(a, b):  # in case both a and b are lists, zip them together and iterate over all their values
        comp = compare(x, y)    # compare the list values, again recursively
        if not comp == 0:   # if this reached a point where both are Integers then return their difference
            return comp
    return len(a) - len(b)  # otherwise just return the difference in list length to see if they are in the right order


data = list(map(str.splitlines, open('Inputs/Day 13.txt').read().strip().split("\n\n")))    # parsing the input into
# pairs of lines
out = 0
for i, (left, right) in enumerate(data):    # for every element in the line pairs
    if compare(eval(left), eval(right)) < 0:    # compare if they are in the right order
        out += i + 1    # add the index in case they are
print('The sum of indices that are in the right order is ' + str(out))