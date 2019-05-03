import random

line = [''] * 9
realBoard = []
myBoard = []
length = 9
number = 10
winningCount = (length * length) - number
clearCount = 0
won = True
mines = []

#realBoard[2][5] = 1
def init(length):
    global realBoard
    global myBoard
    global number

    realBoard = [[' ' for x in range(length)] for y in range(length)]
    myBoard   = [['0' for x in range(length)] for y in range(length)]
    getRandomMines(number)
    printBoard(realBoard)
    print('_________________________')

def printBoard(board):
    for line in board:
        print(line, '\n')
    print('__________________________')

def isValid(x, y, board):
    return x >=0 and x < length and y >= 0 and y < length

def isMine(x, y):
    if realBoard[x][y] == '*':
        return True
    return False

def countAdjesantMines(row, col):
    global realBoard
    count = 0

    '''
    Count all the mines in the 8 adjacent
        cells

            N.W   N   N.E
              \   |   /
               \  |  /
            W----Cell----E
                 / | \
               /   |  \
            S.W    S   S.E

        Cell-->Current Cell (row, col)
        N -->  North        (row-1, col)
        S -->  South        (row+1, col)
        E -->  East         (row, col+1)
        W -->  West         (row, col-1)
        N.E--> North-East   (row-1, col+1)
        N.W--> North-West   (row-1, col-1)
        S.E--> South-East   (row+1, col+1)
        S.W--> South-West   (row+1, col-1)
    '''

    # 1st
    if isValid(row-1, col, realBoard):
        if isMine(row-1, col):
            count += 1

    # 2
    if isValid(row+1, col, realBoard):
        if isMine(row+1, col):
            count += 1

    # 3
    if isValid(row, col+1, realBoard):
        if isMine(row, col+1):
            count += 1

    # 4
    if isValid(row, col-1, realBoard):
        if isMine(row, col-1):
            count += 1

    # 5
    if isValid(row-1, col+1, realBoard):
        if isMine(row-1, col+1):
            count += 1

    # 6
    if isValid(row-1, col-1, realBoard):
        if isMine(row-1, col-1):
            count += 1

    # 7
    if isValid(row+1, col+1, realBoard):
        if isMine(row+1, col+1):
            count += 1

    # 8
    if isValid(row+1, col-1, realBoard):
        if isMine(row+1, col-1):
            count += 1

    return count


def getRandomMines(number):

    global realBoard
    global length
    global mines

    x = random.randint(0, length - 1)
    y = random.randint(0, length - 1)
    for i in range(number):
        while realBoard[x][y] == '*':
            x = random.randint(0, length - 1)
            y = random.randint(0, length - 1)
        realBoard[x][y] = '*'
        mines.append([x,y])

    
def makeMove():
    s = input('Emter your move (row, col): ')
    l = s.split(',')
    return int(l[0]), int(l[1])

def playMineSweep(row, col):
    global realBoard
    global myBoard
    global number
    global clearCount
    global winningCount
    global won

    if myBoard[row][col] == '_':
        return

    # GAME OVER
    if realBoard[row][col] == '*':
        #First Move
        if clearCount == 0:
            realBoard[row][col] = '_'
            x = random.randint(0, length - 1)
            y = random.randint(0, length - 1)
            while realBoard[x][y] == '*':
                x = random.randint(0, length - 1)
                y = random.randint(0, length - 1)
            realBoard[x][y] = '*'
            mines.append([x,y])

            for i in range(len(mines)):
                if mines[i][0] == row and mines[i][1] == col:
                    mines.pop(i)
                    break
            printBoard(realBoard) 
            playMineSweep(row,col)

        else:
            myBoard[row][col] = '*'

            for i in range(number):
                myBoard[mines[i][0]][mines[i][1]] = '*'
            #printBoard(myBoard)
            won = False
            
    else:
        count = countAdjesantMines(row, col)
        if count == 0:
            myBoard[row][col] = '_'
            clearCount += 1
            # 1st
            if isValid(row-1, col, realBoard):
                playMineSweep(row-1, col)

            # 2
            if isValid(row+1, col, realBoard):
                playMineSweep(row+1, col)

            # 3
            if isValid(row, col+1, realBoard):
                playMineSweep(row, col+1)

            # 4
            if isValid(row, col-1, realBoard):
                playMineSweep(row, col-1)

            # 5
            if isValid(row-1, col+1, realBoard):
                playMineSweep(row-1, col+1)

            # 6
            if isValid(row-1, col-1, realBoard):
                playMineSweep(row-1, col-1)

            # 7
            if isValid(row+1, col+1, realBoard):
                playMineSweep(row+1, col+1)

            # 8
            if isValid(row+1, col-1, realBoard):
                playMineSweep(row+1, col-1)

        else:
            myBoard[row][col] = str(count)
            clearCount += 1



if __name__ == '__main__':
    init(length)
    # Game Loop
    while won and clearCount < winningCount:
        row, col = makeMove()
        playMineSweep(row, col)
        printBoard(myBoard)
    
    if won:
        #print(winningCount, clearCount)
        print("CONGRATZ !!! YOU WON")  
    else:
        print('YOU LOST')