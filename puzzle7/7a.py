from utilities import filetoarray

file = "example1.txt"
lines = filetoarray(file)

relevant = lines[0]

min = 9999999
max = 0
numbers = []

for position in range(0, len(relevant.split(','))):
    number = int(relevant.split(',')[position])
    numbers.append(number)
    if number < min:
        min = number
    if number > max:
        max = number

#print(numbers)
#print(min)
#print(max)

minFuel = 999999
bestPosition = -1
for position in range(min, max + 1):
    fuel = 0
    for j in numbers:
        steps = abs(j - position)
        fuel += steps

    if fuel < minFuel:
        minFuel = fuel
        bestPosition = position

print('MinFuel: ' + str(minFuel))
print('Best Position: ' + str(bestPosition))