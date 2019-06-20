def tab_str_to_dict(tab_str: str) -> dict:

    elements = tab_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def convert_morphemes():
    with open('neko.txt.mecab', encoding='utf-8') as input_file:
        morphemes = [tab_str_to_dict(line) for line in input_file]
    return morphemes

