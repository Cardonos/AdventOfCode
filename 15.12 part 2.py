import numpy as np
# Part 2, RIP my PC

sens_or_beac = True
x = 0
y = 0
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
                    if len(beacons) > 0:
                        beacons = np.vstack((beacons,[int(y),int(x)]))
                    else:
                        beacons = [[int(y),int(x)]]
                    x = 0
                    y = 0
                    sens_or_beac = True

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
x_check = 4000000
y_check = 4000000

k=0
while k < len(sensors):
    for dx in range(distances[k]+2):
        dy = (distances[k]+1)-dx
        for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            found = True
            x = sensors[k][1]+(dx*signx)
            y = sensors[k][0]+(dy*signy)
            if not(0 <= x <= x_check and 0 <= y <= y_check):
                continue
            assert abs(x - sensors[k][1]) + abs(y - sensors[k][0]) == distances[k] + 1
            l = 0
            while l < len(sensors):
                dxy = abs(x - sensors[l][1]) + abs(y - sensors[l][0])
                if dxy <= distances[l]:
                    found = False
                l += 1
            if found:
                print(x)
                print(y)
                print(x * 4000000 + y)
                exit(0)
    k += 1
