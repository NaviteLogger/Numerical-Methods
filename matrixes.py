matrix=[[1,0,0],[2,3,0],[4,5,6]]
right_side=[1,2,3]
solution=[0,0,0]

# rozwiązanie równania macierzowego L * x = b
# macierz L jest macierzą dolnotrójkątną
def findx_lower_triangle(L, b):
    x = []
    for i in range(len(L)):
        suma = 0
        for k in range(i):
            suma += L[i][k] * x[k]
        x.append((b[i] - suma) / L[i][i])
    return x


if __name__ == "__main__":
    findx_lower_triangle(matrix, right_side, solution)
    print(solution)
    print("Done")
