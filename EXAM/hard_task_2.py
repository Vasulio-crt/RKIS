line = "the quick brown fox jumps over the lazy dog"
line_revers = ""
len_line = len(line)

for i in range(len_line):
    line_revers += line[len_line - i - 1]

print(line_revers)