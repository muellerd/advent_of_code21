from utilities import filetoarray

file = "input1.txt"
lines = filetoarray(file)

count = 0
for line in lines:
    lineSplit = line.split('|')
    digitString = lineSplit[1].strip()
    digitStringSplit = digitString.split(' ')
    for digit in digitStringSplit:
        if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
            count += 1

print("Number of 1, 4, 7 or 8: " + str(count))