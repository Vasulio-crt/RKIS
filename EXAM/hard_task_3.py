from random import randint

N = list(range(1, 10))
N.pop(randint(0, 8))
print(N)

len_n = len(N) + 1
none_num = (len_n * (len_n + 1) // 2) - sum(N)
print(none_num)