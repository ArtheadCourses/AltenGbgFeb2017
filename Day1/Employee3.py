
class Employee:
    raise_amnt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}", {int(self.pay)})'

    def __str__(self):
        return "The name of this employee is {}".format(self.first)

    def __add__(self, other):
        return Employee(self.first, other.last, self.pay + other.pay)

    def give_raise(self):
        self.pay *= self.raise_amnt

class Developer(Employee):
    raise_amnt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

def main():
    emp1 = Employee("John", "Smith", 50000)
    emp2 = Developer("Anna", "Jones", 55000, 'Python')

    emp2.give_raise()
    print(type(emp2))
    print(repr(emp2))

if __name__ == '__main__':
    main()