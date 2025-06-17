num = int(input("Введите число: "))
dividers = []

for i in range(1, num):
    if num % i == 0:
        dividers.append(i)

if sum(dividers) == num:
    print(f"Число {num} совершенно")
else:
    print(f"Число {num} несовершенно")
