import random, copy

K = int(input("K: "))
N = int(input("N: "))

# A = [
#     [ 0,  2,  7,  3,  1],
#     [ 5,  0,  4,  0,  2],
#     [-3,  7,  0,  1,  6],
#     [ 0,  2,  7,  0, -1],
#     [ 4, -5,  3,  2,  0],
# ]

# Случайное заполнение:
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

def area(i, j):
    if i < j and i + j < N - 1: return 4  # верх
    if i < j and i + j > N - 1: return 3  # лево
    if i > j and i + j > N - 1: return 2  # низ
    if i > j and i + j < N - 1: return 1  # право
    return 0

def show(M, name):
    print(f"\n{name}:")
    for row in M: print(*[f"{x:4}" for x in row])

show(A, "A")

F = copy.deepcopy(A)

zeros = sum(1 for i in range(N) for j in range(N) if j%2==1 and area(i,j)==4 and A[i][j]==0)
prod  = 1
for i in range(N):
    for j in range(N):
        if i%2==1 and area(i,j)==1: prod *= A[i][j]

c1 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==1]
c2 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==2]
c3 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==3]

if zeros * K > prod:  # симметрично меняем обл.1 и 2 (по побочной диагонали)
    for (i,j) in c1:
        mi, mj = N-1-j, N-1-i
        F[i][j], F[mi][mj] = F[mi][mj], F[i][j]
else:                 # несимметрично меняем обл.2 и 3
    for (i2,j2),(i3,j3) in zip(c2,c3):
        F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]

show(F, "F")

AF  = [[sum(A[i][k]*F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
show(AF, "A*F")

KFT = [[K*F[j][i] for j in range(N)] for i in range(N)]
show(KFT, "K*F^T")

R = [[AF[i][j]+KFT[i][j] for j in range(N)] for i in range(N)]
show(R, "A*F + K*F^T")
