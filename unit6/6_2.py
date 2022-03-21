import json
from pprint import pprint

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23,
    'cn_name': '爱吃ლ(′◉❥◉｀ლ)'
}


def str_and_json():
    global data
    json_str = json.dumps(data)
    data = json.loads(json_str)
    print(json_str)
    print(data)


def file_and_json():
    # with open('data_json.json', 'r', encoding='utf8') as f:
    #     pprint(json.load(f))

    with open('data_json_v2.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


class JsonObject:
    def __init__(self, d):
        self.__dict__ = d


def json_object():
    s = '{"武器": "剑", "name": "ACME", "shares": 50, "price": 490.1}'
    ds = json.loads(s, object_hook=JsonObject)
    print(ds.武器, ds.name)


if __name__ == '__main__':
    # str_and_json()
    # file_and_json()
    json_object()