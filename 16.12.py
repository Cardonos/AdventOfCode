import re
data = open('Inputs/testdata.txt').read().strip().split('\n')


class Cave_system:
    def __init__(self):
        self.valves = []

    def add_valve(self, valve):
        self.valves.append(valve)


class Valve:
    def __init__(self, name, flow, connections, open):
        self.name = name
        self.flow = flow
        self.connections = connections
        self.open = open



cave = Cave_system()
for i in data:
    valve = i[6:8]
    flow_of_valve = re.findall('-?\d+', i)
    a, r = i.split(';')
    r = r.replace('valves','valve')[len(' tunnels lead to valve '):]
    cave.add_valve(Valve(valve, flow_of_valve, r.split(', '), False))



