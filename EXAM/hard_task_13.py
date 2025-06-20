str1 = "aabcccaaadddffffff"
str2 = ""
last_letter = str1[0]
num = 0
for i in str1:
    if last_letter == i:
        num += 1
    else:
        str2 += last_letter + str(num)
        num = 1
    last_letter = i
str2 += last_letter + str(num)

print(str2)