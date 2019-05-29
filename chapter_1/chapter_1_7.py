def n_gram_s(s, N):
    result = []
    for i in range(len(s)):
        result.append(s[i:i+N])
    return result

x = n_gram_s('paraparaparadise', 2)
y = n_gram_s('paragraph', 2)

s_union = set(x) | set(y)
s_intersection = set(x) & set(y)
s_symmetric_difference = set(x) ^ set(y)
print('和烏合', s_union)
print('積集合', s_intersection)
print('差集合', s_symmetric_difference)

if 'se' in x:
    print(True)
else:
    print(False)

if 'se' in y:
    print(True)
else:
    print(False)