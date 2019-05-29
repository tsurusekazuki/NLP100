import re
from ch3_module import ch3_extract_json

lines = ch3_extract_json.extract_json('イギリス').split('\n')

for line in lines:
    category = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category is not None:
        print(category.group(1))



