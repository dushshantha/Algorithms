'''
Imagine a robot sitting on the upper left corner of a grid. Robot can only move in 2 directions.
Right and Down. but certain cells are restricted. Design an algorithm that find a path for the robot
to move from top left to bottom right.
'''

def getPath(grid):
    r = len(grid) 
    c = len(grid[0])
    memo = [[False] * c for i in range(r)]

    memo[r - 1][c - 1] = True

    for i in range(c-2, -1, -1):
        if grid[-1][i] == 1:
            print(i)
            memo[-1][i] = memo[-1][i + 1]

    for i in range(r-2, -1, -1):
        if grid[i][-1] == 1:
            print(i)
            memo[i][-1] = memo[i +1][-1]
    
    
    for i in range(r - 2, -1, -1):
        for j in range(c - 2, -1, -1):
            if grid[i][j] == 1:
                memo[i][j] = memo[i + 1][j] or memo[i][j + 1]

    return memo[0][0], constructPath(memo)

def constructPath(memo):
    if not memo[0][0]:
        return []
    
    ret = [(0,0)]
    i , j = 0, 0
    while i < len(memo) - 1 or j < len(memo[0]) - 1:
        if memo[i][j + 1]:
            ret.append((i, j + 1))
            j += 1
        elif memo[i + 1][j]:
            ret.append((i +1, j))
            i += 1

    return ret
    

grid = [ [1,1,1,1],
         [0,0,1,0],
         [1,1,1,0],
         [0,0,1,1]
        ]

print(getPath(grid))

grid = [ [1,0,1,1],
         [0,0,1,0],
         [1,1,1,0],
         [0,0,1,1]
        ]

print(getPath(grid))

grid = [ [1,1,0,1],
         [0,1,0,0],
         [1,1,0,0],
         [0,1,1,1]
        ]

print(getPath(grid))