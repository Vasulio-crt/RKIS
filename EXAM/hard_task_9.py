alphabet = dict()
line = "Today is a beautiful day"
for i in line:
    if i != ' ':
        if i not in alphabet:
            alphabet[i] = 1
        else:
            alphabet[i] += 1

for k, v in alphabet.items():
    print(f"{k}: {v}")