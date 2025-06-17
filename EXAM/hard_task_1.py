mas = [2, 3, 1, 7, 5, 6]
for i in range(len(mas)):
    for j in range(len(mas) - 1 - i):
        if mas[j] > mas[j + 1]:
            mas[j], mas[j + 1] = mas[j + 1], mas[j]

print(mas)