mas = [1, 2, 3, 4, 5]
targer = 5

len_mas = len(mas)

for i in range(len_mas):
    for j in range(i+1, len_mas):
        if mas[i] + mas[j] == targer:
            print(mas[i], mas[j])