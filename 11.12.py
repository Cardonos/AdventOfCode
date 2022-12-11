import math
import numpy as np


class Monkey:
    def __init__(self, name, items, operation, test, target_true, target_false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.target_true = target_true
        self.target_false = target_false
        self.inspections = 0

    def get_items(self):
        return self.items

    def inspect(self):
        self.inspections += 1
        if self.operation[0] == '*':
            if self.operation[1] == 'old':
                self.items[0] = math.floor(int(self.items[0]) * int(self.items[0]) / 3)
            else:
                self.items[0] = math.floor(int(self.items[0]) * int(self.operation[1]) / 3)
        else:
            if self.operation[1] == 'old':
                self.items[0] = math.floor((int(self.items[0]) + int(self.items[0])) / 3)
            else:
                self.items[0] = math.floor((int(self.items[0]) + int(self.operation[1])) / 3)

    def throw(self):
        thrown_item = int(self.items[0])
        self.items = np.delete(self.items, 0)
        if divmod(thrown_item, int(self.test))[1] == 0:
            return thrown_item, self.target_true
        else:
            return thrown_item, self.target_false

    def catch(self, caught_item):
        self.items = np.append(self.items, (caught_item))


class Forest:
    def __init__(self):
        self.monkeys = []
    def inspect(self, index):
        return self.monkeys[index].inspect()

    def throw(self, index):
        return self.monkeys[index].throw()

    def catch(self, caught_item):
        self.monkeys[int(caught_item[1])].catch(caught_item[0])

    def get_items(self, index):
        items = self.monkeys[index].get_items()
        return items

    def get_inspects(self, index):
        return self.monkeys[index].inspections

    def new_monkey(self, new):
        self.monkeys.append(new)


data = open('Inputs/Day 11.txt')
j = 0
forest = Forest()   # Parsing the data and populating the forest with Monkeys
for a in data:
    a = a.rstrip()
    if a.startswith('Monkey'):
        name = a[7]
    if a.startswith('  Starting'):
        items = []
        i = 18
        while i < len(a):
            items.append(a[i:(i+2)])
            i += 4
    if a.startswith('  Operation'):
        operation = [a[23], a[25::]]
    if a.startswith('  Test'):
        test = a[21::]
    if a.startswith('    If true'):
        target_true = a[29]
    if a.startswith('    If false'):
        target_false = a[30]
    if divmod(j, 7)[1] == 5:
        new_monkey = Monkey(name, items, operation, test, target_true, target_false)
        forest.new_monkey(new_monkey)
    j += 1
# 20 Rounds, iterating over the monkeys, making them do their actions
n = 0
while n < 20:
    m = 0
    for k in forest.monkeys:
        o = 0
        itemnumber = len(forest.get_items(m))
        while o < itemnumber:
            forest.inspect(m)
            throwing = forest.throw(m)
            forest.catch(throwing)
            o += 1
        m += 1
    n += 1
monkey_business = []
p = 0
for k in forest.monkeys:    # getting the number of inspections done by each monkey
    monkey_business = np.append(monkey_business, forest.get_inspects(p))
    p += 1
monkey_business = np.sort(monkey_business)
print('The amount of monkey business that has happened is ' + str(monkey_business[-1]*monkey_business[-2]))
