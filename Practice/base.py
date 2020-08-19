class Base:
    def __init__(self):
        print('Base Init called')

    def f(self):
        print('Base.f called')


class Sub(Base):
    def __init__(self):
        super().__init__()
        print('Sub Init Called')

    def f(self):
        print('sub.f called')

