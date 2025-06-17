str1 = "aabcccaaadddffffff"
str2 = ""
last = str1[0]
num = 0
for i in str1:
    if last == i:
        num += 1
    else:
        str2 += last + str(num)
        num = 1
    last = i
str2 += last + str(num)

print(str2)