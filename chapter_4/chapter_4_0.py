import MeCab


with open('neko.txt', encoding='utf-8') as f:
    data = f.read()
    _m = MeCab.Tagger('-Ochasen')
    parse = _m.parse(data)

with open('neko.txt.mecab', encoding='utf-8', mode='a') as f1:
    f1.write(parse)