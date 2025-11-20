def matrx_creation(p):
    print('\n введите матрицу коэфицентов кватратной матрицы 3x3, построчно.')
    matrixA=([0, 0, 0],[0, 0, 0],[0, 0, 0])
    for i in range (3):
        print(f'\n введите {i+1} строку матрицы (коэфиценты вводите через ","):')
        string = input()
        string = string.split(',')
        for j in range (3):
            if string[j].strip() == 'p':
                matrixA[i][j] = p
            else:
                matrixA[i][j] = int(string[j].strip())
    return matrixA

def answer_vector_creation():
    print('\n введите вектор ответов в одну строчку через запятую.')
    matrixB=([0],[0],[0])
    string=input()
    string=string.split(',')
    for i in range (3):
        matrixB[i][0]=int(string[i].strip())
    return matrixB

def var_creation():
    print('введите номера студентов через запятую.')
    string=input()
    string=string.split(',')
    for i in range (2):
        string[i]=int(string[i].strip())
    return sum(string)//10

def det3x3(matrix):
    x=[]
    x.append(1*matrix[0][0]*matrix[1][1]*matrix[2][2])
    x.append(1*matrix[0][1]*matrix[1][2]*matrix[2][0])
    x.append(1*matrix[0][2]*matrix[1][0]*matrix[2][1])
    x.append(-1*matrix[0][2]*matrix[1][1]*matrix[2][0])
    x.append(-1*matrix[0][0]*matrix[1][2]*matrix[2][1])
    x.append(-1*matrix[0][1]*matrix[1][0]*matrix[2][2])
    return sum(x)

def det2x2(matrix):
    x=[]
    x.append(1*matrix[0][0]*matrix[1][1])
    x.append(-1*matrix[0][1]*matrix[1][0])
    return sum(x)

def get_minor(matrix, row, col):
    minor=[[0,0],[0,0]]
    k=0
    for i in range(3):
        if i == row:
            continue
        x=0
        for j in range(3):
            if j == col:
                continue
            minor[k][x]=matrix[i][j]
            x += 1
        k += 1
    return minor

def minor_det_matrix(matrix):
    x=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            x[i][j]=(-1)**(i+j)*det2x2(get_minor(matrix, i, j))
    return x

def matrix_transposition(matrix):
    matrix_transponated=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            matrix_transponated[j][i]=matrix[i][j]
    return matrix_transponated

def inverse_matrix(matrix):
    det = det3x3(matrix)
    if det==0:
        return 'Обратной матрицы не существует.'
    else:
        in_matrix=matrix_transposition(minor_det_matrix(matrix))
        for i in range(3):
            for j in range(3):
                in_matrix[i][j]=in_matrix[i][j]/det
        return in_matrix

def inverse_matrix_for_print(matrix):
    det = det3x3(matrix)
    if det==0:
        return 'Обратной матрицы не существует.'
    else:
        in_matrix=matrix_transposition(minor_det_matrix(matrix))
        for i in range(3):
            for j in range(3):
                in_matrix[i][j]=f'{in_matrix[i][j]}/{det}'
        return in_matrix

def Kramer(matrixA, matrixB):
    detx = []
    ch = 0
    ans = []
    matrix = [[matrixA[i][j] for j in range(3)] for i in range(3)]
    det = det3x3(matrixA)
    for k in range(3):
        for i in range(3):
            for j in range(3):
                matrix[i][j] = matrixA[i][j]
        for i in range(3):
            matrix[i][k] = matrixB[i][0]
        detx.append(det3x3(matrix))
    if det == 0:
        for i in range(3):
            if detx[i] != 0:
                ch += 1
        if ch == 0:
            return 'Система не имеет решений (не совместна).'
        if ch != 0:
            return 'Система имеет бесконечное колличество решений.'
    else:
        for x in detx:
            ans.append(x / det)
        return ans


def Inverse_matrix_metod(matrixA, matrixB):
    if isinstance(matrixA, str):
        return matrixA
    Ans_Matrix = [[0], [0], [0]]
    for i in range(3):
        for j in range(3):
            Ans_Matrix[i][0] = Ans_Matrix[i][0] + matrixA[i][j] * matrixB[j][0]
    return Ans_Matrix

if __name__ == '__main__':
    var=var_creation()
    matrixA=matrx_creation(var)
    matrixB=answer_vector_creation()
    print('det =', det3x3(matrixA))
    print('A^(-1) =', inverse_matrix_for_print(matrixA))
    for i in range (3):
        mas=Kramer(matrixA, matrixB)
        print(f'x{i+1} =', mas[i])
    print('answer vector =', Inverse_matrix_metod(inverse_matrix(matrixA), matrixB))
