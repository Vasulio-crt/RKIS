mas = [1, 2, 3, 7, 5, 6, 4]
max_el = [mas[0], mas[1]]
for i in mas:
    if i > max_el[0]:
        max_el[1] = max_el[0]
        max_el[0] = i
    elif i > max_el[1]:
        max_el[1] = i

print(max_el[1])