# table.py
class Table (object):
    def __init__(self, name, age, savings, salary):
        self.name = name
        self.age = age
        self.savings = savings
        self.salary = salary

    @classmethod
    def from_string(cls, s): # cls in "Table"
        parts = s.split(',')
        return cls(parts[0], int(parts[1]), int(parts[2]), int(parts[3]))


    def list_objects(objects, cnames):
        for c in cnames:
            print('{:>5s}'.format(c), end='...')
        print()
        for obj in objects:
            for col in cnames:
                # print(col, obj.name)
                print("{} ---".format(str(getattr(obj, col))), end='    ')
            print()
            # print('test {}'.format(str(getattr(o, c))), end='  ')
from test2 import Savings
sl = [Savings('Johan', 35, 100000, 35000), Savings('Peter', 39, 8000000, 55000)]
cl = ['name', 'salary']

# import importlib
# importlib.reload(table)