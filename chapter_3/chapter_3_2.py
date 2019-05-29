from ch3_module import ch3_extract_json


def category_row(lines):
    for line in lines:
        if "Category" in line:
            print(line)


if __name__ == '__main__':
    s = ch3_extract_json.extract_json('イギリス').split('\n')
    category_row(s)

