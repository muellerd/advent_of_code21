from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

numberToWires = {}
numberToWires[0] = ['top', 'topleft', 'topright', 'bottomleft', 'bottomright', 'bottom']
numberToWires[1] = ['topright', 'bottomright']
numberToWires[2] = ['top', 'topright', 'middle', 'bottomleft', 'bottom']
numberToWires[3] = ['top', 'topright', 'middle', 'bottomright', 'bottom']
numberToWires[4] = ['topleft', 'topright', 'middle', 'bottomright']
numberToWires[5] = ['top', 'topleft', 'middle', 'bottomright', 'bottom']
numberToWires[6] = ['top', 'topleft', 'middle', 'bottomleft', 'bottomright', 'bottom']
numberToWires[7] = ['top', 'topright', 'bottomright']
numberToWires[8] = ['top', 'topleft', 'topright', 'middle', 'bottomleft', 'bottomright', 'bottom']
numberToWires[9] = ['top', 'topleft', 'topright', 'middle', 'bottomright', 'bottom']

sum = 0
unclear = 0
for line in lines:
    topCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    topLeftCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    topRightCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    middleCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    bottomLeftCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    bottomRightCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    bottomCandidates = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    aCandidates = []
    bCandidates = []
    cCandidates = []
    dCandidates = []
    eCandidates = []
    fCandidates = []
    gCandidates = []
    lineSplit = line.split(' | ')
    inputItems = lineSplit[0].split(' ')
    determineItems = lineSplit[1].split(' ')

    lengthToItem = {}
    wireToCandidates = {'a': aCandidates, 'b': bCandidates, 'c': cCandidates, 'd': dCandidates, 'e': eCandidates,
                        'f': fCandidates, 'g': gCandidates}

    for item in inputItems:
        if len(item) not in lengthToItem:
            lengthToItem[len(item)] = []
        lengthToItem[len(item)].append(item)

    # length 2 => number 1
    for item in lengthToItem[2]:
        for c in item:
            if 'topright' not in wireToCandidates[c]:
                wireToCandidates[c].append('topright')
            if 'bottomright' not in wireToCandidates[c]:
                wireToCandidates[c].append('bottomright')
            if c in topCandidates:
                topCandidates.remove(c)
            if c in topLeftCandidates:
                topLeftCandidates.remove(c)
            if c in middleCandidates:
                middleCandidates.remove(c)
            if c in bottomLeftCandidates:
                bottomLeftCandidates.remove(c)
            if c in bottomCandidates:
                bottomCandidates.remove(c)
        topRightCandidates = []
        bottomRightCandidates = []
        for c in item:
            topRightCandidates.append(c)
            bottomRightCandidates.append(c)

    # length 4 => 4
    # 4 => 4, top left, top right, middle, bottom right
    for item in lengthToItem[4]:
        for c in item:
            if 'topleft' not in wireToCandidates[c]:
                wireToCandidates[c].append('topleft')
            if 'topright' not in wireToCandidates[c]:
                wireToCandidates[c].append('topright')
            if 'middle' not in wireToCandidates[c]:
                wireToCandidates[c].append('middle')
            if 'bottomright' not in wireToCandidates[c]:
                wireToCandidates[c].append('bottomright')
            if c in topCandidates:
                topCandidates.remove(c)
            if c in bottomLeftCandidates:
                bottomLeftCandidates.remove(c)
            if c in bottomCandidates:
                bottomCandidates.remove(c)
        topLeftCandidates = []
        middleCandidates = []
        for c in item:
            topLeftCandidates.append(c)
            middleCandidates.append(c)
        if len(topRightCandidates) <= 2:
            for c in topRightCandidates:
                if c in topLeftCandidates:
                    topLeftCandidates.remove(c)
                if c in middleCandidates:
                    middleCandidates.remove(c)

    # length 3 => 7
    # 7 => 3, top, top right, bottom right
    for item in lengthToItem[3]:
        for c in item:

            if c in topLeftCandidates:
                topLeftCandidates.remove(c)
            if c in middleCandidates:
                middleCandidates.remove(c)
            if c in bottomLeftCandidates:
                bottomLeftCandidates.remove(c)
            if c in bottomCandidates:
                bottomCandidates.remove(c)
        topCandidates = []
        for c in item:
            topCandidates.append(c)
        if len(topRightCandidates) <= 2:
            for c in topRightCandidates:
                if c in topCandidates:
                    topCandidates.remove(c)

    #print(lengthToItem)
    #print("Top: " + str(topCandidates))
    #print("Top Left: " + str(topLeftCandidates))
    #print("Top Right: " + str(topRightCandidates))
    #print("Middle: " + str(middleCandidates))
    #print("Bottom Left: " + str(bottomLeftCandidates))
    #print("Bottom Right: " + str(bottomRightCandidates))
    #print("Bottom: " + str(bottomCandidates))

    result = ''
    for i in determineItems:
        #print(i)
        open = []
        save = []

        for c in i:
            wires = []
            if c in topCandidates:
                if len(topCandidates) == 1:
                    save.append('top')
                else:
                    wires.append('top')
            if c in topLeftCandidates:
                if len(topLeftCandidates) == 1:
                    save.append('topleft')
                else:
                    wires.append('topleft')
            if c in topRightCandidates:
                if len(topRightCandidates) == 1:
                    save.append('topright')
                else:
                    wires.append('topright')
            if c in middleCandidates:
                if len(middleCandidates) == 1:
                    save.append('middle')
                else:
                    wires.append('middle')
            if c in bottomLeftCandidates:
                if len(bottomLeftCandidates) == 1:
                    save.append('bottomleft')
                else:
                    wires.append('bottomleft')
            if c in bottomRightCandidates:
                if len(bottomRightCandidates) == 1:
                    save.append('bottomright')
                else:
                    wires.append('bottomright')
            if c in bottomCandidates:
                if len(bottomCandidates) == 1:
                    save.append('bottom')
                else:
                    wires.append('bottom')

            if wires in open:
                for wire in wires:
                    save.append(wire)
            else:
                open.append(wires)

        #print('Save: ' + str(save))
        #print('Open: ' + str(open))

        if len(i) == 2:
            #print('Number: #1')
            result += '1'
            continue
        if len(i) == 4:
            #print('Number: #4')
            result += '4'
            continue
        if len(i) == 3:
            #print('Number: #7')
            result += '7'
            continue
        if len(i) == 7:
            #print('Number: #8')
            result += '8'
            continue
        if len(i) == 5:
            possibleNumbers = [2, 3, 5]
            tmpCandidate = []
            for possibleNumber in possibleNumbers:
                stillPossible = True
                for wire in save:
                    if wire not in numberToWires[possibleNumber]:
                        stillPossible = False
                if stillPossible:
                    tmpCandidate.append(possibleNumber)

            if len(tmpCandidate) == 1:
                #print('Number: #' + str(tmpCandidate[0]))
                result += str(tmpCandidate[0])
                continue
            else:
                #print('Number unclear')
                result = 'XXXX'
                break
        if len(i) == 6:
            possibleNumbers = [0, 6, 9]
            tmpCandidate = []
            for possibleNumber in possibleNumbers:
                stillPossible = True
                for wire in save:
                    if wire not in numberToWires[possibleNumber]:
                        stillPossible = False
                if stillPossible:
                    tmpCandidate.append(possibleNumber)

            if len(tmpCandidate) == 1:
                #print('Number: #' + str(tmpCandidate[0]))
                result += str(tmpCandidate[0])
                continue
            else:
                #print('Number unclear')
                result = 'XXXX'
                break
    if result == 'XXXX':
        #print(str(i) + ' => no clear result')
        unclear += 1
    else:
        #print(str(i) + ' => ' + result)
        sum += int(result)

print('Unclear lines: ' + str(unclear))
print('Total sum: ' + str(sum))



# Number to length and wires:
# 0 => 6, top, top left, top right, bottom left, bottom right, bottom
# 1 => 2, top right, bottom right
# 2 => 5, top, top right, middle, bottom left, bottom
# 3 => 5, top, top right, middle, bottom right, bottom
# 4 => 4, top left, top right, middle, bottom right
# 5 => 5, top, top left, middle, bottom right, bottom
# 6 => 6, top, top left, middle, bottom left, bottom right, bottom
# 7 => 3, top, top right, bottom right
# 8 => 7, top, top left, top right, middle, bottom left, bottom right, bottom
# 9 => 6, top, top left, top right, middle, bottom right, bottom
