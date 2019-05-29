import json

with open("jawiki-country.json") as f:
    while True:
        article_json = f.readline()
        if not article_json:
            break
        article_dict = json.loads(article_json)
        if article_dict['title'] == "イギリス":
            print(article_dict['text'])

# 改行を含まない場合
# import json
#
# with open("jawiki-country.json") as f:
#     while True:
#         article_json = f.readline()
#         if not article_json:
#             break
#         article_dict = json.loads(article_json)
#         if article_dict['title'] == "イギリス":
#             print(article_dict['text'].replace('\n', ''))



