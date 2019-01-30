
def getLongestConsecutives(matrix):

    max_len = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_len = max(max_len, getMax(matrix, i , j))
            print(max_len)

    return max_len


def getMax(matrix, i, j):
    length = 1
    print(i, j, matrix[i][j])

    h = len(matrix)
    w = len(matrix[0])

    if i > len(matrix) - 1 or j > len(matrix[0]) - 1:
        return 0

    if i > 0 and matrix[i - 1][j] - 1 == matrix[i][j]:
        length += getMax(matrix, i - 1, j)
    if i < h -1 and matrix[i + 1][j] - 1 == matrix[i][j]:
        length += getMax(matrix, i + 1, j)
    if j > 0 and matrix[i][j-1] - 1 == matrix[i][j]:
        length += getMax(matrix, i, j - 1)
    if j < w - 1 and matrix[i][j+1] - 1 == matrix[i][j]:
        length += getMax(matrix, i, j + 1)


    return length

if __name__ == '__main__':
    matrix = [[2,3,9,10],
              [1,7,8,11],
              [6,4,5,12]]
    print(getLongestConsecutives(matrix))
