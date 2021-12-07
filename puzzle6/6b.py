from utilities import filetoarray

def newtmpbucket(length):
    tmpbucket = []
    for i in range(0, length):
        tmpbucket.append(0)
    return tmpbucket

def countfish(buckets):
    count = 0
    for i in range(0, len(buckets)):
        count += buckets[i]
    return count

file = "input1.txt"
lines = filetoarray(file)

relevant = lines[0]
print(relevant)
buckets = []
tmpBuckets = []
for i in range(0,9):
    buckets.append(0)
    tmpBuckets.append(0)

for i in relevant.split(','):
    index = int(i)
    buckets[index] += 1

print(buckets)

generations = 256
printGenerations = 0
k = 0
while k <= generations:

    for i in range(0, len(buckets)):
        if i == 0:
            tmpBuckets[8] += buckets[i]
            tmpBuckets[6] += buckets[i]
        else:
            tmpBuckets[i-1] += buckets[i]

    buckets = tmpBuckets

    if k <= 18:
        print('After ' + str(k+1) + ' days: ' + str(countfish(buckets)) + ' fish -> ' + str(buckets))
    else:
        print('After ' + str(k + 1) + ' days: ' + str(countfish(buckets)) + ' fish')

    tmpBuckets = newtmpbucket(len(buckets))
    k += 1

