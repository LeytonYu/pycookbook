
def test():
    try:
        a = {'a': 'adf'}
        b = 1 / 0
    except:
        print('报错了')
        a = {'a': 'asdfasdf'}
        return a
    finally:
        print(a)
        return a


b = test()
