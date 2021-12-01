input  = "input1.txt"

depthReadings = []
changes = []        # 1 = increase, 0 = no change, -1 = decrease

with open(input) as f:
    for l in f:
        depthReadings.append(int(l.strip()))

i = 1
changes.append(0)
while i < len(depthReadings):
    if depthReadings[i] < depthReadings[i-1]:
        changes.append(-1)
    if depthReadings[i] > depthReadings[i-1]:
        changes.append(1)
    if depthReadings[i] == depthReadings[i-1]:
        changes.append(0)

    i += 1

# count
counts = {}
for change in changes:
    if change not in counts:
        counts[change] = 1
    else:
        counts[change] += 1

print(counts)
