
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
    for j in range (3):
        x.append(1)
    for j in range (3):
        x.append(-1)
    for i in range (3):
        for j in range (3):
            if i==j:
                x[0]=x[0]*matrix[i][j]
            if i==j+1 or i==j-2:
                x[1]=x[1]*matrix[i][j]
            if i==j+2 or i==j-1:
                x[2]=x[2]*matrix[i][j]
            if i==j+2 or i==j-2 or (i==1 and j==1):
                x[3]=x[3]*matrix[i][j]
            if (i==0 and j==0) or (i==2 and j==1) or (i==1 and j==2):
                x[4]=x[4]*matrix[i][j]
            if (i==1 and j==0) or (i==0 and j==1) or (i==2 and j==2):
                x[5]=x[5]*matrix[i][j]
    return sum(x)

def det2x2(matrix): #TODO
    x=[]
    for i in range (2):
        for j in range (2):
            if i==j and len(x)==0:
                x.append(matrix[i][j])
            elif i==j:
                x[0]=x[0]*matrix[i][j]
            if (i==j+1 or i==j-1) and len(x)==1:
                x.append(matrix[i][j])
            elif i==j+2 or i==j-2:
                x[1]=x[1]*matrix[i][j]
    x[1]=x[1]*-1
    return sum(x)
def get_minor(matrix, row, col):
    minor=[[0,0],[0,0]]
    k=0
    x=0
    for i in range(3):
        for j in range(3):
            if i!=row and j!=col:
                minor[k][x]=matrix[i][j]
                if x<k:
                    x-=1
                    k+=1
                else:
                    x+=1
        return minor

def minor_det_matrix(matrix):
    x=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            x[i][j]=matrix[i][j]*det2x2(get_minor(matrix, i, j))
    return x

def matrix_transposition(matrix):
    matrix_transponated=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            matrix_transponated[j][i]=matrix[i][j]
    return matrix_transponated

def inverse_matrix(matrix):
    det = det3x3(matrix)
    in_matrix = []
    if det==0:
        return 'Обратной матрицы не существует.'
    else:
        in_matrix=matrix_transposition(minor_det_matrix(matrix))
        for i in range(3):
            for j in range(3):
                in_matrix[i][j]=in_matrix[i][j]/det
        return in_matrix

def Kramer(matrixA, matrixB):
    detx=[]
    ch=0
    ans=[]
    matrix=matrixA
    det=det3x3(matrixA)
    for k in range(3):
        for i in range(3):
            matrix[i][k]=matrixB[i][0]
            detx.append(det3x3(matrix))
        matrix=matrixA
    if det == 0:
        for i in range(3):
            if detx[i]!=0:
                ch+=1
        if ch==0:
            return 'Система не имеет решений (не совместна).'
        if ch!=0:
            return 'Система имеет бесконечное колличество решений.'
    else:
        for x in detx:
            ans.append(x/det)
        return ans
