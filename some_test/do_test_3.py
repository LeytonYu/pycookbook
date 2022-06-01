import numpy as np


def workbreak_fun(s, dicts):
    n = len(s)
    if len(s) == 0 or len(dicts) == 0:
        return False
    wordchack = np.zeros(n + 1)
    wordchack[0] = True
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if wordchack[j] and s[j:i] in dicts:
                wordchack[i] = True
                break

    return bool(wordchack[n])


def get_max_continuously_list(raw_list: list):
    length = len(raw_list)
    start_end = []
    max_value = 0
    for i in range(length):
        if raw_list[i] > 0:
            now_temp = raw_list[i]
            max_temp = raw_list[i]
            e = i
            if i + 1 < length:
                for j in range(i + 1, length):
                    e = j - 1
                    if now_temp + raw_list[j] > 0:
                        now_temp += raw_list[j]
                        if now_temp > max_temp:
                            max_temp = now_temp
                            e = j
                    else:
                        break
                if max_temp > max_value:
                    max_value = max_temp
                    start_end = [i, e]
    print(max_value, start_end)
    return max_value, start_end


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError, ValueError):
    #     pass

    return False


def best_way(raw_list):
    length = len(raw_list)
    if length < 1:
        return 0
    temp = [0] * length
    temp[0] = raw_list[0]
    for i in range(1, length):
        temp[i] = max(temp[i - 1] + raw_list[i], raw_list[i])
    max_value = temp[0]
    for a in temp:
        max_value = max(max_value, a)
    print(max_value)
    return max_value


def test_first():
    strlist = "carssa"
    dictlist = ["car", "ca", 'ars', 'sa']
    print(workbreak_fun(strlist, dictlist))


def test_second():
    s = [int(i) for i in input('请输入数字，用空格分割:\n').split(' ') if is_number(i)]
    print(s)
    max_value, start_end = get_max_continuously_list(raw_list=s)
    max_value_2 = best_way(raw_list=s)


if __name__ == '__main__':
    test_first()
    # test_second()