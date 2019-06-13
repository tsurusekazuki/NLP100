def tab_str_to_dict(tab_str: str) -> dict:

    elements = tab_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def morphemes_to_sentence(morphemes: list) -> list:

    sentences_list = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences_list.append(morpheme)
            sentence = []

    return sentences_list


with open('neko.txt.mecab', encoding='utf-8') as input_file:
    morphemes = [tab_str_to_dict(line) for line in input_file]

sentences = morphemes_to_sentence(morphemes)

print(sentences[::100])
print(morphemes[::100])

verbs_surface = [morpheme['surface'] for morpheme in morphemes if morpheme['pos1'].find('動詞') == 0]
verbs_base = [morpheme['base'] for morpheme in morphemes if morpheme['pos1'].find('動詞') == 0]
nouns_suru = [morpheme['surface'] for morpheme in morphemes if morpheme['pos1'] == '名詞-サ変接続']

# 結果の確認
print(verbs_surface[::100])
print(verbs_base[::100])
print(nouns_suru[::100])