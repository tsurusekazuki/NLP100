with open('col1.txt', mode='r') as f1:
    with open('col2.txt', mode='r') as f2:
        with open('merge.txt', mode='a') as f3:
            for col1_line, col2_line in zip(f1, f2):
                f3.write('{}    {}'.format(col1_line.rstrip('\n'), col2_line))
