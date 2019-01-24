def search(matrix, target):
    if not matrix or len(matrix[0]) == 0:
        return False

    m = 0
    n = len(matrix[0])

    while m < len(matrix) and matrix[m][n - 1] < target:
        m += 1
    if m < len(matrix):
        for i in range(n):
            if matrix[m][i] == target:
                print(m, i)
                return True


    return False



if __name__ == '__main__':
    matrix = [[1,3,5,7],
              [8,9,10,14],
              [15,16,17,20]]
    target = 13
    print(search(matrix, target))
