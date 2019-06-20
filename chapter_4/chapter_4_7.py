import matplotlib.pyplot as plt
from ch4_module import ch4_morphemes
from matplotlib.font_manager import FontProperties

morphemes = ch4_morphemes.convert_morphemes()
dict_count_word = {}
fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc')

for dict_morpheme in morphemes:
    dict_count_word[dict_morpheme['surface']] = dict_count_word.get(dict_morpheme['surface'], 0) + 1

sort_dict_count_word = sorted(dict_count_word.items(), key=lambda x: x[1], reverse=True)

name = [value[0] for value in sort_dict_count_word[:10]]
value = [value[1] for value in sort_dict_count_word[:10]]

plt.bar(name, value)
plt.xticks(name, fontproperties=fp)
plt.show()

