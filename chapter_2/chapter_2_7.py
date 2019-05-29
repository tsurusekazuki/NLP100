import sys

n = sys.argv[1]

with open('hightemp.txt') as f:
    lines = f.readlines()

split_break_num = len(lines) // int(n)

for i in range(int(n)):
    with open("split%s.txt" % str(i), "w") as w:
        w.writelines(lines[i*split_break_num:(i+1)*split_break_num])
