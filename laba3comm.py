import random, copy

K = int(input("K: "))
N = int(input("N: "))

# Случайное заполнение матрицы A размером N×N значениями от -10 до 10
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

def area(i, j):
    """
    Определяет, в какой области квадратной матрицы находится элемент (i, j).
    Матрица делится диагоналями на 4 треугольные области + сами диагонали:
      0 — главная или побочная диагональ
      1 — правый треугольник   (i > j  и  i + j < N-1)
      2 — нижний треугольник   (i > j  и  i + j > N-1)
      3 — левый треугольник    (i < j  и  i + j > N-1)
      4 — верхний треугольник  (i < j  и  i + j < N-1)
    """
    if i < j and i + j < N - 1: return 4  # верх
    if i < j and i + j > N - 1: return 3  # лево
    if i > j and i + j > N - 1: return 2  # низ
    if i > j and i + j < N - 1: return 1  # право
    return 0                               # на диагонали

def show(M, name):
    """Вывод матрицы M с заголовком name, каждое число занимает 4 символа."""
    print(f"\n{name}:")
    for row in M: print(*[f"{x:4}" for x in row])

show(A, "A")

# F — рабочая копия A; будем менять F, не трогая оригинал A
F = copy.deepcopy(A)

# Считаем количество нулей в верхнем треугольнике (область 4) в нечётных столбцах (j % 2 == 1)
zeros = sum(1 for i in range(N) for j in range(N) if j%2==1 and area(i,j)==4 and A[i][j]==0)

# Считаем произведение элементов правого треугольника (область 1) в нечётных строках (i % 2 == 1)
prod = 1
for i in range(N):
    for j in range(N):
        if i%2==1 and area(i,j)==1: prod *= A[i][j]

# Собираем координаты всех элементов каждой из трёх областей
c1 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==1]  # правый треугольник
c2 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==2]  # нижний треугольник
c3 = [(i,j) for i in range(N) for j in range(N) if area(i,j)==3]  # левый треугольник

if zeros * K > prod:
    # Ветка 1: симметричный обмен области 1 (право) и области 2 (низ) относительно побочной диагонали.
    # Элемент (i, j) симметричен элементу (N-1-j, N-1-i) по побочной диагонали.
    for (i,j) in c1:
        mi, mj = N-1-j, N-1-i
        F[i][j], F[mi][mj] = F[mi][mj], F[i][j]
else:
    # Ветка 2: несимметричный попарный обмен элементов области 2 (низ) и области 3 (лево).
    # Элементы берутся в том порядке, в каком они были собраны в c2 и c3.
    for (i2,j2),(i3,j3) in zip(c2,c3):
        F[i2][j2], F[i3][j3] = F[i3][j3], F[i2][j2]

show(F, "F")

# A*F — обычное матричное произведение: элемент [i][j] = скалярное произведение i-й строки A и j-го столбца F
AF  = [[sum(A[i][k]*F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
show(AF, "A*F")

# K*F^T — транспонирование F (индексы i и j меняются местами: F[j][i] вместо F[i][j]),
# умноженное на скаляр K. Всё делается в одну строку через list comprehension.
KFT = [[K*F[j][i] for j in range(N)] for i in range(N)]
show(KFT, "K*F^T")

# Итоговая матрица: поэлементная сумма A*F и K*F^T
R = [[AF[i][j]+KFT[i][j] for j in range(N)] for i in range(N)]
show(R, "A*F + K*F^T")
