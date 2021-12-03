from utilities import countbits, filetoarray

file = "example1.txt"
lineArray = filetoarray(file)
bitCount = countbits(lineArray)

#calculate gamma
gammaBin = ''
for i in range(0, len(bitCount)):
    if bitCount[i][0] > bitCount[i][1]:
        gammaBin += '0'
    if bitCount[i][0] < bitCount[i][1]:
        gammaBin += '1'

print('Gamma: ' + gammaBin)

#calculate epsilon
epsBin = ''
for i in range(0, len(bitCount)):
    if bitCount[i][0] < bitCount[i][1]:
        epsBin += '0'
    if bitCount[i][0] > bitCount[i][1]:
        epsBin += '1'

print('Epsilon: ' + epsBin)

#calculate final
gammaValue = int(gammaBin, 2)
epsValue = int(epsBin, 2)
print("Power Consumption: " + str(gammaValue * epsValue))