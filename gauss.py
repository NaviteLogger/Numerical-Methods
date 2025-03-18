import numpy as np

MAXN = 100


def partial_pivot(A, n):
    for i in range(n):
        pivot_row = i

        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot_row][i]):
                pivot_row = j

        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]


def back_substitute(A, n):
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_val = sum(A[i][j] * x[j] for j in range(i + 1, n))

        x[i] = (A[i][n] - sum_val) / A[i][i]
    return x


if __name__ == "__main__":
    n = 3

    A = np.array([[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]])

    partial_pivot(A, n)
    x = back_substitute(A, n)

    print("Rozwiązanie dla układu to:")
    for i in range(n):
        print(x[i])
