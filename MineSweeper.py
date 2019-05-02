line = [''] * 9
realBoard = []
myBoard = []
length = 9
#realBoard[2][5] = 1
def init(length):
    realBoard = [['' for x in range(length)] for y in range(length)]
    myBoard   = [['' for x in range(length)] for y in range(length)]
    printBoard(realBoard)

def printBoard(board):
    for line in board:
        print(line, '\n')

def isValid(x, y, board):
    return x >=0 and x < length and y >= 0 and y < lngth

def isMine(x, y):
    if realBoard[x][y] == '*':
        return True
    return False

def countAdjesantMines(row, col):
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


def makeMove():

    x = input("row ")
    y = input("col ")
    return x, y



if __name__ == '__main__':
    makeMove()
    init(9)
