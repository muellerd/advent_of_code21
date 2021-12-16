from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

#print(lines)

def printOctopuses(octopuses):
    toPrint = ''
    for line in octopuses:
        l = ''
        for column in line:
            l += str(column)
        toPrint += l + '\n'

    print(toPrint)

octopuses = []
for line in lines:
    row = []
    for l in line:
        row.append(int(l))
    octopuses.append(row)

#print(octopuses)

steps = 300
numberOfFlashes = 0

for step in range(0, steps):

    #print('Step: ' + str(step + 1))
    #print('Before:')
    #printOctopuses(octopuses)

    # step = increase & flashes
    # increase by 1
    tmpOctopuses = []
    flashingCandidates = []
    for i in range(0, len(octopuses)):
        row = []
        for j in range(0, len(octopuses[i])):
            newValue = octopuses[i][j] + 1
            if newValue > 9:
                if [i, j] not in flashingCandidates:
                    flashingCandidates.append([i, j])
            row.append(octopuses[i][j] + 1)
        tmpOctopuses.append(row)

    #print(tmpOctopuses)

    hasFlashed = []

    #print(flashingCandidates)
    while len(flashingCandidates) > 0:
        newCandidates = []
        for flashingCandidate in flashingCandidates: # [i, j]
            if flashingCandidate not in hasFlashed:
                hasFlashed.append(flashingCandidate)
                #print('Octopus ' + str(flashingCandidate[0]) + '|' + str(flashingCandidate[1]) +
                #      ' has flashed with value ' + str(tmpOctopuses[flashingCandidate[0]][flashingCandidate[1]]))
            #tmpOctopuses[flashingCandidate[0]][flashingCandidate[1]] = 0
            # increase adjacent ones
            # [i-1, j-1]
            # [i-1, j]
            # [i-1, j+1]
            # [i, j-1]
            # [i, j+1]
            # [i+1, j-1]
            # [i+1, j]
            # [i+1, j+1]
            i = flashingCandidate[0]
            j = flashingCandidate[1]
            if i-1 >= 0 and j-1 >= 0:
                tmpOctopuses[i-1][j-1] += 1
                if tmpOctopuses[i-1][j-1] > 9:
                    if [i-1, j-1] not in newCandidates \
                            and [i-1, j-1] not in hasFlashed\
                            and [i-1, j-1] not in flashingCandidates:
                        newCandidates.append([i-1, j-1])
            if i-1 >= 0:
                tmpOctopuses[i-1][j] += 1
                if tmpOctopuses[i-1][j] > 9:
                    if [i-1, j] not in newCandidates \
                            and [i-1, j] not in hasFlashed\
                            and [i-1, j] not in flashingCandidates:
                        newCandidates.append([i-1, j])
            if i-1 >= 0 and j+1 < len(tmpOctopuses[i-1]):
                tmpOctopuses[i-1][j+1] += 1
                if tmpOctopuses[i-1][j+1] > 9:
                    if [i-1, j+1] not in newCandidates \
                            and [i-1, j+1] not in hasFlashed \
                            and [i-1, j+1] not in flashingCandidates:
                        newCandidates.append([i-1, j+1])
            if j-1 >= 0:
                tmpOctopuses[i][j-1] += 1
                if tmpOctopuses[i][j-1] > 9:
                    if [i, j-1] not in newCandidates \
                            and [i, j-1] not in hasFlashed \
                            and [i, j-1] not in flashingCandidates:
                        newCandidates.append([i, j-1])
            if j+1 < len(tmpOctopuses[i]):
                tmpOctopuses[i][j+1] += 1
                if tmpOctopuses[i][j+1] > 9:
                    if [i, j+1] not in newCandidates \
                            and [i, j+1] not in hasFlashed \
                            and [i, j+1] not in flashingCandidates:
                        newCandidates.append([i, j+1])
            if i+1 < len(tmpOctopuses) and j-1 >= 0:
                tmpOctopuses[i+1][j-1] += 1
                if tmpOctopuses[i+1][j-1] > 9:
                    if [i+1, j-1] not in newCandidates \
                            and [i+1, j-1] not in hasFlashed \
                            and [i+1, j-1] not in flashingCandidates:
                        newCandidates.append([i+1, j-1])
            if i+1 < len(tmpOctopuses):
                tmpOctopuses[i+1][j] += 1
                if tmpOctopuses[i+1][j] > 9:
                    if [i+1, j] not in newCandidates \
                            and [i+1, j] not in hasFlashed \
                            and [i+1, j] not in flashingCandidates:
                        newCandidates.append([i+1, j])
            if i+1 < len(tmpOctopuses) and j+1 < len(tmpOctopuses[i+1]):
                tmpOctopuses[i+1][j+1] += 1
                if tmpOctopuses[i+1][j+1] > 9:
                    if [i+1, j+1] not in newCandidates \
                            and [i+1, j+1] not in hasFlashed \
                            and [i+1, j+1] not in flashingCandidates:
                        newCandidates.append([i+1, j+1])
        flashingCandidates = newCandidates

    numberOfFlashes += len(hasFlashed)
    for hf in hasFlashed:
        tmpOctopuses[hf[0]][hf[1]] = 0

    octopuses = tmpOctopuses

    #print('After:')
    #printOctopuses(octopuses)

    if len(hasFlashed) == len(tmpOctopuses) * len(tmpOctopuses[0]):
        print('SYNCHRONOUS FLASH ALERT: Step ' + str(step + 1))
        break

print('Number of flashes after ' + str(steps) + ' steps: ' + str(numberOfFlashes))