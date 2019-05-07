import random
import time

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
        return row >=0 and row < 3 and col >=0 and col < 3 and self.grid[row][col] == '-' and not self.isBoardFull()

    def printBoard(self):
        for row in self.grid:
            print(row[0] + '|' + row[1] + '|' + row[2])
        print('_________________')

    def isBoardFull(self):
        return self.addCount >= 9


    def makeMove(self, row, col, token):
        return self.addTocken(row, col, token)


    def moveByAI(self):
        for i in range(10):
            x = random.randint(0,2)
            y = random.randint(0,2)

            if self.makeMove(i,i, "O"):
                self.printBoard()
            else:
                print("Invalid Move")

    def ramdomMove(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        while not self.makeMove(x,y, "O"):
            x = random.randint(0, 2)
            y = random.randint(0, 2)

    def isPlayerWon(self):
        return True

    def getMove(self):
        s = input("Your Move (X,Y) : ")
        return int(s.split(',')[0]), int(s.split(',')[1])



if __name__ == "__main__" :
    board = TTTBoard()
    board.printBoard()
    while not board.isBoardFull():
        x,y = board.getMove()
        while not board.isValid(x,y):
            print("Invalid Move")
            x, y = board.getMove()

        board.makeMove(x,y, "X")
        board.printBoard()
        time.sleep(3)
        print("Computer's Move")
        board.ramdomMove()
        board.printBoard()
        time.sleep(3)