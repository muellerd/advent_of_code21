from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

polymer = lines[0]
print(polymer)
rules = {}

# read rules
for i in range(2, len(lines)):
    lineSplit = lines[i].split(' -> ')
    if lineSplit[0][0] not in rules:
        rules[lineSplit[0][0]] = {}
    if lineSplit[0][1] not in rules[lineSplit[0][0]]:
        rules[lineSplit[0][0]][lineSplit[0][1]] = lineSplit[1]

countDict = {} # count occurences of char
pairDict = {} # dictionary of char pairs to count

# initialize dictionaries
for i in range(0, len(polymer) - 1):
    char1 = polymer[i]
    char2 = polymer[i+1]

    if char1 not in countDict:
        countDict[char1] = 0
    countDict[char1] += 1

    if str(char1 + char2) not in pairDict:
        pairDict[str(char1 + char2)] = 0
    pairDict[str(char1 + char2)] += 1

lastChar = polymer[len(polymer) - 1]
if lastChar not in countDict:
    countDict[lastChar] = 0
countDict[lastChar] += 1

# execute rules
steps = 40
for s in range(0, steps):
    newPairDict = {}
    for pair in pairDict.keys():
        #for i in range(0, pairDict[pair]):
        newChar = rules[pair[0]][pair[1]]
        if newChar not in countDict:
            countDict[newChar] = 0
        countDict[newChar] += pairDict[pair]

        if str(pair[0] + newChar) not in newPairDict:
            newPairDict[str(pair[0] + newChar)] = 0
        newPairDict[str(pair[0] + newChar)] += pairDict[pair]

        if str(newChar + pair[1]) not in newPairDict:
            newPairDict[str(newChar + pair[1])] = 0
        newPairDict[str(newChar + pair[1])] += pairDict[pair]

    pairDict = newPairDict

minCountChar = ''
minCountValue = -1
maxCountChar = ''
maxCountValue = 0
for key in countDict.keys():
    if minCountValue == -1:
        minCountValue = countDict[key]
        minCountChar = key
    else:
        if countDict[key] < minCountValue:
            minCountValue = countDict[key]
            minCountChar = key
    if countDict[key] > maxCountValue:
        maxCountValue = countDict[key]
        maxCountChar = key

print('Result: ' + str(maxCountValue - minCountValue))
