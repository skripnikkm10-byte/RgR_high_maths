def matrix_creation():
    matrixA = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    print('\n введите матрицу коэфицентов матрицы, построчно.')
    for i in range (3):
        print(f'\n введите {i + 1} строку матрицы (коэфиценты вводите через ","):')
        string = input()
        string = string.split(',')
        for j in range (4):
            matrixA[i][j] = int(string[j].strip())
    return matrixA

def answer_creation_matrix():
    print('\n введите вектор ответов в одну строчку через запятую.')
    matrixB=([0],[0],[0])
    string=input()
    string=string.split(',')
    for i in range (3):
        matrixB[i][0]=int(string[i].strip())
    return matrixB

def Trap_vew(matrixA, matrixB):
    if not hasattr(matrixB[0], '__len__'):
        matrixB = [[x] for x in matrixB]
    if matrixA[0][0] == 0 and (matrixB[1][0] != 0 or matrixA[2][0] != 0):
        if matrixA[1][0] != 0:
            for i in range(4):
                matrixA[0][i], matrixA[1][i] = matrixA[1][i], matrixA[0][i]
            matrixB[0][0], matrixB[1][0] = matrixB[1][0], matrixB[0][0]
        else:
            for i in range(4):
                matrixA[0][i], matrixA[2][i] = matrixA[2][i], matrixA[0][i]
            matrixB[0][0], matrixB[2][0] = matrixB[2][0], matrixB[0][0]
    if matrixA[0][0] == 0:
        return matrixA, matrixB
    pivot = matrixA[0][0]
    for i in range(4):
        matrixA[0][i] /= pivot
    matrixB[0][0] /= pivot
    for row in [1, 2]:
        if matrixA[row][0] != 0:
            factor = matrixA[row][0]
            for i in range(4):
                matrixA[row][i] -= factor * matrixA[0][i]
            matrixB[row][0] -= factor * matrixB[0][0]
    if matrixA[1][1] == 0 and matrixA[2][1] != 0:
        for i in range(4):
            matrixA[1][i], matrixA[2][i] = matrixA[2][i], matrixA[1][i]
        matrixB[1][0], matrixB[2][0] = matrixB[2][0], matrixB[1][0]
    if matrixA[1][1] != 0:
        pivot = matrixA[1][1]
        for i in range(1, 4):
            matrixA[1][i] /= pivot
        matrixB[1][0] /= pivot
        if matrixA[2][1] != 0:
            factor = matrixA[2][1]
            for i in range(1, 4):
                matrixA[2][i] -= factor * matrixA[1][i]
            matrixB[2][0] -= factor * matrixB[1][0]
    if matrixA[2][2] != 0:
        pivot = matrixA[2][2]
        matrixA[2][3] /= pivot
        matrixB[2][0] /= pivot
    return matrixA, matrixB


def FSR(matrixA, matrixB):
