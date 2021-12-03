from utilities import countbits, filetoarray

file = "input1.txt"
lineArray = filetoarray(file)
bitCount = countbits(lineArray)

tmpBitArray = []
# oxygen generator rating -> most common
i = 0
while(len(lineArray) > 1):
    relevantBitValue = ''
    if bitCount[i][0] > bitCount[i][1]:
        relevantBitValue = '0'
    if bitCount[i][0] < bitCount[i][1]:
        relevantBitValue = '1'
    if bitCount[i][0] == bitCount[i][1]:
        relevantBitValue = '1'

    for bit in lineArray:
        if bit[i] == relevantBitValue:
            tmpBitArray.append(bit)

    lineArray = tmpBitArray
    tmpBitArray = []
    bitCount = countbits(lineArray)

    i += 1

oxygenBit = lineArray[0]
print('Oxygen generator rating bit: ' + oxygenBit)

lineArray = filetoarray(file)
bitCount = countbits(lineArray)

tmpBitArray = []
# co2 scrubber rating -> least common
i = 0
while(len(lineArray) > 1):
    relevantBitValue = ''
    if bitCount[i][0] > bitCount[i][1]:
        relevantBitValue = '1'
    if bitCount[i][0] < bitCount[i][1]:
        relevantBitValue = '0'
    if bitCount[i][0] == bitCount[i][1]:
        relevantBitValue = '0'

    for bit in lineArray:
        if bit[i] == relevantBitValue:
            tmpBitArray.append(bit)

    lineArray = tmpBitArray
    tmpBitArray = []
    bitCount = countbits(lineArray)

    i += 1

scrubberBit = lineArray[0]
print('CO2 scrubber rating bit: ' + scrubberBit)

# life supporting rate
oxygenValue = int(oxygenBit, 2)
scrubberValue = int(scrubberBit, 2)
print('Life supporting rate: ' + str(oxygenValue * scrubberValue))