split_1column_text_list = []
with open('hightemp.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        split_1column_text_list.append(line.split()[0])
split_1column_text_set = set(split_1column_text_list)
print(split_1column_text_set)
