matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

sum_matrix_elem = 0
for i in matrix:
    for j in range(len(matrix)):
        sum_matrix_elem += i[j]

print(sum_matrix_elem)