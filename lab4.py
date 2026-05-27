import numpy as np
import matplotlib.pyplot as plt

K, N = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(N)])

print("A:\n", A)

half = N // 2
D = A[:half, :half]
E = A[:half, half:]
C = A[half:, :half]
B = A[half:, half:]

F = A.copy()

odd_cols = [j for j in range(half) if j % 2 == 1]
zero_count = 0
for i in range(half):
    for j in odd_cols:
        if E[i, j] == 0:
            zero_count += 1

odd_rows = [i for i in range(half) if i % 2 == 1]
product_odd = 1
for i in odd_rows:
    for j in range(half):
        product_odd *= E[i, j]

if zero_count * K > product_odd:
    print("Меняем B и C симметрично")
    F[half:, :half] = B
    F[half:, half:] = C
else:
    print("Меняем B и E несимметрично")
    F[:half, half:] = B
    F[half:, half:] = E

print("F:\n", F)

plt.figure(figsize=(14, 4))

plt.subplot(131)
plt.imshow(F, cmap='cool')
plt.title('Матрица F')
plt.colorbar()

plt.subplot(132)
plt.plot(np.mean(F, axis=0), marker='o', label='Среднее по столбцам')
plt.plot(np.mean(F, axis=1), marker='s', label='Среднее по строкам')
plt.title('Средние значения матрицы F')
plt.xlabel('Индекс')
plt.ylabel('Среднее значение')
plt.legend()
plt.grid(True)

plt.subplot(133)
plt.hist(F.flatten(), bins=20, edgecolor='black', alpha=0.7, color='teal')
plt.title('Гистограмма элементов F')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)

plt.tight_layout()
plt.show()

detA = np.linalg.det(A)
sum_diag_F = np.trace(F)

if detA > sum_diag_F:
    print("detA > sum_diag_F: A * A^T - K * F^{-1}")
    result = A @ A.T - K * np.linalg.inv(F)
else:
    print("detA <= sum_diag_F: (A^{-1} + G - F^T) * K")
    G = np.tril(A)
    result = (np.linalg.inv(A) + G - F.T) * K

print("Результат:\n", result)
