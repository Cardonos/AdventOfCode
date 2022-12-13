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


data = list(map(str.splitlines, open('Inputs/testdata.txt').read().strip().split("\n\n")))

out = 0
for i, (left, right) in enumerate(data):
    if compare(eval(left), eval(right)) < 0:
        out += i + 1
print(out)