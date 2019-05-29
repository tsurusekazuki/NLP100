with open('hightemp.txt') as f:
    lines = f.readlines()

for line in sorted(lines, key=lambda x: x.split()[2]):
    print(line)