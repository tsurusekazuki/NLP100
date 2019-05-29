import json


def extract_json(title):
    with open("jawiki-country.json") as f:
        while True:
            article_json = f.readline()
            if not article_json:
                break
            article_dict = json.loads(article_json)
            if article_dict['title'] == title:
                return article_dict['text']


