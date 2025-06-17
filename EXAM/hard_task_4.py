mas = [7, 6, 5, 4, 3, 2, 1]
mas_revers = []
len_mas = len(mas)

for i in range(len_mas):
    mas_revers.append(mas[len_mas - i - 1])

print(mas_revers)