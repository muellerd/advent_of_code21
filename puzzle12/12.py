from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)


class Cave:
    def __init__(self, name, small=True):
        self.neighborNames = []
        self.name = name
        self.small = small

    def __str__(self):
        return 'Cave ' + self.name

    def __repr__(self):
        return 'Cave ' + self.name


def maxcountsmallcavesinlist(list):
    counts = {}
    for l in list:
        if l.small:
            if l not in counts:
                counts[l] = 1
            else:
                counts[l] += 1

    maxCount = 0
    for key in counts.keys():
        if counts[key] > maxCount:
            maxCount = counts[key]

    return maxCount


def deepcopylist(list):
    copy = []
    for item in list:
        copy.append(item)

    return copy


rules = 'b'

caves = {}

for line in lines:
    lineSplit = line.split('-')
    if lineSplit[0] not in caves:
        caves[lineSplit[0]] = Cave(lineSplit[0], small=lineSplit[0].islower())
    if lineSplit[1] not in caves:
        caves[lineSplit[1]] = Cave(lineSplit[1], small=lineSplit[1].islower())
    if lineSplit[1] not in caves[lineSplit[0]].neighborNames:
        caves[lineSplit[0]].neighborNames.append(lineSplit[1])
    if lineSplit[0] not in caves[lineSplit[1]].neighborNames:
        caves[lineSplit[1]].neighborNames.append(lineSplit[0])

constructedPaths = [[caves['start']]]
finishedPaths = []
while len(constructedPaths) > 0:
    tmpPaths = []
    for constructedPath in constructedPaths:
        for caveName in constructedPath[len(constructedPath) - 1].neighborNames:
            nextCave = caves[caveName]
            if rules == 'a':
                if nextCave in constructedPath and nextCave.small:
                    continue
            if rules == 'b':
                if (nextCave in constructedPath and nextCave.small
                    and maxcountsmallcavesinlist(constructedPath) >= 2) or (nextCave.name == 'start'):
                    continue
            tmpList = deepcopylist(constructedPath)
            tmpList.append(nextCave)
            if nextCave.name == 'end':
                if tmpList not in finishedPaths:
                    finishedPaths.append(tmpList)
            else:
                tmpPaths.append(tmpList)

    constructedPaths = tmpPaths
    print((len(finishedPaths)))

print('Unique paths: ' + str(len(finishedPaths)))
#for path in finishedPaths:
#    print(path)
