from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

relevant = lines[0]

fishArray = []
for i in relevant.split(','):
    fishArray.append(int(i))

print('Initial state: ' + str(fishArray))

generations = 80
printGenerations = 0
i = 0
while i <= generations:

    tmpArray = []
    newFish = 0
    for j in range(0, len(fishArray)):
        if fishArray[j] == 0:
            tmpArray.append(6)
            newFish += 1
        else:
            tmpArray.append(fishArray[j] - 1)

    for j in range(0, newFish):
        tmpArray.append(8)

    fishArray = tmpArray

    if i <= 18:
        print('After ' + str(i+1) + ' days: ' + str(len(fishArray)) + ' fish -> ' + str(fishArray))
    else:
        print('After ' + str(i + 1) + ' days: ' + str(len(fishArray)) + ' fish')

    i += 1
