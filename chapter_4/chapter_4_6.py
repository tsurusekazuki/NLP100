from ch4_module import ch4_morphemes

morphemes = ch4_morphemes.convert_morphemes()
dict_count_word = {}

for dict_morpheme in morphemes:
    dict_count_word[dict_morpheme['surface']] = dict_count_word.get(dict_morpheme['surface'], 0) + 1

sort_dict_count_word = sorted(dict_count_word.items(), key=lambda x: x[1], reverse=True)

print(sort_dict_count_word)