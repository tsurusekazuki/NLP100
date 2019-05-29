import sys
input_file = sys.argv[1]
n = sys.argv[2]

with open(input_file) as f:
    lines = f.readlines()

for line in lines[:int(n)]:
    print(line)
