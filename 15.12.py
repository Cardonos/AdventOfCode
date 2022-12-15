import numpy as np
import math


def draw_circle(center_y, center_x,  radius, cavesystem):
    x = center_x
    y = center_y
    k = 0
    while k < radius*2:
        l = -radius
        while k >= abs(radius+l):
            if x + abs(radius+l) > cavesystem.shape[1] or x - abs(radius+l) < 0:
                l+=1
                break
            if y + k - radius > cavesystem.shape[0] or y + k - radius < 0:
                l+=1
                break
            else:
                cavesystem[y + k - radius, x - abs(radius + l)] = '#'
                cavesystem[y + k - radius, x + abs(radius + l)] = '#'
            l += 1
        k += 1
    return cavesystem


sens_or_beac = True
x = 0
y = 0
sensors = []
beacons = []
data = open('Inputs/testdata.txt').read().split('\n')
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
                        sensors = np.vstack((sensors, [int(y), int(x)]))
                    else:
                        sensors = [[int(y), int(x)]]
                    x = 0
                    y = 0
                    sens_or_beac = False
            else:
                if i.startswith('x='):
                    x = i[2:-1]
                if i.startswith('y='):
                    y = i[2:]
                if not x == 0 and not y == 0:
                    if len(beacons) > 0:
                        beacons = np.vstack((beacons, [int(y), int(x)]))
                    else:
                        beacons = [[int(y), int(x)]]
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
cave = np.full(((max_y - min_y + 1), (max_x - min_x + 1)), '.', dtype=str)
for i in beacons:
    cave[i[0], i[1] - min_x] = 'B'
for i in sensors:
    cave[i[0], i[1] - min_x] = 'S'


distances = []
for i in sensors:
    beacon_distance = []
    j = 0
    while j < len(beacons):
        if len(beacon_distance) > 0:
            beacon_distance.append(math.sqrt((i[0]-beacons[j][0])**2 + (i[1]-beacons[j][1])**2))
        else:
            beacon_distance =  [math.sqrt((i[0] - beacons[j][0]) ** 2 + (i[1] - beacons[j][1]) ** 2)]
        j += 1
    if len(distances) > 0:
        distances.append(min(beacon_distance))
    else:
        distances = [min(beacon_distance)]
print(distances)
cave = draw_circle(sensors[0][0], sensors[0][1]-min_x, math.floor(distances[0]), cave)
print(cave)