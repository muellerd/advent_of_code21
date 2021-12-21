from utilities import filetoarray

file = "example1.txt"
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

# execute rules
steps = 10
for s in range(0, steps):
    newPolymer = ''
    newPolymer += polymer[0]
    for i in range(0, len(polymer) - 1):
        #print(polymer[i] + ' - ' + polymer[i + 1])
        newPolymer += rules[polymer[i]][polymer[i+1]] + polymer[i+1]

    polymer = newPolymer
    #print(polymer)

# count occurences:
countDict = {}
for i in range(0, len(polymer)):
    if polymer[i] not in countDict:
        countDict[polymer[i]] = 0
    countDict[polymer[i]] += 1

print(countDict)
minCountChar = ''
minCountValue = 99999999
maxCountChar = ''
maxCountValue = 0
for key in countDict.keys():
    if countDict[key] < minCountValue:
        minCountValue = countDict[key]
        minCountChar = key
    if countDict[key] > maxCountValue:
        maxCountValue = countDict[key]
        maxCountChar = key

print('Result: ' + str(maxCountValue - minCountValue))

