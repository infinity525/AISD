import random, copy

#ввод матриц
K = int(input("K: "))
N = int(input("N: "))

#рандомное заполнение
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

#определение позиции
def chast(i, j):
    if i < j and i+j < N-1: return 4  # верх
    if i > j and i+j < N-1: return 1  # право
    if i > j and i+j > N-1: return 2  # низ
    if i < j and i+j > N-1: return 3  # лево
    return 0

#вывод матрицы
def matrica(M, name):
    print(f"\n{name}:")
    for row in M: print(*[f"{x:4}" for x in row])

matrica(A, "A")

F = copy.deepcopy(A)

nuli = sum(1 for i in range(N) for j in range(N) if j%2==1 and chast(i,j)==4 and A[i][j]==0)
prod  = 1
for i in range(N):
    for j in range(N):
        if i%2==1 and chast(i,j)==1: prod *= A[i][j]

c1 = [(i,j) for i in range(N) for j in range(N) if chast(i,j)==1]
c2 = [(i,j) for i in range(N) for j in range(N) if chast(i,j)==2]
c3 = [(i,j) for i in range(N) for j in range(N) if chast(i,j)==3]

if nuli * K > prod:  #симметрично меняются части 1 и 2
    for (i,j) in c1:
        F[i][j], F[j][i] = F[j][i], F[i][j]
else:                 #нессиметрично меняются части 2 и 3
    for (i2,j2),(i3,j3) in zip(c2,c3):
        F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]

#вывод
matrica(F, "F")

result_AF  = [[sum(A[i][k]*F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
matrica(result_AF, "A*F")

result_KFT = [[K*F[j][i] for j in range(N)] for i in range(N)]
matrica(result_KFT, "K*F^T")

result = [[result_AF[i][j]+result_KFT[i][j] for j in range(N)] for i in range(N)]
matrica(result, "A*F + K*F^T")
