f = open('hightemp.txt')
with open('col1.txt', mode='a') as f_1:
    with open('col2.txt', mode='a') as f_2:
        for text in f:
            tab_to_space_text = text.replace('  ', ' ')
            split_text = tab_to_space_text.split()
            f_1.write('{}\n'.format(split_text[0]))
            f_2.write('{}\n'.format(split_text[1]))
