with open('hightemp.txt') as f:
    lines = f.readlines()

words = {}
for line in lines:
    line = line.split()[0]
    words[line] = words.get(line, 0) + 1
sort_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
for sort_word in sort_words:
    print(sort_word[0])
 