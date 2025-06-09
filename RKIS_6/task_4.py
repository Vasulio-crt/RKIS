mas = (-1, -33, 777, 315, 86, 17, -676)
flag, last_num = True, 0

for i in range(len(mas)):
    if mas[i] > 0 and flag:
        print("Max num:", mas[i])
        flag = False
    elif mas[i] < 0:
        last_num = mas[i]
print("Min num:", last_num)