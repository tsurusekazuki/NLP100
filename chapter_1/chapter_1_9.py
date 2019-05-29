def cipher(s):
    result = []
    for c in s:
        if c.islower():
            result.append(chr(219-ord(c)))
        else:
            result.append(c)
    return ''.join(result)


input_encode = 'hEllO world'
print(cipher(input_encode))