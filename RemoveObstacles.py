import collections

def getLongestConsecutives(matrix):

    cache = {}
    
    length = getMax(cache, matrix, 0 ,0)
    if length == 999999: 
        return -1
    return length


def getMax(cache, matrix, i, j):
    if str(i)+','+str(j) in cache:
        return cache[str(i)+','+str(j)]

    if matrix[i][j] == 0:
        return 999999
    if matrix[i][j] == 9:
        return 0
    
    length = 1
    print(i, j, matrix[i][j])

    h = len(matrix)
    w = len(matrix[0])

    if i > len(matrix) - 1 or j > len(matrix[0]) - 1:
        return -1

    t = 999999

    if i > 0 and matrix[i - 1][j] != 0:
        t = min(t, getMax(cache, matrix, i - 1, j))
    if i < h -1 and matrix[i + 1][j] != 0:
        t = min(t, getMax(cache, matrix, i + 1, j))
    if j > 0 and matrix[i][j-1] != 0:
        t = min(t, getMax(cache, matrix, i, j - 1))
    if j < w - 1 and matrix[i][j+1] != 0:
        t = min(t, getMax(cache, matrix, i, j + 1))

    cache[str(i)+','+str(j)] = length
    if t != 999999:
        return len + t
    else:
        return 999999
    
    

if __name__ == '__main__':
    matrix = [[1,0,0,0],
              [1,0,0,0],
              [1,9,0,0]]
    print(getLongestConsecutives(matrix))