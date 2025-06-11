mas_num = (99, 3, 1, 5, 86, 17, -2, 7, -4 , -88, 234, 66)
positiv_num = []
for i in mas_num:
    if 100 > i > 9:
        positiv_num.append(i)
positiv_num.sort()
print(positiv_num)