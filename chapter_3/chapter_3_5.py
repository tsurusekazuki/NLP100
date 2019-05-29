import re

from ch3_module import ch3_extract_json

lines = ch3_extract_json.extract_json('イギリス').split('\n')

for line in lines:
    file_line = re.search("", line)

