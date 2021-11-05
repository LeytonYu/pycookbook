# python对象序列化


import pickle


def simple_exp():
    data = ['俞立栋', 'hhh', '慧慧']
    with open('pickle_smp', 'wb') as f:
        pickle.dump(data, f)

    s = pickle.dumps(data)

    # 复原
    with open('pickle_smp', 'rb') as f:
        data_v = pickle.load(f)
        print(data_v)

    data_w = pickle.loads(s)
    print(data_w)


def second_exp():
    with open('pickle_second', 'wb') as f:
        pickle.dump([1, 2, 3, 4], f)
        pickle.dump('I like rice', f)
        pickle.dump({'lss': '李舜生', 'ymj': '樱满集'}, f)

    with open('pickle_second', 'rb') as f:
        for i in range(3):
            print(pickle.load(f))


if __name__ == '__main__':
    second_exp()
