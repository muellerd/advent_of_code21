from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

maxDimensionX = 0
maxDimensionY = 0
commands = []
points = []

for line in lines:
    lineSplit = line.split(',')
    if len(lineSplit) == 2:
        x = int(lineSplit[0])
        y = int(lineSplit[1])
        points.append([x, y])
        if x > maxDimensionX:
            maxDimensionX = x
        if y > maxDimensionY:
            maxDimensionY = y
    if 'fold' in line:
        lineSplit = line.split(' ')
        commands.append(lineSplit[2])

print(maxDimensionY)
print(maxDimensionX)

for command in commands:
    commandSplit = command.split('=')
    relevantIndex = -1
    if commandSplit[0] == 'y':
        relevantIndex = 1
    if commandSplit[0] == 'x':
        relevantIndex = 0

    newPoints = []

    for point in points:
        if point[relevantIndex] > int(commandSplit[1]):
            # create new point
            # horizontal -> newX = oldX, newY = maxY - oldY
            # vertical -> newX = maxX - oldX, newY = oldY
            if relevantIndex == 1:  # horizontal fold line
                newPoint = [point[0], maxDimensionY - point[1]]
                if newPoint not in newPoints:
                    newPoints.append(newPoint)
            if relevantIndex == 0:  # vertical fold line
                newPoint = [maxDimensionX - point[0], point[1]]
                if newPoint not in newPoints:
                    newPoints.append(newPoint)
        else:
            if point not in newPoints:
                newPoints.append(point)

    points = newPoints
    print('Number of points after fold ' + str(command) + ': ' + str(len(points)))
    if relevantIndex == 1:
        maxDimensionY = int(commandSplit[1]) - 1
    if relevantIndex == 0:
        maxDimensionX = int(commandSplit[1]) - 1

for i in range(0, maxDimensionY+1):
    l = ''
    for j in range(0, maxDimensionX+1):
        if [j,i] in points:
            l += '#'
        else:
            l += '.'
    print(l)