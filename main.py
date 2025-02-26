addition_result = [[0,0,0],[0,0,0],[0,0,0]]
multiplication_result = [[0,0,0],[0,0,0],[0,0,0]]

def two_matrix_addition(matrix1, matrix2):
    for i in range(len(matrix1)): # To zwróci liczbę wierszy
        for j in range(len(matrix1[0])): # To zwróci liczbę kolumn
            addition_result[i][j] += matrix1[i][j] + matrix2[i][j]

def two_matrix_multiplication(matrix1, matrix2):
    for i in range(len(matrix1)): # To zwróci liczbę wierszy
        for j in range(len(matrix2[0])): # To zwróci liczbę kolumn
            for k in range(len(matrix2)): # Tutaj długośc drugiej macierzy
                multiplication_result[i][j] += matrix1[i][k] * matrix2[k][j]

def main():
    A = [[1,1,1],[1,1,1],[1,1,1]]
    B = [[2,2,2],[2,2,2],[2,2,2]]
    two_matrix_addition(A, B)
    print(addition_result)
    two_matrix_multiplication(A, B)
    print(multiplication_result)

if __name__ == "__main__":
    main(  )

