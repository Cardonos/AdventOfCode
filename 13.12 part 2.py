def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return a - b
        else:
            return compare([a], b)
    elif type(b) == int:
        return compare(a, [b])
    for x, y in zip(a, b):
        comp = compare(x, y)
        if not comp == 0:
            return comp
    return len(a) - len(b)


data = list(map(eval, open('Inputs/Day 13.txt').read().split()))
print(data)
check_order = True
while check_order:
    check_order = False
    k = 0
    while k < len(data)-1:
        if compare(data[k], data[k+1]) > 0:
            check_order = True
            a = data[k]
            b = data[k+1]
            data[k] = b
            data[k+1] = a
        k += 1
print((data.index([[2]])+1)*(data.index([[6]])+1))
