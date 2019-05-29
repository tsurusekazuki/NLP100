def n_gram_c(s, N):
    result = []
    words = s.split()
    for i, word in enumerate(words):
        result.append(words[i:i+N])
    return result


def n_gram_s(s, N):
    result = []
    for i in range(len(s)):
        result.append(s[i:i+N])
    return result


s, n = 'I am an NLPer', 2
print(n_gram_c(s, n))
print(n_gram_s(s, n))

