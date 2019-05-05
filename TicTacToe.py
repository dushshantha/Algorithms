import random

class TTTBoard:
    def __init__(self):
        self.grid = [['-' for x in range(3)] for y in range(3)]
        self.addCount = 0


    def addTocken(self, row, col, token):
        if self.isValid(row, col):
            self.grid[row][col] = token
            self.addCount += 1
            return True
        return False


    def isValid(self, row, col):
        return row >=0 and row < 3 and col >=0 and col < 3 and self.grid[row][col] == '-'

    def printBoard(self):
        for row in self.grid:
            print(row[0] + '|' + row[1] + '|' + row[2])
        print('_________________')

    def isBoardFull(self):
        return self.addCount >= 9


    def makeMove(self, row, col, token):
        if not self.addTocken(row, col, token):
            raise Exception("Invalid Move")
        return True


    def moveByAI(self):
        for i in range(10):
            x = random.randint(0,2)
            y = random.randint(0,2)
            try:
                self.makeMove(i,i, "Y")
                self.printBoard()
            except Exception as e:
                print("Invalid Move")


if __name__ == "__main__" :
    board = TTTBoard()
    board.addTocken(0,1,'X')
    board.printBoard()

    #board.makeMove(0,1,'X')
    board.moveByAI()


