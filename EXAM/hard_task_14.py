words = ["123", "ooo", "321", "101", "808",
         "777", "ooo", "101", "908", "go"]
good = list()

for i in range(len(words)):
    for j in range(i+1, len(words)):
        cheak = words[i] + words[j]
        if cheak == cheak[::-1]:
            good.extend([words[i], words[j]])

print(good)