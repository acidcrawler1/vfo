class Master(object):
    def __init__(self, value):
        self.value = value

    def func(self):
        print('Master.func', self.value)

    def cool(self):
        print('Master.cool')
        self.func()

p = Master(35)


class Child(Master):
    def lisa(self):
        print('Child.lisa')


class Child2(Master):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value) # Initialize parent

    def func(self):
        print('New cool func')
        super().func()

class Child3(Child, Child2):
    def test(self):
        print('testing fästing')