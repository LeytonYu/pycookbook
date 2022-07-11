import json


def str_to_json(value):
    if value and not isinstance(value, list):
        try:
            tp = json.loads(value)
            return [tp] if isinstance(tp, int) else tp
        except Exception as e:
            print(str(e))
            try:
                return json.loads(value.replace("'", '"'))
            except:
                return []
    elif value and isinstance(value, list):
        return value
    else:
        return []


def test_demo_one():
    a = ['adfas', '11', "[1, 2, 3]", 15]
    for p in a:
        print(str_to_json(p))
    # a = json.loads("1")
    # print(a)


if __name__ == '__main__':
    test_demo_one()
