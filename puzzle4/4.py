from utilities import filetoarray

# class Board
# rows = [[row1], [row2], [row3], [row4], [row5]]
# to mark a number => *(-1)

class Board:
    def __init__(self):
        self.rows = []
        self.columnCount = []
        self.rowCount = []
        self.numbers = []
        self.markedNumbers = []
        self.hasFinished = False

    def containsnumber(self, number):
        return number in self.numbers

    def createBoard(self, numberInput):
        for row in numberInput:
            split = row.split(' ')
            self.rowCount.append(0)
            self.columnCount.append(0)
            for i in range (0, len(split)):
                split[i] = int(split[i])
                self.numbers.append(int(split[i]))
            self.rows.append(split)

    def marknumber(self, numberValue):
        self.markedNumbers.append(numberValue)
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                if self.rows[i][j] == numberValue:
                    self.rowCount[i] += 1
                    self.columnCount[j] += 1

    def checkwin(self):
        return 5 in self.rowCount or 5 in self.columnCount

    def getscore(self, number):
        sum = 0
        for n in self.numbers:
            if not n in self.markedNumbers:
                sum += n

        return sum * number

    def clearmarks(self):
        for i in range(0, len(self.rowCount)):
            self.rowCount[i] = 0
            self.columnCount[i] = 0
        self.markedNumbers = []


file = "input1.txt"
lines = filetoarray(file)
numbers = lines[0].split(',')

# create boards
boards = []
j = 1
while j < len(lines) - 5:
    numberInput = []
    for i in range(1, 6):
        numberInput.append(lines[j + i])

    b = Board()
    b.createBoard(numberInput)
    boards.append(b)
    j += 6

# pick numbers from list, check for win and calculate score
# 4a
winner = False
i = 0
while not winner:
    number = numbers[i]
    numberValue = int(number)
    for board in boards:
        if board.containsnumber(numberValue):
            board.marknumber(numberValue)
            if board.checkwin():
                print("[4a] Winner's score: " + str(board.getscore(numberValue)))
                winner = True
        if winner:
            break
    i += 1

# clear boards
for board in boards:
    board.clearmarks()

# 4b
lastWinner = False
i = 0
finishedBoards = []
while len(finishedBoards) < len(boards):
    number = numbers[i]
    numberValue = int(number)
    for board in boards:
        if board.hasFinished:
            continue
        if board.containsnumber(numberValue):
            board.marknumber(numberValue)
            if board.checkwin():
                board.hasFinished = True
                if len(finishedBoards) + 1 == len(boards):
                    # last winner
                    print("[4b] Last winner score: " + str(board.getscore(numberValue)))
                finishedBoards.append(board)
    i += 1