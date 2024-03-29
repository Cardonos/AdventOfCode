import numpy as np



sens_or_beac = True
x = 0
y = 0
y_check = 2000000
beacons_on_y = 0
sensors = []
beacons = []
data = open('Inputs/Day 15.txt').read().split('\n')
for line in data:
    for k in line.split(':'):
        for i in k.split():
            if sens_or_beac:
                if i.startswith('x='):
                    x = i[2:-1]
                if i.startswith('y='):
                    y = i[2:]
                if not x == 0 and not y == 0:
                    if len(sensors) > 0:
                        sensors = np.vstack((sensors,[int(y),int(x)]))
                    else:
                        sensors = [[int(y),int(x)]]
                    x = 0
                    y = 0
                    sens_or_beac = False
            else:
                if i.startswith('x='):
                    x = i[2:-1]
                if i.startswith('y='):
                    y = i[2:]
                if not x == 0 and not y == 0:
                    if y == y_check:
                        beacons_on_y += 1
                    if len(beacons) > 0:
                        beacons = np.vstack((beacons,[int(y),int(x)]))
                    else:
                        beacons = [[int(y),int(x)]]
                    x = 0
                    y = 0
                    sens_or_beac = True
max_x = 0
max_y = 0
min_x = 0
min_y = 0
for i in sensors:
    if i[0] > max_y:
        max_y = i[0]
    if i[0] < min_y:
        min_y = i[0]
    if i[1] > max_x:
        max_x = i[1]
    if i[1] < min_x:
        min_x = i[1]
for i in beacons:
    if i[0] > max_y:
        max_y = i[0]
    if i[0] < min_y:
        min_y = i[0]
    if i[1] > max_x:
        max_x = i[1]
    if i[1] < min_x:
        min_x = i[1]

distances = []
for i in sensors:
    beacon_distance = []
    j = 0
    while j < len(beacons):
        if len(beacon_distance) > 0:
            beacon_distance.append(abs(i[0] - beacons[j][0]) + abs(i[1] - beacons[j][1]))
        else:
            beacon_distance = [abs(i[0] - beacons[j][0]) + abs(i[1] - beacons[j][1])]
        j += 1
    if len(distances) > 0:
        distances.append(min(beacon_distance))
    else:
        distances = [min(beacon_distance)]


coverage = 0
o = 0
sensors_in_range = []
dist_in_range = []
while o < len(sensors):
    if sensors[o][0] + distances[o] < y_check or sensors[o][0] - distances[o] > y_check:
        o += 1
        continue
    else:
        if len(sensors_in_range) > 0:
            sensors_in_range = np.vstack((sensors_in_range,[sensors[o][0],sensors[o][1]]))
        else:
            sensors_in_range = [sensors[o][0],sensors[o][1]]
        if len(dist_in_range) > 0:
            dist_in_range.append(distances[o])
        else:
            dist_in_range = [distances[o]]
    o += 1

m = min_x - max(distances) - 10
while m < max_x + max(distances) + 10:
    covered = False
    n = 0
    while n < len(sensors_in_range):
        if abs(sensors_in_range[n][0] - y_check) + abs(sensors_in_range[n][1] - m) <= dist_in_range[n]:
            covered = True
        n += 1
    if covered:
        coverage += 1
        covered = False
    m += 1

print(coverage - 1)
