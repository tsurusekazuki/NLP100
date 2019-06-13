import ngram


def tab_str_to_dict(tab_str: str) -> dict:

    elements = tab_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


with open('neko.txt.mecab', encoding='utf-8') as input_file:
    morphemes = [tab_str_to_dict(line) for line in input_file]


def ngram_to_list(lst: list, n: int = 3) -> list:
    index = ngram.NGram(N=n)
    result = [row for row in index.ngrams(lst)]
    return result


def is_nou_no_nou(words: list, ) -> bool:
    return (type(words) == list) and (len(words) == 3) and \
           (words[0]['pos1'].find('名詞') == 0) and \
           (words[1]['surface'] == 'の') and \
           (words[2]['pos1'].find('名詞') == 0)


# 「名詞-の-名詞」を含むNグラムのみを抽出
noun = [ngram for ngram in ngram_to_list(morphemes) if is_nou_no_nou(ngram)]

noun = [''.join([word['surface'] for word in ngram]) for ngram in noun]

print(noun[::100])

