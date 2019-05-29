import re
from ch3_module import ch3_extract_json

lines = ch3_extract_json.extract_json('イギリス').split('\n')

for line in lines:
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2))



