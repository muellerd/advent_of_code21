file = "input1.txt"

horizontal = 0
depth = 0

with open(file) as f:
    for line in f:
        lineSplit = line.split(" ")
        if "forward" in lineSplit[0]:
            horizontal += int(lineSplit[1])

        if "down" in lineSplit[0]:
            #increase depth
            depth += int(lineSplit[1])

        if "up" in lineSplit[0]:
            #decrease depth
            depth -= int(lineSplit[1])

print("Horizontal: " + str(horizontal))
print("Depth: " + str(depth))
print("Multiply: " + str(horizontal * depth))