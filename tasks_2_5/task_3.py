import random

mas = list()
while len(mas) < 5:
    num_r = random.randint(1, 100)
    if num_r % 2 == 0:
        mas.append(num_r)
        mas.sort()

print(mas)