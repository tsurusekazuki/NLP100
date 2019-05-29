f = open('hightemp.txt')

for text in f:
    tab_to_space_text = text.replace('  ', ' ')
    print(tab_to_space_text)