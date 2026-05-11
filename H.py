import random
import copy

K = int(input("K: "))
N = int(input("N: "))

A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

def chast(i, j):
    if i < j and i + j < N - 1:
        return 4  # верх
    if i < j and i + j > N - 1:
        return 3  # лево
    if i > j and i + j > N - 1:
        return 2  # низ
    if i > j and i + j < N - 1:
        return 1  # право
    return 0

def matrica(M, name):
    print(f"\n{name}:")
    for row in M:
        print(*[f"{x:4}" for x in row])

matrica(A, "A")

F = copy.deepcopy(A)

count_k = sum(
    1
    for i in range(N)
    for j in range(N)
    if j % 2 == 0 and chast(i, j) == 1 and A[i][j] == K
)

prod = 1
for i in range(N):
    for j in range(N):
        if i % 2 == 1 and chast(i, j) == 4:
            prod *= A[i][j]

c1 = [(i, j) for i in range(N) for j in range(N) if chast(i, j) == 1]
c2 = [(i, j) for i in range(N) for j in range(N) if chast(i, j) == 2]
c3 = [(i, j) for i in range(N) for j in range(N) if chast(i, j) == 3]

if count_k > prod:
    for (i2, j2), (i3, j3) in zip(c2, c3):
        F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]
else:
    for (i1, j1), (i2, j2) in zip(c1, c2):
        F[i1][j1], F[i2][j2] = F[i2][j2], F[i1][j1]

matrica(F, "F")

AF = [[sum(A[i][k] * F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
matrica(AF, "A*F")

KAF = [[K * AF[i][j] for j in range(N)] for i in range(N)]
matrica(KAF, "K*(A*F)")

FT = [[F[j][i] for j in range(N)] for i in range(N)]
matrica(FT, "F^T")

result = [[sum(KAF[i][k] * FT[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
matrica(result, "K*(A*F)*F^T")
