file = "input1.txt"

horizontal = 0
depth = 0
aim = 0

with open(file) as f:
    for line in f:
        lineSplit = line.split(" ")
        if "forward" in lineSplit[0]:
            horizontal += int(lineSplit[1])
            depth += int(lineSplit[1]) * aim

        if "down" in lineSplit[0]:
            #increase aim
            aim += int(lineSplit[1])

        if "up" in lineSplit[0]:
            #decrease aim
            aim -= int(lineSplit[1])

print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("Multiply: " + str(horizontal * depth))