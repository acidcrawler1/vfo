# test2.py

class Savings(object):
    def __init__(self, name, age, banksavings, salary):
        self.name = name
        self.age = age
        self.banksavings = banksavings
        self.salary = salary
    
    def calc_salary(self, months):
        return months * self.salary

