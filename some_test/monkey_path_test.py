from some_test.models.leyton_test import MyBall


class MyBallV2(MyBall):
    def __init__(self, ggj, fxxk=None, apple=None, on_delete=None):
        if not on_delete:
            on_delete = 'fucking fuck'
        super(MyBallV2, self).__init__(on_delete, ggj, fxxk=None, apple=None)


if __name__ == '__main__':
    a = MyBallV2(ggj='ggj oo')
    print(a.get_on_delete())