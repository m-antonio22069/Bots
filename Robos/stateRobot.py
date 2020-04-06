import json


def save(content):
    with open(file='content.json', mode='w') as f:
        return json.dump(obj=content, fp=f, indent=4, ensure_ascii=False)


def load():
    with open(file='content.json', mode='r') as f:
        return json.load(fp=f)