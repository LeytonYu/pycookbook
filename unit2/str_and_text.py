import re


def my_split():
    line = 'adf jlkj; kjl,  akdf,jkad,   foo'
    print(re.split(r'[;,\s]\s*', line))

    print(line.startswith(('li', 'dd', 'ad')))

    print(line.find('古'))


def re_desc():
    """
    match()只匹配开头
    findall()匹配所有
    finditer()返回迭代器
    re.compile()预编译
    :return:
    """
    str_pat = re.compile(r'C(.*?)r')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))
    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))


def justify_str():
    text = "Hello World"
    a = text.ljust(20, '=')
    b = text.rjust(20, '+')
    c = text.center(20, '-')
    print(a)
    print(b)
    print(c)
    d = format(text, '=>20')
    e = format(text, '*<20')
    f = format(text, '~^20')
    print(d)
    print(e)
    print(f)
    g = '{:>10} {:>10}'.format('Hello', 'World')
    print(g)


def link_str():
    data = ['yld', 173, 58]
    ss = ','.join(str(d) for d in data)  # 生成器，节省内容开销
    print(ss)
    a = 1
    b = 2
    c = 3
    print(a, b, c, sep=":")     # 默认分割用空格


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def use_missing():
    name = 'Leyton'
    n = 12
    s = '{name} has {n} messages'
    a = s.format_map(SafeSub(vars()))
    print(a)


if __name__ == '__main__':
    use_missing()
