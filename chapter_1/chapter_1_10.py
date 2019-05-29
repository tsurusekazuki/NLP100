import random
input_encode = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
input_split_encodes = input_encode.split()
result = []
for encode in input_split_encodes:
    if len(encode) >= 5:
        random_encode = encode[0] + ''.join(random.sample(encode[1:-1], len(encode[1:-1]))) + encode[-1]
        result.append(random_encode)
    else:
        result.append(encode)
print(' '.join(result))
