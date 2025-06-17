matrix = [[1, 2, 3],
          [4, 9, 6],
          [7, 8, 5]]

max_matrix_elem = matrix[0][0]
for i in matrix:
    for j in range(len(matrix)):
        if max_matrix_elem < i[j]:
            max_matrix_elem = i[j]

print(max_matrix_elem)