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


data = list(map(eval, open('Inputs/Day 13.txt').read().split()))    # Parsing the input into a list of elements
check_order = False  # tracking whether the list is ordered
while not check_order:  # while the list isn't ordered
    check_order = True
    k = 0
    while k < len(data)-1:  # iterating over the list
        if compare(data[k], data[k+1]) > 0:  # if something in the list is out of order
            check_order = False
            line_1 = data[k]
            line_2 = data[k+1]
            data[k] = line_2
            data[k+1] = line_1   # changing the order of the elements
        k += 1
print('The decoder key is ' + str((data.index([[2]])+1)*(data.index([[6]])+1)))
