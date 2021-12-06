from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)
taskflag = 'b'

map = {}

for line in lines:
    lineSplit = line.split(' -> ')

    x1 = int(lineSplit[0].split(',')[0])
    y1 = int(lineSplit[0].split(',')[1])
    x2 = int(lineSplit[1].split(',')[0])
    y2 = int(lineSplit[1].split(',')[1])
    if taskflag == 'a':
        if not (x1 == x2 or y1 == y2):
            continue

    print(lineSplit)
    if x1 == x2:
        distance = abs(y1 - y2) + 1
        if y1 < y2:
            for i in range(0, distance):
                if not x1 in map:
                    map[x1] = {}
                if not (y1 + i) in map[x1]:
                    map[x1][y1 + i] = 1
                else:
                    map[x1][y1 + i] += 1
        else:
            for i in range(0, distance):
                if not x1 in map:
                    map[x1] = {}
                if not (y2 + i) in map[x1]:
                    map[x1][y2 + i] = 1
                else:
                    map[x1][y2 + i] += 1
    else:
        if y1 == y2:
            distance = abs(x1 - x2) + 1
            if x1 < x2:
                for i in range(0, distance):
                    if not (x1 + i) in map:
                        map[x1 + i] = {}
                    if not y1 in map[x1 + i]:
                        map[x1 + i][y1] = 1
                    else:
                        map[x1 + i][y1] += 1
            else:
                for i in range(0, distance):
                    if not (x2 + i) in map:
                        map[x2 + i] = {}
                    if not y1 in map[x2 + i]:
                        map[x2 + i][y1] = 1
                    else:
                        map[x2 + i][y1] += 1
        else:
            # x1 != x2 and y1 != y2
            distanceX = x2 - x1
            distanceY = y2 - y1
            # distx > 0, disty > 0
            # distx > 0, disty < 0
            # distx < 0, disty > 0
            # distx < 0, disty < 0

            if distanceX >= 0 and distanceY >= 0:
                for i in range(0, abs(distanceX) + 1):
                    position = '[' + str(x1 + i) + ', ' + str(y1 + i) + ']'
                    if not (x1 + i) in map:
                        map[x1 + i] = {}
                    if not (y1 + i) in map[x1 + i]:
                        map[x1 + i][y1 + i] = 1
                    else:
                        map[x1 + i][y1 + i] += 1

            if distanceX >= 0 and distanceY < 0:
                for i in range(0, abs(distanceX) + 1):
                    position = '[' + str(x1 + i) + ', ' + str(y1 - i) + ']'
                    if not (x1 + i) in map:
                        map[x1 + i] = {}
                    if not (y1 - i) in map[x1 + i]:
                        map[x1 + i][y1 - i] = 1
                    else:
                        map[x1 + i][y1 - i] += 1

            if distanceX < 0 and distanceY >= 0:
                for i in range(0, abs(distanceX) + 1):
                    position = '[' + str(x1 - i) + ', ' + str(y1 + i) + ']'
                    if not (x1 - i) in map:
                        map[x1 - i] = {}
                    if not (y1 + i) in map[x1 - i]:
                        map[x1 - i][y1 + i] = 1
                    else:
                        map[x1 - i][y1 + i] += 1

            if distanceX < 0 and distanceY < 0:
                for i in range(0, abs(distanceX) + 1):
                    position = '[' + str(x1 - i) + ', ' + str(y1 - i) + ']'
                    if not (x1 - i) in map:
                        map[x1 - i] = {}
                    if not (y1 - i) in map[x1 - i]:
                        map[x1 - i][y1 - i] = 1
                    else:
                        map[x1 - i][y1 - i] += 1

print(map)

# determine overlap count
count = 0
for key in map:
    for kkey in map[key]:
        if map[key][kkey] >= 2:
            count += 1

print("Number of overlaps > 2: " + str(count))