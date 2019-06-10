import re
from ch3_module import ch3_extract_json


def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    return str

temp_dict = {}
lines = ch3_extract_json.extract_json(u"イギリス").split("\n")

for line in lines:
    category_line = re.search("^\|(.*?)\s=\s(.*)", line)
    if category_line is not None:
        temp_dict[category_line.group(1)] = remove_markup(category_line.group(2))

for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
    print(k, v)