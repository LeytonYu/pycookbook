import json


def str_to_json(value):
    if value and not isinstance(value, list):
        try:
            return json.loads(value)
        except:
            try:
                return json.loads(value.replace("'", '"'))
            except:
                return []
    elif value and isinstance(value, list):
        return value
    else:
        return []


with open('用户意向高校.json', encoding='utf8') as f:
    a = json.load(open('用户意向高校.json', encoding='utf8'))

    st = {}
    for obj in a.get('RECORDS'):
        for key, value in obj.items():
            lst = str_to_json(value)
            for item in lst:
                st.setdefault(item['name'], 0)
                st[item['name']] += 1
    res = sorted(st.items(), key=lambda x: x[1], reverse=True)[:100]
    res_wb = {obj[0]: obj[1] for obj in res}
    print(res_wb)
    with open('top_intention_university_leyton.json', 'w', encoding='utf8') as ff:
        json.dump(res_wb, ff, ensure_ascii=False)
