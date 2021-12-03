def countbits(lineArray):
    bitcount = []  # counts [[1,3]] => first column, index 0 count 1, index 1 count 3
    init = False
    # count bit

    for line in lineArray:
        line = line.strip()

        if not init:
            for j in range(0, len(line)):
                bitcount.append([0, 0])
            init = True

        for i in range(0, len(line)):
            bitcount[i][int(line[i])] += 1
    #print('BitCount: ' + str(bitcount))
    return bitcount


def filetoarray(file):
    filearray = []
    with open(file) as f:
        for line in f:
            filearray.append(line.strip())
    return filearray
