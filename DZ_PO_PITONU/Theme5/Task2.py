s = ""
matrix = []
print("¬ведите матрицу, если вы хотите закончить, введите Ђendї в следующей строке")
while True:
    s = input()
    if s == "end":
        break
    matrix.append(list(map(int, s.split())))

for i in range(len(matrix)):
    matrix[i] = [matrix[i][-1]] + matrix[i] + [matrix[i][0]]
matrix = [matrix[-1]] + matrix + [matrix[0]]

matrix2 = []
for i in range(1, len(matrix)-1):
    matrix2.append([0] * (len(matrix[i])-2))
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        matrix2[i][j] = matrix[i+2][j+1] + matrix[i][j+1] + matrix[i+1][j+2] + matrix[i+1][j]
for i in matrix2:
    print(*i)
