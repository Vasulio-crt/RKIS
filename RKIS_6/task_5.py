C = "z"
A = "zoz z zzo zdksjfksz"
count = 0
for i in A.split():
    if i[0] == C and i[-1] == C and len(i) > 1:
        count += 1

print(count)