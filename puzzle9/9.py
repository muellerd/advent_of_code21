from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

spots = []

for line in lines:
    lineSpots = []
    for l in line:
        lineSpots.append(l)
    spots.append(lineSpots)

sum = 0
lowPoints = []

for i in range(0, len(spots)):
    for j in range(0, len(spots[i])):
        # current spot: i|j
        # top neighbor: i-1|j
        # left neighbor: i|j-1
        # right neighbor: i|j+1
        # bottom neighbor: i+1|j
        currentHeight = int(spots[i][j])
        if currentHeight == 9:
            continue
        if i-1 >= 0:
            if currentHeight > int(spots[i-1][j]):
                continue
        if j-1 >= 0:
            if currentHeight > int(spots[i][j-1]):
                continue
        if j+1 < len(spots[i]):
            if currentHeight > int(spots[i][j+1]):
                continue
        if i+1 < len(spots):
            if currentHeight > int(spots[i+1][j]):
                continue

        lp = [i, j]
        lowPoints.append(lp)
        riskLevel = 1 + int(spots[i][j])
        sum += riskLevel

print("Sum of risk levels: " + str(sum))
basins = []
for lowPoint in lowPoints:
    basinNodes = []
    openCandidates = [lowPoint]
    checkedCandidates = []

    while len(openCandidates) > 0:
        currentCandidate = openCandidates[0]
        if currentCandidate in basinNodes:
            checkedCandidates.append(openCandidates[0])
            openCandidates.remove(openCandidates[0])
            continue
        basinNodes.append(currentCandidate)

        if int(currentCandidate[0])-1 >= 0:
            if int(spots[int(currentCandidate[0])-1][int(currentCandidate[1])]) < 9 and [int(currentCandidate[0])-1, int(currentCandidate[1])] not in checkedCandidates:
                openCandidates.append([int(currentCandidate[0])-1, int(currentCandidate[1])])
        if int(currentCandidate[1])-1 >= 0:
            if int(spots[int(currentCandidate[0])][int(currentCandidate[1])-1]) < 9 and [int(currentCandidate[0]), int(currentCandidate[1])-1] not in checkedCandidates:
                openCandidates.append([int(currentCandidate[0]), int(currentCandidate[1])-1])
        if int(currentCandidate[1])+1 < len(spots[0]):
            if int(spots[int(currentCandidate[0])][int(currentCandidate[1])+1]) < 9 and [int(currentCandidate[0]), int(currentCandidate[1])+1] not in checkedCandidates:
                openCandidates.append([int(currentCandidate[0]), int(currentCandidate[1])+1])
        if int(currentCandidate[0])+1 < len(spots):
            if int(spots[int(currentCandidate[0])+1][int(currentCandidate[1])]) < 9 and [int(currentCandidate[0])+1, int(currentCandidate[1])] not in checkedCandidates:
                openCandidates.append([int(currentCandidate[0])+1, int(currentCandidate[1])])

        checkedCandidates.append(openCandidates[0])
        openCandidates.remove(openCandidates[0])


    basins.append(basinNodes)

basinLengths = []
for basin in basins:
    basinLengths.append(len(basin))

print(basinLengths)
basinLengths = sorted(basinLengths, reverse=True)
print('Result: ' + str(basinLengths[0] * basinLengths[1] * basinLengths[2]))
