from dataclasses import dataclass
f = open("d4.data")
numbers = f.readline().split(",")

@dataclass
class boardNumber:
    number: str
    marked: bool

def getBoards():
    boards = []
    for line in f:
        line = line.strip()
        if line == "":
            boards.append([])
            continue
        numbers = [boardNumber(number=num, marked=False) for num in line.replace("  ", " ").split(" ")]
        boards[-1].append(numbers)
    return boards


boards = getBoards()

def markNumber(number, board):
    for line in board:
        for num in line:
            if num.number == number:
                num.marked = True

def isLineWinning(line):
    lineMarked = True
    for num in line:
        lineMarked &= num.marked
    if lineMarked:
        return True


def HasBoardWon(board):
    for rowNumber in range(len(board)):
        row = board[rowNumber]
        column = [line[rowNumber] for line in board]
        if isLineWinning(row) or isLineWinning(column):
            return True
    return False
                


# markNumber("4", boards[-1])
# markNumber("19", boards[-1])
# markNumber("20", boards[-1])
# markNumber("5", boards[-1])

# print(HasBoardWon(boards[-1]))
# markNumber("7", boards[-1])
# print(HasBoardWon(boards[-1]))

def getWinningBoardsAndNumbers():
    winningBoards = []
    winningNumbers = []
    done = False
    for number in numbers:
        for board in boards:
            if board in winningBoards:
                continue
            markNumber(number, board)
            if HasBoardWon(board):
                winningBoards.append(board)
                winningNumbers.append(number)
        if len(winningBoards) == len(boards):
            break
    return winningBoards, winningNumbers
        
def getUnmarkedNumbers(board):
    totalSum = 0
    for line in board:
        totalSum += sum([int(n.number) for n in line if not n.marked])
    return totalSum
    
winningBoards, winningNumbers = getWinningBoardsAndNumbers()
        
print(int(winningNumbers[0]) * getUnmarkedNumbers(winningBoards[0]))
print(int(winningNumbers[-1]) * getUnmarkedNumbers(winningBoards[-1]))






# for board in boards:
#     markNumber
#     for line in board:
#         print(line)
#     print()
